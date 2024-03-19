from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from .models import Profile, CommentReview, Sessions
from .forms import CommentForm, EditProfileForm

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
    # Retrieve the session object corresponding to the provided slug
    session_obj = get_object_or_404(Sessions, slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the comment. Assign the authed user & session object to the comment
            comment = form.save(commit=False)
            comment.username = request.user 
            comment.post = session_obj  
            comment.save()
            # Redirect to the session detail page after successfully adding the comment
            return redirect('session-detail', slug=slug)
    else:
        # If the request method is not POST, render the empty comment form
        form = CommentForm()
    
    # Render the add_comment.html template with the comment form and session object
    return render(request, 'add_comment.html', {'form': form, 'session_obj': session_obj})

def edit_comment(request, comment_id):
    # Retrieve the comment object based on the provided comment ID
    comment = get_object_or_404(CommentReview, pk=comment_id)
    if request.user.is_authenticated and comment.username == request.user:
        # Check if user is the owner of the comment
        if request.method == 'POST':
            # If request method is POST, process the form. If it's valid, save.
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                # Redirect if successful, redirect elsewhere if not 
                return redirect('session-detail', slug=comment.post.slug)
        else:
            form = CommentForm(instance=comment)
        # Render the edit_comment.html template
        return render(request, 'edit_comment.html', {'form': form, 'comment': comment})
    else:
        # If user is not the owner of the comment, redirect to the session detail page
        return redirect('session-detail', slug=comment.post.slug)

def delete_comment(request, comment_id):
    # Retrieve the comment object based on the provided comment ID
    comment = get_object_or_404(CommentReview, pk=comment_id)
    if request.user.is_authenticated and comment.username == request.user:
        # Check if the logged-in user is the owner of the comment
        session_slug = comment.post.slug
        # Delete the comment
        comment.delete()
        # Redirect if successful, redirect elsewhere if not 
        return redirect('session-detail', slug=session_slug)
    else:
        return redirect('session-detail', slug=comment.post.slug)

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user