from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile

# Django Views for Login
@login_required
def dashboard(req):
    return render(req, 
                  'registration/dashboard.html',
                  {'section':dashboard})

@login_required
def edit_user_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(
            instance=request.user, 
            data=request.POST
        )

        profile_form = ProfileEditForm(
            instance=request.user,
            data=request.POST
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit-profile.html', { 'user_form':user_form,'profile_form':profile_form })



def User_Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User = authenticate(
                username = cd['username'],
                password = cd['password']
            )
            if User is not None:
                if User.is_active:
                    login(request, User)
                    return HttpResponse('Yey, Welcome to the login!')
                else:
                    return HttpResponse("Sorry, your account is disabled")
            else:
                return HttpResponse("Sorry Invalid Input")
            
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
           
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #Create a new user without saving yet
            new_user = user_form.save(commit=False)

            #Set Pwd to User
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            #Save and Add User
            new_user.save()
            #Auto Create User
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user':new_user})
        
    else:
        user_form = UserRegistrationForm()

    return render(request, 'account/register.html', {'user_form': user_form})
        











