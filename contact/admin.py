from django.contrib import admin
from contact import models


# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    #colunas da página admin
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show',
    ordering = '-id', #ordena os contados pelo id em ordem crescente, com '-id terá uma ordem decrescente
    #list_filter, permite filtrar os resultados
    #campo pelos quais posso pesquisar
    search_fields = 'id', 'first_name', 'last_name',
    #quantos contatos "mostra" por página
    list_per_page = 10
    #valores que podem ser editados
    list_editable = 'first_name', 'last_name', 'show',
    #valor se torna um link
    list_display_links = 'id', 'phone',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    #colunas da página admin
    list_display = 'name', 
    ordering = 'id', #ordena os contados pelo id em ordem crescente, com '-id terá uma ordem decrescente
   