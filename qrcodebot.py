import telebot
import qrcode
import configparser
from PIL import Image
from io import BytesIO

# 创建配置解析器
config = configparser.ConfigParser()
# 从配置文件中读取配置
config.read('config.ini')

# 获取 Telegram Bot Token
TOKEN = config['telegram']['TOKEN']

# 创建 Telegram Bot 客户端
bot = telebot.TeleBot(TOKEN)

# 处理 /start 命令
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '欢迎使用二维码生成器Bot！发送需要生成二维码的文本给我吧！')

# 处理用户发送的文本消息
@bot.message_handler(func=lambda message: True)
def generate_qrcode(message):
    try:
        # 获取用户发送的文本消息
        text = message.text
        # 生成二维码
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # 将二维码图片保存到 BytesIO 对象中
        img_bytes_io = BytesIO()
        img.save(img_bytes_io, format='PNG')
        img_bytes_io.seek(0)
        
        # 将生成的二维码图片发送给用户
        bot.send_photo(message.chat.id, img_bytes_io)
        
        # 保存二维码图片到本地
        img.save('qrcode.png', format='PNG')
    except Exception as e:
        bot.reply_to(message, f'生成二维码时出错：{e}')

# 启动 Telegram Bot
bot.polling()
