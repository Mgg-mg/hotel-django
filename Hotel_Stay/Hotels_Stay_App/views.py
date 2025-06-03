#from django.shortcuts import render

# Create your views here.

#from django.shortcuts import render
#from django.http import HttpResponse
#def home(request):
    #return HttpResponse("¡Hola desde Hotels_Stay_App!")

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render({}, request))

def blog(request):
    template = loader.get_template('blog.html')
    return HttpResponse(template.render({}, request))

def grid(request):
    template = loader.get_template('grid.html')
    return HttpResponse(template.render({}, request))


def single_post(request):
    template = loader.get_template('single-post.html')
    return HttpResponse(template.render({}, request))

def blog_page_2(request):
    return render(request, 'blog_page_2.html')
