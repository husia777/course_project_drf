from django.db import models


class Ad(models.Model):
    image = models.ImageField(upload_to='logos/ad/', null=True)
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    ad = models.ForeignKey('Ad', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
