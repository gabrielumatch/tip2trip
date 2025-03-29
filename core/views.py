from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from posts.models import Post

# Create your views here.

class LandingPageView(TemplateView):
    template_name = 'core/landing.html'

class CustomLoginView(LoginView):
    template_name = 'core/auth/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('core:feed')  # Updated to use namespaced URL

class RegisterView(CreateView):
    template_name = 'core/auth/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('core:feed')  # Updated to use namespaced URL
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # Log the user in after registration
        return response
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:feed')  # Updated to use namespaced URL
        return super().dispatch(request, *args, **kwargs)

class FeedView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard/feed.html'
    login_url = 'core:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.select_related('author').prefetch_related('likes', 'comments').all()
        return context
