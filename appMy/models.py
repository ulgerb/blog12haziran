from django.db import models

# Model tablosu oluşturmak için
# python manage.py makemigrations
# python manage.py migrate
# SQL DATABASE içerisine Tablo oluşturur


class Blog(models.Model):
   title = models.CharField(("Başlık"), max_length=150) # html input text
   text = models.TextField( verbose_name="İçerik" ) # html textarea
   date_now = models.DateTimeField(("Tarih - Saat"), auto_now=False, auto_now_add=False)
   author = models.CharField(("Yazar"), max_length=50)
   
class Deneme(models.Model):
   baslik = models.CharField(("Başlık Deneme"), max_length=50)