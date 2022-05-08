from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home_page.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))
    if length < 6 or length > 14:
        length = 12

    the_password = ''
    for i in range(length):
        the_password += random.choice(characters)

    context = {
        'password': the_password,
    }
    return render(request, 'generator/password.html', context)
