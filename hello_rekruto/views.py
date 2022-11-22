from django.shortcuts import render


def index(request):
    name = request.GET.get('name', '')
    message = request.GET.get('message', '')
    return render(request, 'index.html', {'name': name, 'message': message})
