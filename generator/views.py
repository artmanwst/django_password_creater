from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request,'generator/home.html',)
def password(request):
    import random
    import string
    Characters=list(string.ascii_lowercase)
    CHAR1=list(string.ascii_uppercase)
    length=int(request.GET.get('length',10))
    if request.GET.get('uppercase'):
        Characters+=CHAR1
    if request.GET.get('special'):
        Characters+=list('@!#$%^&*()_?><":}{[]')
    if request.GET.get('numbers'):
        Characters+=list('1234567890')
    password=""
    for i in range(length):
        password+=random.choice(Characters)
    return render(request,'generator/password.html',{'password':password})
def opis(request):
    return render(request,'generator/opis.html')