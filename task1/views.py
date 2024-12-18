from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def game_platform(request):
    return render(request, 'task2/platform.html')

def game(request):
    game_dict = {
        "games": [
            {
                "title": "Atomic Heart",
                "description": "Atomic Heart is a first-person shooter set in an alternate universe during the height of the Soviet Union. Players explore a world filled with mutated creatures and advanced technology.",
                "price": 59.99  # стоимость в долларах
            },
            {
                "title": "Cyberpunk 2077",
                "description": "Cyberpunk 2077 is an open-world RPG set in a dystopian future where players assume the role of V, a mercenary navigating the neon-lit streets of Night City.",
                "price": 49.99  # стоимость в долларах
            }
        ]
    }
    context = {'game_dict': game_dict}
    return render(request, 'task2/games.html', context)

def cart(request):
    return render(request, 'task2/cart.html')


def sign_up(request):
    buyers = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password == repeat_password and int(age) >= 18 and username not in str(buyers):
            Buyer.objects.create(name=username, balance=200.0, age=age)
            return HttpResponse(f'Добро пожаловать {username}!')
        elif password != repeat_password:
            info['error'] = 'Пароли не совподают!'

        elif int(age) < 18:
            info['error'] = 'Вам не 18 лет!'

        elif username in str(buyers):
            info['error'] = 'Такой логин уже зарегистрирован!'

    return render(request, 'task1/registration_page.html', context=info)


