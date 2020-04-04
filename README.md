Setup:
  1) Install python 3
  2) Run 'pip install -r requirements.txt' in command prompt
  3) cd to mysite directory, and run:
      'python manage.py makemigrations'
      'python manage.py migrate'
  4) run 'python manage.py runserver'
  5) In your web browser, go to localhost:8000

Notes:
  1) Website is not fully functional
  2) username: admin
     password: admin
  3) If admin is not present, run 'python manage.py createsuperuser'
  4) A .env file containing my SECRET_KEY, email, password has been included (mysite/mysite/.env). If you want to use your own email, see .env-example for format and replace my .env
  5) username: useri
     password: password@i ,(i=1, 2, 3)
