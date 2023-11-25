from django.db import models

class show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=45)
    release_date=models.DateField()
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def create(title,network,release_date,desc):
        show.objects.create(
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