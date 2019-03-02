from django.shortcuts import render
from .models import Comment

def index(request):
    comments = Comment.objects.order_by('-data added')
    contect = {
        'comments' : comments
    }
    return render(request, 'guestbook/index.html', context)
# Create your views here.
