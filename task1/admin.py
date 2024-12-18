from django.contrib import admin
from .models import Buyer, Game

# Register your models here.
class BuyerAdmin(admin.ModelAdmin):
    # Ограничение количества записей на странице
    list_per_page = 20

    # Поля, которые будут отображаться в списке
    list_display = ('title', 'cost', 'size')

    # Поля, по которым будет доступна фильтрация
    list_filter = ('size', 'cost')

    # Поле, по которому будет доступен поиск
    search_fields = ('title',)


# Регистрация модели Buyer с админ-классом BuyerAdmin
admin.site.register(Game, BuyerAdmin)


class GameAdmin(admin.ModelAdmin):
    # Ограничение количества записей на странице
    list_per_page = 30

    # Поля, которые будут отображаться в списке
    list_display = ('name', 'balance', 'age')

    # Поля, по которым будет доступна фильтрация
    list_filter = ('balance', 'age')

    # Поле, по которому будет доступен поиск
    search_fields = ('name',)

    # Делаем поле balance доступным только для чтения
    readonly_fields = ('balance',)


# Регистрация модели Game с админ-классом GameAdmin
admin.site.register(Game, GameAdmin)


