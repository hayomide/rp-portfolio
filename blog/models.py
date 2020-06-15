from django.db import models

# creating the model Category 
class Category(models.Model):
    name = models.CharField(max_length=200)

#model post with various field and relationship field categories 
#linking model category to post such that we have many categoeires to one post line 14
class Post(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')  

#model Comment for comment sections 
#linking model coment to Post such that we have many comment to one post also on deleting a Post the commenrt is also deleted  in line 22
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)



# Create your models here.
