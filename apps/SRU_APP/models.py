from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
# app.secret_key = 'This is not a secret key'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, post_data):
        errors = []
        if User.objects.filter(email=post_data['email']):
        # checks to see if email in database. If there are more than 1 email returned there is a duplicate and sends errors
            errors.append('email is already in database')
         # captures error messages
        if len(post_data['fname'])<0: 
            errors.append('first name fields needs to be at least 0 characters!')
        elif not post_data['fname'].isalpha():
            errors.append('alphabetic characters only. In this case the numbers are not allowed')
            # First Name - Required; No fewer than 2 characters; letters only
        if len(post_data['lname'])<0:
            errors.append('last name field needs to be at least 0 characters!')
        elif not post_data['lname'].isalpha():
            errors.append('alphabetic characters only. In this case the numbers are not allowed')
            # Last Name - Required; No fewer than 2 characters; letters only
        if len(post_data['email']) == 0:
            errors.append('email field is required')
        elif not EMAIL_REGEX.match(post_data['email']):
            errors.append("Invalid email")
            # Email - Required; Valid Format
        # if len(post_data['password'])< 8:
        #     errors.append('invalid - password is less than 8 characters')
        # elif post_data['password']!= post_data['cpassword']:
        #     errors.append('email fields do not match. please try again')
            # Password - Required; No fewer than 8 characters in length; matches Password Confirmation
        if not errors:
            new_user = User.objects.create (
                fname = post_data['fname'],
                lname = post_data['lname'],
                email = post_data['email'],
            )
            return new_user
        return errors
class User(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

