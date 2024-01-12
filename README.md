# ResPusher
通过微信发送实验的结果

目前实现的方式有

1. Server 酱

2. WxPusher

## 安装

1. 通过官方源安装

```shell
pip install ResPusher -i https://pypi.org/simple
```

2. 下载 github 库

```shell
cd ResPusher
pip install .
```

## 使用

### Server酱

![image-20240113170246096](https://gitlab.com/XLJZT/img/-/raw/main/blog/pictures/2024/01/13_17_2_50_image-20240113170246096.png)

微信搜索 方糖 关注公众号，或者前往[官网链接](https://sct.ftqq.com/)进行登录关注公众号

登录成功后会获得 SendKey（必需）

![image-20240113170552577](https://gitlab.com/XLJZT/img/-/raw/main/blog/pictures/2024/01/13_17_5_54_image-20240113170552577.png)

代码调用示例

```python
from ResPusher import *

res = ServerChan(key="serverchan sendkey").send_message(title="实验结果", content="结果远超当前 sota 值")
print(res)
```

结果展示

![image-20240121224836556](https://gitlab.com/XLJZT/img/-/raw/main/blog/pictures/2024/01/21_22_48_36_image-20240121224836556.png)

## WxPusher

通过[Wxpusher 管理后台链接](https://wxpusher.zjiecode.com/admin/)微信扫码注册进入后台

具体步骤：[[注册并且创建应用](https://wxpusher.zjiecode.com/docs/#/?id=注册并且创建应用)]

![image-20240113190944113](https://gitlab.com/XLJZT/img/-/raw/main/blog/pictures/2024/01/13_19_10_0_image-20240113190944113.png)

![image-20240113190955690](https://gitlab.com/XLJZT/img/-/raw/main/blog/pictures/2024/01/13_19_9_57_image-20240113190955690.png)

appToken 和 UID 是必需的参数

代码调用示例

```python
from ResPusher import *

res = WxPusher(apptoken="wxpusher apptoken", uids=["wxpusher uid"]).send_message(title="实验结果", content="结果远超当前 sota 值")
print(res)
```

结果展示

![image-20240121224916611](https://gitlab.com/XLJZT/img/-/raw/main/blog/pictures/2024/01/21_22_49_16_image-20240121224916611.png)

## 接口代码来源

[serverchan-demo](https://github.com/easychen/serverchan-demo)

[wxpusher-sdk-python](https://github.com/wxpusher/wxpusher-sdk-python/tree/1713c37dcaa5014a374644fb96243368da804790)