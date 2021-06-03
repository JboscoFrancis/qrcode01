from django.shortcuts import render
from .models import Webqrcode
# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        about = request.POST['about']
        phone = request.POST['phone']
        query,created = Webqrcode.objects.get_or_create(name=name, about=about, phone=phone)
        return render(request, 'qr/home.html', {'query':query})
    return render(request, 'qr/home.html')