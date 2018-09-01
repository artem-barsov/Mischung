# Mischung
Telegram bot for testing anything

____________________________________
Setting up Git for GitHub:
```
ssh-keygen -t rsa -b 4096 -C "your_mail@example.com"
ssh-add ~/.ssh/your_key_name
https://github.com/settings/keys
git init
git remote add Mischung git@github.com:Artyom-Barsov/Mischung.git
```
____________________________________
To Heroku:
```
git add .
git commit -am "commit on Heroku"
git push heroku master
```
____________________________________
To GitHub:
```
git add .
git commit -am "commit on GitHub"
git push Mischung master
```
____________________________________
Start on Heroku:
```
codeheroku ps:scale web=1
heroku open
```
