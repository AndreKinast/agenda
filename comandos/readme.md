Iniciar projeto Django

````
python -m venv agenda
pyhon agenda\Scripts\activate
pip install django
django-admin startproject project .
python manage.py startapp contact
base.html
style.css

````

configurar o git

````
git config --global user.name 'seunome'
git config --global user.email 'seuemail'
git config --global init.defaultBranch main

#configure o gitignore
git init

````
Migrando a base de dados do Django

````
python manage.py makemigrations
python manage.py migrate
````
Criando e modificando a senha de um super usuário Django

````
python manage.py createsuperuser
python manage.py changepassword USERNAME
````