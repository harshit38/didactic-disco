from django.shortcuts import render

def index(request):
    return render(
        request,
        "dashboard/home.html",
        {
            "title": "Study portal",
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


def logout(request):
    return render(
        request,
        "dashboard/logout.html",
        {
            "title": "logout",
        },
    )


def youtube(request):
    return render(
        request,
        "dashboard/youtube.html",
        {
            "title": "logout",
        },
    )

def notes(request):
    return render(request, "dashboard/notes.html")