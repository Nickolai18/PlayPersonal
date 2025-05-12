from django.shortcuts import render, redirect
from .models import Bid, Comment

def main(request):
    bid = Bid.objects.all()
    context = {"bid": bid}
    return render(request, 'main/index.html', context)

def bid(request):
    if request.method == 'POST':
        # Обработка действий с кнопками
        bid_id = request.POST.get('bid_id')
        action = request.POST.get('action')
        
        if bid_id and action:
            bid = Bid.objects.get(id=bid_id)
            if action == 'approve':
                bid.status = 'approved'
            elif action == 'reject':
                bid.status = 'rejected'
            elif action == 'rate':
                bid.rating = request.POST.get('rating', 0)
            bid.save()
        
        # Обработка комментариев
        if 'comment_text' in request.POST:
            Comment.objects.create(
                bid_id=bid_id,
                user=request.user.username if request.user.is_authenticated else 'Гость',
                text=request.POST.get('comment_text')
            )
    
    bid = Bid.objects.all()
    context = {"bid": bid}
    return render(request, 'main/bid.html', context)
