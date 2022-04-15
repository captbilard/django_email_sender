from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail(
        "Test mail",
        "This is a test mail",
        "from@example.com",
        ["to@example.com",],
        fail_silently=True
    )
    return HttpResponse("<h2> Email Sent </h2>")