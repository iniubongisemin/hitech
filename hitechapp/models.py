from django.db import models

# Create your models here.
class BlogPost(models.Model): # models is the file, Model is the class
    title = models.CharField(max_length=200, verbose_name='blog title', unique=True, null=False, blank=True)
    description = models.CharField(max_length=500)
    content = models.TextField() # allows unlimited number of text
    posted_at = models.DateTimeField(auto_now=True) #12 March, 2024 12:00PM
    update_at = models.DateTimeField(auto_now=True)
    view_count = models.PositiveBigIntegerField()  
    # view_count = models.IntegerField()  

    class Meta: # to specify a special database name for some feature
        db_table = 'post' # name in your database NB: checkout django docs for more info
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = [-1] # this reverts the order
        ordering = ['post_at'] # order by date
        ordering = ['-post_at'] # reverts the order by date

