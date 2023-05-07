from django.shortcuts import render

def index(request):
    return render(
        request,
        "index.html",
        {
            "title": "Django example",
        },
    )



def home(request):
    return render(
        request,
        "dashboard/home.html",
        {
            "title": "home",
        },
    )


def login(request):
    return render(
        request,
        "dashboard/login.html",
        {
            "title": "login",
        },
    )