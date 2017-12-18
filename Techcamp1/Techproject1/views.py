from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .models import Registration
# Create your views here.


def index(request):

    if request.method == 'POST':
        Fullname = request.POST.get('Fullname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        email1 = request.POST.get('email1')

        Registration_obj = Registration(Fullname = Fullname, email = email, contact = contact)
        Registration_obj.save()



        return render(request,'Techproject1/thanks.html')

    return render(request,'Techproject1/index.html')
