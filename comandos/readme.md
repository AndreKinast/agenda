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

````
#criar models na pasta model de contact
#criar campos e deteminar o tipo de arquivo de cada um
#configurar pasta settings
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
#criar campo imagem, executar o comando 'pip install pillow'
#migrar a base de dados django
#configurar pasta gitignore ---'static/', 'media/'

````

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

Configurar URLS para poder acessar as imagens dos contatos

````
#em urls do projeto:
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
````

Criar model foreignkey

````
Criar outro model
criar uma category no model já existente que recebe como parâmetro o novo model

 category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 blank=True, null=True)

fazer as migrações de dados django

registrar o novo model em contact-admin
````

Verbose name

````
em models configurar verbose name, para que substantivos singulares e plurais sejam escristos corretamente

````
criar foreignkey owner

````
#permite que cada contato criafo tenha identificado o usuário que o criou
from django.contrib.auth.models import User
criar campo owner --- para criar novos usuários

owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 blank=True, null=True)
fazer as migrações de dados django
````

criar contatos aleatórios com faker

````
pasta utils -- create_contacts.py

pip install faker

executar
python utils/create_contacts.py
````