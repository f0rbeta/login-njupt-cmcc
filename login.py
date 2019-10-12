import os
import re
import requests
from pprint import pprint
'''南京邮电大学'NJUPT-CMCC'的网络认证，选择无线来自动获取需要进行认证IP地址，再POST数据包进行网络认证
'''

# 确认主机操作系统
if os.name == 'posix':
	print('你的操作系统是类UNIX/OS X')
	cmdstr = 'ifconfig '
elif os.name == 'nt':
	print('你的操作系统是Windows')
	cmdstr = 'ipconfig '

# 确认无线网卡名称
# eth = input('请输入你的网卡名称:')
# cmdstr = cmdstr + eth

# 获取ip
eth_info = os.popen(cmdstr)
eth_info = eth_info.read()
addr = re.search('10\.[0-9]*\.[0-9]*\.[0-9]*',eth_info)
ipaddr = addr.group()
print('你的认证IP:',ipaddr)

# 模拟post请求
# 请求URL
# 其实第二个IP可以不更改，最主要的参数是wlanuserip
url = 'http://p.njupt.edu.cn:801//eportal/?c=ACSetting&a=Login&protocol=http:&hostname=p.njupt.edu.cn&iTermType=1&wlanuserip=%s&wlanacip=null&wlanacname=null&mac=00-00-00-00-00-00&ip=%s&enAdvert=0&queryACIP=0&loginMethod=1' % (ipaddr,ipaddr) 
print('访问的URL如下:\n',url)
print(20*'*')

# Post数据
# source_data里面填写自己的一卡通号和密码
source_data = "DDDDD=,0,一卡通号@cmcc&upass=密码&R1=0&R2=0&R3=0&R6=0&para=00&0MKKey=123456&buttonClicked=&redirect_url=&err_flag=&username=&password=&user=&cmd=&Login=&v6ip="
data = dict(k.split("=") for k in source_data.split("&") if k)  # 转化为字典形式

# 请求头
headers = {"Host": "p.njupt.edu.cn:801",
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Accept-Encoding":"gzip, deflate",
"Content-Type":"application/x-www-form-urlencoded",
"Content-Length":"176",
"Connection":"close",
"Referer":"http://p.njupt.edu.cn/a70.htm?wlanuserip=10.163.33.136&wlanacip=null&wlanacname=null&vlanid=0&ip=10.163.33.136&ssid=null&areaID=null&mac=00-00-00-00-00-00",
"Cookie":"program=2; vlan=0; ip=10.163.33.136; ssid=null; areaID=null; md5_login2=,0,学号@cmcc|密码; PHPSESSID=pgq5hv0e2i31a8i5li545qerb1; DDDDD=,0,学号@cmcc",
"Upgrade-Insecure-Requests":"1"
}
# pprint(data)

res = requests.post(url=url, headers=headers, data=data)
if res.status_code == 200:
	print('认证成功！')
else:
	print("呀~失败了。")

# print(res.text)

