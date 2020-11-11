# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ttalk_app.models import Profile
from django.shortcuts import render, redirect, render_to_response

# Create your views here.

def index(request):
  if request.method == 'POST' and request.FILES.iteritems():

    text = request.POST.get('text','')
    image = request.FILES['image']

    post, created = Post.objects.get_or_create(
        profile = request.user.profile_set.get(),
        text = text,
        image = image,

      )
    return render('index')
  else:
    return render(request, 'index.html')

def create_profile(request): 
    #context = RequestContext(request)
    if request.method == 'POST' and request.FILES.iteritems():

        profile_pic = request.FILES['profile_pic']
        location = request.POST.get('location','')

        profile,created = Profile.objects.get_or_create(
                  user = request.user,
                  profile_pic = profile_pic,
                  location = location,

                )

        return render('index')       
    else:
        return render(request, 'create_profile.html')

