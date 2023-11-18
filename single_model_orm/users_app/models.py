from django.db import models

class users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=45)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<users object: {self.first_name} ({self.last_name})>"

    def create_user(first_name,last_name,email_address,age):
        users.objects.create(
        first_name=first_name,
        last_name=last_name,
        email_address=email_address,
        age=age
        )

    def show_all(self):
        return users.objects.all()