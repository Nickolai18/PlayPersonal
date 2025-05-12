from django.shortcuts import render
from .models import Bid, Comment

def bid(request):
    if request.method == 'POST':
        bid_id = request.POST.get('bid_id')
        action = request.POST.get('action')
        
        if bid_id and action:
            bid = Bid.objects.get(id=bid_id)
            if action == 'approve':
                bid.status = 'approved'
            elif action == 'reject':
                bid.status = 'rejected'
            elif action == 'rate':
                bid.rating = int(request.POST.get('rating', 0))
            bid.save()
        
        if 'comment_text' in request.POST:
            Comment.objects.create(
                bid_id=bid_id,
                user=request.POST.get('user', 'Гость'),
                text=request.POST.get('comment_text')
            )
    
    bid = Bid.objects.all()
    return render(request, 'main/bid.html', {'bid': bid})
