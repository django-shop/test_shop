from django.http import HttpResponse, Http404
from django.template import loader, Context
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect
from mysite.general.models import *

def hello(request):
    return HttpResponse('hello')

def cat(request, ca):
    id_cat = Category.objects.get(slug=ca)
    subcats = SubCategory.objects.filter(sel_cat=id_cat)
    #return HttpResponse(id_cat.id)
    return direct_to_template(request, 'index.html', {'subcats': subcats, })

def magazin(request):
    #id_cat = Category.objects.get(id=4)
    categoryes = Category.objects.all()
    return direct_to_template(request, 'index.html', {'categoryes': categoryes, })
    #return HttpResponse(id_cat.slug)

def subcat(request, ca, subca):
    id_subcat = SubCategory.objects.get(slug=subca)
    products = list(Product.objects.filter(sel_subcat=id_subcat))
    #return HttpResponse(products)
    return direct_to_template(request, 'index.html', {'products': products, })