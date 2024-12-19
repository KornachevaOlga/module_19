from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator


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

class BlogPage:
    per_page = 3

    def get_page(self, request):
        posts = Post.objects.all().order_by('-created_at')
        if request.method == 'POST':
            if request.POST.get('page_len') == 'all':
                self.per_page = len(posts)
            else:
                self.per_page = int(request.POST.get('page_len'))
        paginator = Paginator(posts, self.per_page)
        try:
            page_number = int(request.GET.get('page'))
        except TypeError:
            page_number = 1
        page_obj = paginator.get_page(page_number)
        num_page_list = []
        if page_number - 2 > 1:
            num_page_list.append(0)
        for i in range(max(1, page_number - 2), min(paginator.num_pages, page_number + 2) + 1):
            num_page_list.append(i)
        if page_number + 2 < paginator.num_pages:
            num_page_list.append(0)
        context = {'page_obj': page_obj,
                   'paginator': paginator,
                   'num_page_list': num_page_list}
        return render(request, 'task2/news.html', context)
