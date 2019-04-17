from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, ProfileForm
from django.views.decorators.http import require_POST
from django.contrib.auth import update_session_auth_hash

############################ signup ################################

    
def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
      
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) 				# 1 ?? 
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
    
########################### login ####################################
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'posts:list') # 해당 코드 수정
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)
    
    
    
############logout ####################


def logout(request):
    auth_logout(request)
    return redirect('posts:list')
    
### 20190417 수요일 진도 ###################

#################### profile my page ################
def people(request, username):
    people = get_object_or_404(get_user_model(), username=username)
    context = {'people': people,}
    return render(request, 'accounts/people.html', context)


###### 회원정보 수정 및 탈퇴 ###############3
@login_required
def update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user = user_change_form.save()
            return redirect('people')
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)

    context = {'user_change_form': user_change_form}
    return render(request, 'accounts/update.html', context)


@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
    return redirect('posts:list')

    
############################# 비밀번호 변경 #########################
@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('posts:list')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/password.html', context)




###### profile
@login_required
def profile_update(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('people', request.user.username)
    else:
        profile_form = ProfileForm(instance=request.user.profile) # 유저의 프로필을 수정
    context = {'profile_form': profile_form,}
    
    return render(request,'accounts/profile_update.html', context)