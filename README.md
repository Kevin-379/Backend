Setup:
  1) Install python 3
  2) Run 'pip install -r requirements.txt' in command prompt
  3) cd to mysite directory
  4) run 'python manage.py makemigrations'
  5) run 'python manage.py migrate'
  6) run 'python manage.py runserver'
  7) run 'python manage.py createsuperuser', enter credentials for admin
  8) In your web browser, go to localhost:8000

Notes:
  1) Website is not fully functional
  2) A .env file containing my SECRET_KEY, email, password has been included (mysite/mysite/.env). If you want to use your own email, see .env-example for format and replace my .env
  3) The following users were not working on a different machine. If they are not present (can check after logging in admin page and going to profiles) you can register.
     username: useri
     password: password@i ,(i=1, 2, 3)
  4) admin route: localhost:8000/admin
