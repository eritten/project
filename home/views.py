from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.



def home(request):
    return render(request, 'home.html')

@api_view(["POST"])
def email(request):
    name = request.data.get("name")
    email = request.data.get("email")
    age = request.data.get("age")
    date = request.data.get("date")
    tel = request.data.get("tel")
    country = request.data.get("country")
    send_mail()
    return Response({"status": "ok"})
