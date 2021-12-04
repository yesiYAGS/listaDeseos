from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
import re

class UserManager(models.Manager):

    def basic_validator(self, postData):
        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData['name']) < 3:
            errors["name"] = "First name should be at least 5 characters"
        if len(postData['username']) < 3:
            errors["username"] = "Last name should be at least 5 characters"
        # validate_email(postData['email'])
        
        try:
            validate_email(postData['email'])
        except ValidationError:
            print('VALIDATION ERROR')
            errors["email"] = "please enter a valid email"
        # if EmailValidator(postData['email']):
        #     errors["first_name"] = "First name should be at least 5 characters"
        if postData['password'] != postData['confirmed_pw']:
            errors["password"] = "Passwords must be the same"
        return errors

class User(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=255)
    created_at = models.TimeField(auto_now=True)
    updated_at =  models.TimeField(auto_now=True)

class List(models.Model):
    Item = models.CharField(max_length=30)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    favorites = favorites = models.ManyToManyField(User, related_name="favorite_product")
    created_at = models.TimeField(auto_now=True)
    updated_at =  models.TimeField(auto_now=True)