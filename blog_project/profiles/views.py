from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import UpdateUser
from .profiles import UpdateProfile
from django.contrib import messages

@login_required
def profiles(request):
    if request.method == 'POST':
        u_form = UpdateUser(request.POST, instance=request.user)
        p_form = UpdateProfile(request.POST, request.FILES, instance=request.user.profiles)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Updated Successfully')
            return redirect('profile')
    else:
        u_form = UpdateUser(instance=request.user)
        p_form = UpdateProfile(instance=request.user.profiles)
        
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'profiles/profile.html', context)
