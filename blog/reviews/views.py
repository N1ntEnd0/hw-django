from django.http import HttpResponse
from .models import Review
from django.shortcuts import render

MENU = {"Лента": "/", "О блоге": "/about", "Книга отзывов": "/review"}


def reviews_page(request):
    fullName = request.POST.get('fullName')
    email = request.POST.get('email')
    text = request.POST.get('text')

    print(fullName, email, text)
    if fullName and email and text:
        Review.objects.create(fullName=fullName, email=email, text=text)

    reviews = Review.objects.filter(checked=True).order_by('-id')
    data = {"menu": MENU, "reviews": reviews}
    return render(request, './reviews.html', context=data)
