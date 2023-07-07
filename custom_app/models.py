from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
    
    

class Author(BaseModel):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    place = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"
    

class Post(BaseModel):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    blog = models.CharField(max_length=240)

    def __str__(self):
        blog = self.blog[0:25]
        return f"{blog}"
    