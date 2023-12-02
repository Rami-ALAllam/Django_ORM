from django.db import models
import datetime
from datetime import datetime
import re

class userManager(models.Manager):
    def validator(self,postData):
        errors={}
        if len(postData['fname']) < 2:
            errors["fname"] = "first name should be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "last name should be at least 2 characters"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email Address"
        if len(user.objects.filter(email = postData['email'])) > 0:
            errors["email"] = "Email address must be unique"

        if postData['bdate'] == "":
            errors["bdate"] = "Birth date is mandatory"
        else:
            bdate = datetime.strptime(postData['bdate'],'%Y-%m-%d')
            date_num1 = datetime.today().year
            date_num2 = bdate.year
            if datetime.today() < bdate:
                errors["bdate"] = "Birth date should be in the past"
            elif (date_num1 - date_num2) < 13:
                errors["bdate"] = "Age should be 13 years old at least"

        if len(postData['pass']) < 8:
            errors["password"] = "password should be at least 8 charcters"
        if postData["con-pass"] != postData['pass']:
            errors["password"] = "Password should be the same"
        return errors

class user(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.CharField(max_length=70)
    birth_date=models.DateField()
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=userManager()

    def create(first,last,email,birth,pwd):
        return user.objects.create(
        first_name=first,
        last_name=last,
        email=email,
        birth_date=birth,
        password=pwd
        )