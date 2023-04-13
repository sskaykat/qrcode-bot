FROM python:3.9-slim-buster

WORKDIR /qrcode

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./qrcodebot.py" ]
