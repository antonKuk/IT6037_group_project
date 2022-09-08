python -m venv .venv  #or any other name
source .venv/bin/activate
View > Command Palette or (Ctrl+Shift+P) Then select the .venv Python from: Select Interpreter command.
python -m pip install --upgrade pip
pip install Django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
pip install -r requirements.txt
pip freeze > requirements.txt  #to create txt file for reqirements
pip install django-crispy-forms     #for bootstrap forms
pip install crispy-bootstrap5

https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html How to Reset Migrations