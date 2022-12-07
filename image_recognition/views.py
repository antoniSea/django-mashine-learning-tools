from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from django.template import loader

def index(request):
  images = Image.objects.all()
  template = loader.get_template('image_recognition/index.html')
  context = {
    'images': images,
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