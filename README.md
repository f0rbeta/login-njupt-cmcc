# NJUPT-CMCC
脚本进行网络认证 我觉得很计算机
## 你需要做什么
1. 修改程序内source_data,headers['Cookie']中的一卡通号和密码
2. 确认自己的网卡名称
3. 安装requests
## 运行方法
```shell
~/python_home$ python login.py
```
## 简单说明
因为mac os认证弹出的框不能保存账号密码，卡号又臭又长，差掉再打开浏览器认证有点麻烦，因此动手抓包分析了下，写了个小脚本，可能不够完善，但是凑合能用
