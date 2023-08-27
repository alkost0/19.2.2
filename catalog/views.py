from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    return render(request, 'catalog/index.html')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f'Новое сообщение от  {name}({number}, {email}): {message}')
    return render(request, 'catalog/contacts.html')
