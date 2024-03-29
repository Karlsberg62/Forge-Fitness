from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from allauth.account.views import SignupView
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, CommentReview, Sessions
from .forms import CommentForm, EditSettingsForm, AnonContactForm

# Create your views here.


def index(request):

    return render(request, 'index.html')


def our_clubs(request):

    return render(request, 'our_clubs.html')


def team(request):

    return render(request, 'team.html')


def contact_us(request):
    if request.method == 'POST':
        form = AnonContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Form Submitted'
            )
            # Redirect to a thank you page or display a success message
            return redirect('index')
    else:
        form = AnonContactForm()

    return render(request, 'contact_us.html', {'form': form})


@login_required
def profile(request):

    return render(request, 'profile.html')


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
            # If form valid, save comment.
            # Assign authed user & session object to comment
            comment = form.save(commit=False)
            comment.username = request.user
            comment.post = session_obj
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted'
            )
            # Redirect to session detail page after successfully adding comment
            return redirect('session-detail', slug=slug)
    else:
        # If the request method is not POST, render the empty comment form
        form = CommentForm()

    # Render add_comment.html template with the comment form and session object
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
                messages.add_message(
                    request, messages.SUCCESS,
                    'Comment edited'
                )
                # Redirect if successful, redirect elsewhere if not
                return redirect('session-detail', slug=comment.post.slug)
        else:
            form = CommentForm(instance=comment)
        # Render the edit_comment.html template
        return render(request, 'edit_comment.html', {'form': form, 'comment': comment})
    else:
        # If user is not owner of the comment, redirect to session detail page
        return redirect('session-detail', slug=comment.post.slug)


def delete_comment(request, comment_id):
    # Retrieve the comment object based on the provided comment ID
    comment = get_object_or_404(CommentReview, pk=comment_id)
    if request.user.is_authenticated and comment.username == request.user:
        # Check if the logged-in user is the owner of the comment
        session_slug = comment.post.slug
        # Delete the comment
        comment.delete()
        messages.add_message(
                    request, messages.SUCCESS,
                    'Comment deleted'
                )
        # Redirect if successful, redirect elsewhere if not
        return redirect('session-detail', slug=session_slug)
    else:
        return redirect('session-detail', slug=comment.post.slug)


class UserEditView(LoginRequiredMixin, generic.UpdateView):
    form_class = EditSettingsForm
    template_name = 'edit_settings.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            messages.add_message(
                    self.request, messages.SUCCESS,
                    'Settings edited'
                )
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class EditProfileView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    template_name = "edit_profile.html"
    fields = ['profile_pic', 'age', 'gender', 'phone', 'address', 'postcode']

    def get_success_url(self):
        return reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            messages.add_message(
                    self.request, messages.SUCCESS,
                    'Profile edited'
                )
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


@login_required
def delete_account(request):
    if request.method == 'POST':
        # Assuming the user and profile are related via OneToOneField
        user = request.user
        profile = user.profile

        # Delete the user and profile
        user.delete()
        profile.delete()

        # Redirect to a relevant page after deletion
        return redirect('index')  # Change 'home' to the desired URL name

    # If request method is not POST, render the template or handle accordingly
    return render(request, 'delete_account.html')
