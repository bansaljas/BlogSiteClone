from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    publish_date=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('post_detail',kwargs={'pk':self.pk})

    def publish(self):
        self.publish_date=timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approve_comment=True)


class Comment(models.Model):
    post=models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    approve_comment=models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def approve(self):
        self.approve_comment=True
        self.save()

    def get_absolute_url(self):
        return render('post_list')
