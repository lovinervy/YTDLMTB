# YTDLMTB
## Что это?
Простой телеграм бот для скачивание видео с сайта **YouTube**

## Как работает?
Скидываете ютуб ссылку на видео.
Бот продублирует сообщение, но с контекстными(-ой) кнопками(-ой) с выбором качество видео
## Чем отличается от savefrom.net и ему подобных
-  Бот склеивает автоматически аудио и видео дорожки.

- Бот ~~не следит~~ имеет открытый исходный код и можно использовать, как пример для расширение функционала вашего бота.

## Установка
#### Ubuntu

```
sudo apt install python3
python3 -m pip install --upgrade pip
pip3 install virtualenv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
sudo apt install ffmpeg
```

Перименовать **examples.config.py** на **config.py**
в **config.py** ввести **token** в **telegram_token**

***Пример:***
```
telegram_token = '123456:afdsgfwqdcfsad...'
```

***Запуск:***
```
source venv/bin/activate
python3 main.py
```

------------


#### Windows

Скачать **[Python](https://www.python.org/downloads/)**

Во время установки Python поставить галочку на добавление в **PATH**

Запустить командную строку ***cmd***

В ***cmd*** добраться до корневой папки скаченного проекта

Далее выполняем последовательно следующие коды в ***cmd***

```
python -m pip install --upgrade pip
pip install virutalenv
python -m venv venv
.\venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r .\requirements.txt
```
***cmd*** пока не закрываем

Скачиваем **[ffmpeg](https://www.gyan.dev/ffmpeg/builds/)**

В скаченном архиве извлекаем **ffmpeg.exe** и кладем в корень проекта

В корне программы открываем файл **example.config.py** через **блокнот** (или её аналог) и ставим **токен** вашего **бота** в строку **telegram_token**

***Пример:***
```
telegram_token = '123456:afdsgfwqdcfsad...'
```

Переименовываем файл с **example.config.py** на **config.py**

В ***cmd*** пишем следующее

```
python main.py
```

При последующих запусках доходим до корня программы в **cmd**
Пишем последовательно следующие строки
```
.\venv\Scripts\activate
python main.py
```
