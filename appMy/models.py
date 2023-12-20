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
   # null değerlere None değer gönderir
   # default başlangıç değeri gönder
   # blank doldurulması zorunlu değil
   subtitle = models.CharField(("Alt Başlık"), max_length=50, null=True, blank=True)
   isactive = models.BooleanField(("Sayfada Göster"), default=False)
   
   
class Deneme(models.Model):
   baslik = models.CharField(("Başlık Deneme"), max_length=50)
   
class Contact(models.Model):
   fullname = models.CharField(("Ad Soyad"), max_length=50)
   title = models.CharField(("Konu"), max_length=50)
   email = models.EmailField(("Email"), max_length=254)
   text = models.TextField(("İletişim Mesajı"))