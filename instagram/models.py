from django.db import models

from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.


class Image(models.Model):
  photo = CloudinaryField('image')
  photo_name = models.CharField(max_length=60)
  posted_at = models.DateTimeField(auto_now_add=True)
  photo_caption = models.TextField()
  user = models.ForeignKey(User,on_delete = models.CASCADE)

  def save_photo(self):
     self.save()

  

