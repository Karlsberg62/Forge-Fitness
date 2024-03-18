from django.shortcuts import render
from django.views import generic
from .models import Profile, CommentReview, Sessions

# Create your views here.
def index(request):
    return render(request,'index.html')

def profile(request):
    return render(request,'profile.html')

class SessionList(generic.ListView):
    model = Sessions
    template_name = 'classes.html'
    paginate_by = 6

class SessionDetail(generic.DetailView):
    model = Sessions
    template_name = 'classes_details.html'