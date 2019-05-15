from django.db import models
from django.contrib.auth.models import User
import datetime


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to="images/")
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now())
    location = models.CharField(max_length=200)
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%d %B %Y')

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title
