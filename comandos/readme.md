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
configurar css
````
no arquivo base.html criar a tag main class content
criar o block content
no arquivo index.html usar o block content
acessar os contatos através de contact_views

from contact.models import Contact

def index(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts,
    }
    return render (
        request,
        'contact/index.html',
        context
    )

    no block content de index html criar um for

````
configurar a tabela que apresentará os contatos

````
em index.html no block content configurar html para que apresente todos os contatos em uma tabela
em contact_views configurar a forma como a tabela se apresentará
````
configurar para acessar um único contato
````
criar template contact.html
extends global/base
criar view contact em contact_views
configurar url.py
configurar o link em index.html
````
criando o cabeçalho

````
em base.html criar a tag header
configurar o link da header para retornar a página inicial
criar o menu
criar campo de pesquisa

````
criar parcial de header

````
em base_templates/global criar pasta partials e arquivo _header.html
copiar header de base.html
em base.html fazer o include
{% include "global/partials/_header.html" %}
````
configurar pesquisa
````
criar view
criar url
passar a url no form search
import redirect
fazendo um filter, pelo valor digitado no search
import Q para poder pesquisar dois campos com filter usando "ou = | "
````
usando a classe Paginator para paginação no django

````
nas views: from django.core.paginator import Paginator
configurar a view index
configurar a view search
criar o partial _pagination.html
incluir o partial no base.html
````
criar CRUD

```` 
criar e configurar função criar um contato
em template contact criar create.html
extends global/cbase.html
block content
organizar aqrquivo html
csrf_token para proteger contra ataques csrf
````
em views criar contact_forms.py
from contact.forms import ContactForm
criar view create
em __init__.py ----> from .contact_forms.py import *

````
em urls.py criar a url para a view create
````
criar formulários em django

````
configurar o formulário em create.html
criar arquivo forms.py
from django import forms
from django.core.exceptions import ValidationError
criar a class ContactForm

````
configurar o formulário
````
em forms.py --->>> widgets
````
validando campos formulário
````
configurar método clean em forms.py
````
salvando o formulário e redirecionando o formulário
````
em contact_forms.py criar uma variável form
if form.is_valid():
````
criando as opções update e delete
````
em contact_forms.py 
from django.urls import reverse
configurar def create
criar a views update
import get_object_or_404
de contato models import Contact
criar a views para delete
````
em create.html
form action {{form_action}}, (para action passar a variável form_action)
````
em urls.py criar a url para update
criar a url para delete
````
em contact.html 
criar o link para update
criar form e botão para deletes
criar if para confirmar delete
````
exibindo imagem no contado e no update

````
em contact.html inserir imagem
````
em forms.py adicionar o campo picture e configura
````
em create.html criar um if para exibir a imagem
````
para que passe a ser atualizada a imagem
em contact_forms -- em TODOS os locais que tiver request.POST, passar, request.FILES
````
Criar novos usuários
````
em forms.py
from django.contrib.auth.forms import UserCreationForm
criar a class RegisterForm
from django.contrib.auth.models import User
criar a class Meta
criar o metodo clean_email para impedir que possa ser criado usuários com o mesmo email
configurar first_mname, last_name e email, para que sejam campos obrigatórios e que tenham um tamanho minimo
````
criar register.html
````
em views criar user_forms
criar uma view
from contact.forms import RegisterForm
````
em __init__.py ---> from .user_forms import *
````
em urls.py criar uma url para create user
````
enviando mensagens com django
````
em user_forms
import redirect
from django.contrib import messages
messages.tipo(request, 'um texto')
````
em partials
criar o arquivo messages.html
criar um if para checar as mensagens e um for para exibi-las
````
em base.html
fazer o include de _messages.html
````
em contact_forms
from django.contrib import messages
configurar mensagens para cada view
````

criando login e logout

````
em templates --> contact 
criar pasta partials e user-form.html
retirar o form de register.html --> permitirá que seja usado em outros locais
colar o form em user-form.html
fazer o include de user-form.html em register.html
````
duplicar a pasta de register.html com o nome de login
alterar o h2 para login
fazer um if para confirmar a autenticidade do usuário
````
em user_forms
importar AuthenticationForm
criar uma view para login
importar auth
na view auth.login()
criar umaview para logout
````
em urls.py
criar uma url para login
criar uma url para logout
````

criar formulário para atualizar usuários
´´´´
em forms.py
criar class RegisterUpdateForm
import password_validation
configurar campos, criar campos password, fazer validação de senha
criar uma verificação de email
criar método para alterar senha
criar método para verificação de senhas
criar método para salvar nova senha
````
em urls.py
criar uma url
````
em user_forms
criar uma view
importar RegisterUpdateForm
````
diferenciando usuário logado de não logado
````
em _header.html
criar um if para verificar se usuário está logado
criar os links para cada opção
````
em user_forms.py
import login_required
nos locaisa que precisar de usuário logado usar o decorator '@loginrequired'
````
em contact_forms.py
import login_required
nos locaisa que precisar de usuário logado usar o decorator '@loginrequired'
````
vinculando usuário aos contatos que ele criou
````
em contact_forms
em em def register -->>contact= form.save(commit=False) 
contact.owner = request.user
contact.save()
````
criar a página user_update
````
em templates criar arquivo user_update.html
````