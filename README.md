# YTDLMTB

## Установка
**ubuntu**

sudo apt install python3
python3 -m pip install --upgrade pip
pip3 install virtualenv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
sudo apt install ffmpeg


Перименовать examples.config.py на config.py
в config.py ввести в token в telegram_token
Пример:
    telegram_token = '123456:afdsgfwqdcfsad...'

Запуск:
    python3 main.py