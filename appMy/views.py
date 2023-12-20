from django.shortcuts import render
from appMy.models import *
# Create your views here.


def indexPage(request):
   blog_list = Blog.objects.all()
   
   context = {
      "blog_list":blog_list,
   }
   return render( request, 'index.html', context)

def categoryPage(request):
   blog_list = Blog.objects.all()
   
   context = {
      "blog_list":blog_list,
   }
   return render(request, 'category.html', context)
   
def aboutPage(request):
   blog_list = Blog.objects.all() # [1.blog, 2.blog, 3.blog]
   blog_isactive = Blog.objects.filter(isactive=True) # []
   blog2 = Blog.objects.get(id=2) # 2.obje not: eğer çekilen blog yoksa hata verir
   
   context = {
      "blog_list":blog_list,
      "blog_isactive":blog_isactive,
      "blog2":blog2,
   }
   return render(request, 'about.html', context)

def contactPage(request):

   if request.method == "POST":
      fname = request.POST.get("fullname")
      title = request.POST.get("title")
      email = request.POST.get("email")
      text = request.POST.get("text")
      
      contact = Contact(fullname=fname, title=title, email=email, text=text) # obje oluşturuldu değişkene gönderildi
      contact.save() # değişken kaydedildi
      
   context = {}
   return render(request, 'contact.html', context)


def detailPage(request, bid):
   # Kullanıcı yada Frontend'den bilgi alabilmenin 2 yöntemi vardır
   # 1) url adresinden
   # 2) Formlardan
   blog = Blog.objects.get(id=bid)
   context = {
      "blog":blog,
   }
   return render(request, 'detail.html', context)
