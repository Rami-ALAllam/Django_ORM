from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    Desc = models.TextField(default = "old_dojo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def show_all(self):
        return Dojo.objects.all()
    
    def create_dojo(name,city,state):
        Dojo.objects.create(
        name=name,
        city=city,
        state=state
        )
    
    def delete_dojo(dojodel):
        d1 = Dojo.objects.get(id=dojodel)
        d1.delete()

class Ninja(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    dojo = models.ForeignKey(Dojo, related_name= "ninjas", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def show_all(self):
        return Ninja.objects.all()

    def create_ninja(fname,lname,dojo):
        Ninja.objects.create(
        first_name=fname,
        last_name=lname,
        dojo=Dojo.objects.get(id=dojo)
        )
