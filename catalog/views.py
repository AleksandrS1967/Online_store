from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        textarea = request.POST.get('textarea')
        print(f'Вывод запросов: {email}: {textarea}')
    return render(request, 'catalog/contacts.html')
