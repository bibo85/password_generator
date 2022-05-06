from django.shortcuts import render


def home(request):
    return render(request, 'generator/home_page.html')


def password(request):
    password = 'asdf87asdf0u'
    context = {
        'password': password,
    }
    return render(request, 'generator/password.html', context)
