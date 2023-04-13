## qrcode-bot

> 一个 `telegram bot`，用来把文字等信息生成二维码。

---
### 使用说明

1.下载源码

```
git clone https://github.com/sskaykat/qrcode-bot.git
```

2.修改 `config.ini` 文件，把 `TOKEN` 替换

```
[telegram]
TOKEN = 5007260780:AAE************6DOCytU
```

3.安装运行所需的 `python` 库

`pip install requirements.txt`

4.运行 `python qrcodebot.py` 或者 `python3 qrcodebot.py` 即可

### 使用 `docker` 安装

1.把代码打包成镜像

```
docker build -t qrcodebot:latest .
```

2.运行

```
docker run -d --name qrcodebot -v /localpath:/qrcode qrcodebot:latest
```

### 使用 `docker-compose` 安装，创建 `docker-compose.yml` , 文件内容如下：

```
version: '3'
services:
  qrcodebot:
    image: qrcodebot:latest
    container_name: qrcodebot
    volumes:
      - /localpath:/qrcode
    restart: always
    detach: true
```

运行 `docker-compose up -d`


