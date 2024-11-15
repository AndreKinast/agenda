from django.db import models
from django.utils import timezone

#ID (primary key)
# first_name (string), last_name(string), phone(string)
#email (email), created_date(date), description(text)
#category(foreing key), show(boolean), owner(foreing key)
#picture(imagem)


#os campos de texto normalmente são obrigatórios, para que não seja é preciso adicionar 'blank=true'
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
