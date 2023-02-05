import email
import json

from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render, redirect
from web.models import Customers, Subscriber
from django.http.response import HttpResponse
from django.urls import reverse

def index(request):
    customers = Customers.objects.all()

    print(customers)

    context = {
        "customers" : customers,
    }

    return render(request, "index.html", context=context)


def subscriber(request):
    email = request.POST.get("email")

    if not Subscriber.objects.filter(email=email).exists():


        Subscriber.objects.create(
            email = email
        )

        response_data = {
            "status" : "success",
            "title" : "Subscribe Successfully",
            "message" : "You subscribed to our newsletter successfully"
        }

    else:
        response_data = {
            "status" : "erro",
            "title" : "You are already exist ",
            "message" : "You are already a member"
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")
    