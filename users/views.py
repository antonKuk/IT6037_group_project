from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .form_registration import UserRegistrationForm

''' Register User'''

def register(request):
     if request.method=="POST":
          form=UserRegistrationForm(request.POST)
          if form.is_valid():
               form.save()
               username=form.cleaned_data.get('username')
               messages.success(request,f'{username} Account created successfully!!')
               return redirect('/')
         
     else:

          form=UserRegistrationForm()
     return render(request,'registration.html',{'form':form})

