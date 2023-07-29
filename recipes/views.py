from django.shortcuts import render


# Create your views here.
def home(request):
    return render(
        request, "recipes/Pages/home.html", context={"name": "Allan Ribeiro da Silva"}
    )
