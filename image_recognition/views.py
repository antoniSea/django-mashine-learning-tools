from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from django.template import loader
from django.core.paginator import Paginator

def index(request):
  images = Image.objects.all()
  paginator = Paginator(images, 6) # Show 6 contacts per page.

  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  template = loader.get_template('image_recognition/index.html')

  context = {
    'images': page_obj,
    'page_obj': page_obj
  }

  return HttpResponse(template.render(context, request))

def detail(request, image_id):
  image = Image.objects.get(pk=image_id)
  template = loader.get_template('image_recognition/show.html')
  context = {
    'image': image,
  }

  return HttpResponse(template.render(context, request))

def upload (request):
  if request.method == 'POST':
    image = Image()
    image.image = request.FILES['image']
    image.save()

    return detail(request, image.id)
  else:
    return render(request, 'image_recognition/upload.html')