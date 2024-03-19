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

def edit_comment(request, comment_id):
    comment = get_object_or_404(CommentReview, pk=comment_id)
    if request.user.is_authenticated and comment.username == request.user:
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('session-detail', slug=comment.post.slug)
        else:
            form = CommentForm(instance=comment)
        return render(request, 'edit_comment.html', {'form': form, 'comment': comment})
    else:
        return redirect('session-detail', slug=comment.post.slug)

def delete_comment(request, comment_id):
    comment = get_object_or_404(CommentReview, pk=comment_id)
    if request.user.is_authenticated and comment.username == request.user:
        session_slug = comment.post.slug
        comment.delete()
        return redirect('session-detail', slug=session_slug)
    else:
        return redirect('session-detail', slug=comment.post.slug)
