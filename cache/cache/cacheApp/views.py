from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache


@cache_page(30)
def home(request):
    return HttpResponse("Home PAGE")


# def about(request):
#     name=cache.get('name',None)
#     if name==None:
#         cache.set('name','FizaKhan',30)
#         name=cache.get('name')
#     return render(request,'about.html',{'name':name})

# def about(request):
#     name=cache.get_or_set('name','FIZA',30,version=3)
#     return render(request,'about.html',{'name':name})

#SET MANY AND GET MANY

def about(request):
    data={
        'name':'FIZA',
        'age':22
    }
    cache.set_many(data,30)
    info=cache.get_many(data)
    return render(request,'about.html',{'info':info})


#deleting
def delete(request):
    cache.delete('name' ,version='2')   
    return HttpResponse("CACHE DELETED")
 
def menu(request):
    return render(request,'menu.html')



