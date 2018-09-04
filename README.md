# Mischung
Telegram bot for testing anything

Use ./[request.sh](https://github.com/Artyom-Barsov/Mischung/blob/master/request.sh) with [Telegram Bot API](https://core.telegram.org/bots/api#available-methods) methods in URL query string format as arguments to send request and get response from <api.telegram.org> of the bot.
For example:
```
curl "https://api.telegram.org/bot688343184:AAGnRwbHccoACNsrWr3N75_wnSesvp4t5dA/getMe"
```
or just:
```
./request.sh getMe
```
----------------------------------------------------------------------
### Setting up Git for GitHub:
```
ssh-keygen -t rsa -b 4096 -C "your_mail@example.com"
ssh-add ~/.ssh/your_key_name
```
<https://github.com/settings/keys>
```
git init
git remote add Mischung git@github.com:Artyom-Barsov/Mischung.git
git pull
```
----------------------------------------------------------------------
### Setting up for Heroku:
- Instal heroku
- Login on Heroku
- In Pipfile version:
```
[requires]
python_version = "3.5"
```
- Create Pipfile.lock:
```
pipenv lock
```
- In Procfile how to run:
```
web: python3 bot.py
```
- In requirements.txt are libraries.

```
heroku login
heroku git:remote -a app_name
heroku buildpacks:set heroku/python
heroku ps:scale web=1
heroku maintenance:off
heroku open
```
----------------------------------------------------------------------
### To GitHub:
```
git add .
git commit -am "commit on GitHub"
git push Mischung master
```
Automatic deploys to Heroku can be set up

----------------------------------------------------------------------
### To Heroku:
```
git add .
git commit -am "commit on Heroku"
git push heroku master
```
