from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth
from django.urls import reverse

from main.models import Bid
from main.models import Games

from main.forms import AddGames, UserLoginForm, UserRegistrationForm


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

  if request.method == 'POST':
    formS = UserRegistrationForm(data=request.POST)
    if formS.is_valid():
      formS.save()
      return HttpResponseRedirect(reverse('main'))
  else:
    formS = UserRegistrationForm()

  card = Games.objects.all()

  content = {
    "card": card,
    "form": form,
    "formS": formS
  }

  return render(request, 'main/index.html', content)

def logout(request):
  auth.logout(request)
  return redirect(reverse('main'))

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
  
def addgames(request):

  if request.method == 'POST':
    game = AddGames(data=request.POST, files=request.FILES)
    if game.is_valid():
      game.save()
      return HttpResponseRedirect(reverse('main'))
  else:
    game = UserRegistrationForm()

  context = {
    "game": game,
  }

  return render(request, 'main/addgames.html', context)
# Create your views here.
