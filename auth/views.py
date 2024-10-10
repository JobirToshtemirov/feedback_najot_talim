from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.http import urlsafe_base64_encode
from auth.form import RegisterForm
from auth.token import TokenGenerator


# Create your views here.


def send_email(request, user):
    # Send email to user
    token = TokenGenerator.make_token(user)
    uid = urlsafe_base64_encode(user.pk)
    current = get_current_site(request)
    verification_url = reverse('auth_fur:verify_email', kwargs={'uidb64': uid, 'token': token})
    full_url = f"http://{current.site.domain}{verification_url}"

    text_content = render_to_string(
        'register/verify_email.html',
        {'user': user, 'full_url': full_url},

    )

    message = EmailMultiAlternatives(
        subject="Verify your email address",
        body=text_content,
        to=[user.email],
        from_email=[EMAIL_HOST_USER]
    )

    message.attach_alternative(text_content, 'text/html')
    message.send()


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False
            user.save()
            send_email(request, user)
            return redirect(reverse_lazy('auth:login'))
        else:
            errors = form.errors
            return render(request, 'register.html', {"form": form, "errors": errors})
    else:
        form = RegisterForm()
        return render(request, 'register.html', {"form": form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            auth_login(request, user)
            # Redirect to a success page
            return redirect('dashboard')  # Replace 'dashboard' with your desired URL name
        else:
            # Invalid login details
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
