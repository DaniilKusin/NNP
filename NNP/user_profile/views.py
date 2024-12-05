from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomRegistrationForm, CustomLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def register(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomRegistrationForm()

    return render(request, 'user_profile/register.html', {'form': form})


class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'user_profile/login.html'

    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            return 'profile'
        return super().get_redirect_url()


@login_required
def profile(request):
    user = request.user
    return render(request, 'user_profile/profile.html', {
        'user': user,
    })