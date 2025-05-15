from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse

from main.models import Bid
from main.models import Games

from main.forms import UserLoginForm


def main(request):
  if request.method == 'POST':
    form = UserLoginForm(data=request.POST)
    if form.is_valid():
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username, password=password)
      if user:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('main'))
  else:
    form = UserLoginForm()

  card = Games.objects.all()

  content = {
    "card": card,
    "form": form
  }

  return render(request, 'main/index.html', content)

def bid(request):

  bid = Bid.objects.all()

  context = {
    "bid": bid,
  }

  return render(request, 'main/bid.html', context)
def users(request):
  return render(request, 'main/users-control.html')
def product(request, product_id):

  game = Games.objects.get(id=product_id)

  context = {
    "game": game,
  }

  return render(request, 'main/product.html', context)
  

# Create your views here.
