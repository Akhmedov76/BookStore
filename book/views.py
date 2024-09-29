from django.shortcuts import render

from book.models import BookStoreModel


def home_page_view(request):
    bookspolis = BookStoreModel.objects.all()

    context = {
        'books': bookspolis,
    }
    return render(request, 'index.html', context)


def login_page_view(request):
    return render(request, 'login.html')


def register_page_view(request):
    return render(request, 'register.html')


def member_page_view(request):
    return render(request, 'member.html')


def error_page_view(request):
    return render(request, '404Error.html')
