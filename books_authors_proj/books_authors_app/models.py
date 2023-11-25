from django.db import models

class book(models.Model):
    title = models.CharField(max_length=70)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def show_all():
        return book.objects.all()
    
    def show(id):
        return book.objects.get(id=int(id))

    def create(title,desc):
        book.objects.create(
                title=title,
                desc=desc
                )

    def add_author(author1,bk):
        au = author.objects.get(id=author1)
        bk = book.objects.get(id=bk)
        bk.authors.add(au)

# ==========================================================================

class author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField()
    books = models.ManyToManyField(book,related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def show_all():
        return author.objects.all()
    
    def show(id):
        return author.objects.get(id=int(id))

    def create(fname,lname,notes):
        author.objects.create(
                first_name=fname,
                last_name=lname,
                notes = notes
                )

    def add_book(book1,au1):
        au = author.objects.get(id=au1)
        bk = book.objects.get(id=book1)
        au.books.add(bk)