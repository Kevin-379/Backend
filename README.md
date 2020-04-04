Setup:
  1) Install python 3
  2) Run 'pip install -r requirements.txt' in command prompt
  3) cd to mysite directory
  4) run 'python manage.py makemigrations'
  5) run 'python manage.py migrate'
  6) run 'python manage.py runserver'
  7) run 'python manage.py createsuperuser', enter credentials for admin (Not necessary)
  8) In your web browser, go to localhost:8000

Notes:
  1) Website is not fully functional
  2) ADMIN
     username: KevinS_379
     password: fe1192be
  3) If admin is not present, run 'python manage.py createsuperuser'
  4) A .env file containing my SECRET_KEY, email, password has been included (mysite/mysite/.env). If you want to use your own email, see .env-example for format and replace my .env
  5) username: useri
     password: password@i ,(i=1, 2, 3)
