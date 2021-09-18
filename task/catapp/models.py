from django.db import models

# Create your models here.
Breed = [
    ('Billy','Billy'),
    ('Persian Cats','Persian Cats'),
    ('American Curl Cats','American Curl Cats'),
    ('Mumbai Cats','Mumbai Cats'),
    ('Munchkin Cats','Munchkin Cats')
]

class Catmodel(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(null=True,blank=True,max_length=50)
    cat_breed = models.CharField(choices=Breed,max_length=50,null=True)
    cat_desc = models.TextField(null=True,blank=True)
    cat_image = models.ImageField(upload_to='static/images/')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.cat_name:
            return self.cat_name
        else:
            return "No name"
