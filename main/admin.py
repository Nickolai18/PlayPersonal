from django.contrib import admin
from .models import Bid, Comment

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'status', 'rating')
    list_editable = ('status', 'rating')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'bid', 'user', 'created_at')
