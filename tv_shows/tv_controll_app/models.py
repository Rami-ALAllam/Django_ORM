from django.db import models
import datetime
from datetime import datetime

class showManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if len(postData['desc']) < 10 and len(postData['desc']) > 0 :
            errors["desc"] = "Show description should be at least 10 characters"
        if datetime.today() < datetime.strptime(postData['release_date'],'%Y-%m-%d'):
            errors["release_date"] = "Show release date should be in the past"
        for shows in show.objects.all():
            if shows.title == postData['title']:
                errors["title"] = "Show name must be unique"
        return errors

class show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=45)
    release_date=models.DateField()
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects= showManager()

    def create(title,network,release_date,desc):
        return show.objects.create(
            title=title,
            network=network,
            release_date=release_date,
            desc=desc
        )
    def show_all():
        return show.objects.all()

    def show_id(id):
        return show.objects.get(id=int(id))
    
    def show_delete(id):
        showdel= show.objects.get(id=int(id))
        showdel.delete()

    def update(editshow_id,title,network,release_date,desc):
        show_update=show.objects.get(id=int(editshow_id))
        show_update.title=title
        show_update.network=network
        show_update.release_date=release_date
        show_update.desc=desc
        show_update.save()
        