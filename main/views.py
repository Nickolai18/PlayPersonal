from django.shortcuts import render

from main.models import Bid

def main(request):
  bid = Bid.objects.all()

  context = {
    "bid": bid,
  }
  # ex = {
  #   "ex":"Ghjdthrf hf,jns",
  # }
  return render(request, 'main/index.html', context)

def bid(request):

  bid = Bid.objects.all()

  context = {
    "bid": bid,
  }

  return render(request, 'main/bid.html', context)
# Create your views here.
