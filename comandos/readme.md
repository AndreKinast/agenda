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

Trabalhando com o model do django

````python

#import o módulo
from contact.models import Contact
#Cria um contato (Lazy)
#Retorna o contato
contact = Contact(**fields)
contact.save()
#Cria um contato(não Lazy)
#Retorna o contato
contact = Contact.objects.create(**fields)
#seleciona um contato através do id
#retorna o contato
contact = Contact.objects.get(id=1)
#edita um contato
#Retorna um contato
contact.field_name1 = 'novo valor'
contact.save()
#Apaga um contato
#Depende da base de dados, geralmente retorna o número de valores manipulado na base de dados
contact.delete()
#seleciona todos os contatos por id desc
#retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')
````