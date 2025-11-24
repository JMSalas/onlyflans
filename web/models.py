from django.db import models
from django.contrib import auth
import uuid

# Create your models here.

class Flan(models.Model):
    flan_uuid = models.UUIDField(primary_key = True)
    name = models.CharField(max_length = 64, blank = False)
    description = models.TextField(blank = False)
    precio = models.IntegerField(blank = False)
    image_url = models.URLField(blank = False)
    slug = models.SlugField()
    is_private = models.BooleanField(blank = False)

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(editable = False, default = uuid.uuid4, primary_key = True)
    customer_email = models.EmailField(blank = False)
    customer_name = models.CharField(max_length = 64, blank = False)
    message = models.TextField(blank = False)

class Favoritos(models.Model):
    id = models.AutoField(primary_key=True)
    id_flan = models.ForeignKey(Flan, on_delete=models.CASCADE)
    id_user = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_flan', 'id_user'], name='unique_flan_user')
        ]

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    mensaje = models.TextField(blank = False)
    calificacion = models.IntegerField(blank = False)
    date_created = models.DateTimeField(auto_now_add=True)
    id_flan = models.ForeignKey(Flan, on_delete=models.CASCADE)
    id_user = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)