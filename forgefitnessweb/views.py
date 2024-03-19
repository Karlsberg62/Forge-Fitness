from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Profile, CommentReview, Sessions
from .forms import CommentForm

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

def add_comment(request, slug):
    session_obj = get_object_or_404(Sessions, slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.username = request.user  # Assuming the user is authenticated
            comment.post = session_obj
            comment.save()
            return redirect('session-detail', slug=slug)  # Redirect to session detail page
    else:
        form = CommentForm()
    
    return render(request, 'add_comment.html', {'form': form, 'session_obj': session_obj})