from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from .forms import ProfileForm


@login_required
def profile(request):
    '''展示个人资料'''
    user = request.user
    return render(request, 'users/profile.html', {'user':user})


@login_required
def change_profile(request):
    '''更新个人资料'''
    if request.method == 'POST':
        # instance参数表示用model实例来初始化表单，这样就可以达到通过表单来更新数据
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # 添加一条信息，表单验证成功就重定向到个人信息页面
            messages.add_message(request, messages.SUCCESS, '个人信息更新成功！')
            return redirect('users:profile')
    else:
        # 不是POST请求就返回空表单
        form = ProfileForm(instance=request.user)
    return render(request, 'users/change_profile.html', context={'form': form})