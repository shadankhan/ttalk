# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	location = models.CharField(max_length=100)
	profile_pic = models.ImageField(upload_to="static/profile_pic")
	user = models.ForeignKey(User)

	def __str__(self):
		return self.user.username

class Post(models.Model):
	text = models.CharField(max_length=500)
	image = models.ImageField(upload_to="static/post_image", null=True, blank=True)
	pub_date = models.DateField(auto_now=False, auto_now_add=False)
	profile = models.ForeignKey("Profile")

	def __str__(self):
		return self.text