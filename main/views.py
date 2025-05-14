from django.shortcuts import render

from main.models import Bid
from main.models import Games


def main(request):

  card = Games.objects.all()

  content = {
    "card": card
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
