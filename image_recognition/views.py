from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image
from django.template import loader
from django.core.paginator import Paginator
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from django.views.generic import View
import cv2 as cv
from django.core.files.storage import FileSystemStorage
import urllib
import base64
import json
from django.db.models.functions import Lower

def train(request):
  if request.method == 'POST':
    model = tf.keras.models.load_model('image_recognition/model.h5')
    #convert image 
    return HttpResponse("Model został zaktualizowany")

  template = loader.get_template('image_recognition/train.html')

  context = {
    'class_names': ['apple', 'quarium_fish', 'baby', 'bear', 'beaver', 'bed', 'bee', 'beetle', 'bicycle', 'bottle', 'bowl', 'boy', 'bridge', 'bus', 'butterfly', 'camel', 'can',
        'castle', 'caterpillar', 'cattle', 'chair', 'chimpanzee', 'clock', 'cloud', 'cockroach', 'couch', 'cra', 'crocodile', 'cup', 'dinosaur', 'dolphin', 'elephant', 'flatfish', 'forest', 'fox', 'girl', 'hamster', 'house', 'kangaroo', 'keyboard', 'lamp', 'lawn_mower', 'leopard', 'lion', 'lizard', 'lobster', 'man', 'maple_tree', 'motorcycle', 'mountain', 'mouse', 'mushroom', 'oak_tree', 'orange', 'orchid', 'otter', 'palm_tree', 'pear', 'pickup_truck', 'pine_tree', 'plain', 'plate', 'poppy', 'porcupine', 'possum', 'rabbit', 'raccoon', 'ray', 'road', 'rocket', 'rose', 'sea', 'seal', 'shark', 'shrew', 'skunk', 'skyscraper', 'snail', 'snake', 'spider', 'squirrel', 'streetcar', 'sunflower', 'sweet_pepper', 'table', 'tank', 'telephone', 'television', 'tiger', 'tractor', 'train', 'trout', 'tulip', 'turtle', 'wardrobe', 'whale', 'willow_tree', 'wolf', 'woman', 'worm']
  }

  return HttpResponse(template.render(context, request))

def downvote(request, image_id):
  image = Image.objects.get(id=image_id)
  image.downvotes += 1
  image.save()
  
  return redirect(request.META.get('HTTP_REFERER'))

def upvote(request, image_id):
  image = Image.objects.get(id=image_id)
  image.upvotes += 1
  image.save()

  return redirect(request.META.get('HTTP_REFERER'))

def list(request):
  template = loader.get_template('image_recognition/list.html')

  context = {
    'class_names': ['apple', 'quarium_fish', 'baby', 'bear', 'beaver', 'bed', 'bee', 'beetle', 'bicycle', 'bottle', 'bowl', 'boy', 'bridge', 'bus', 'butterfly', 'camel', 'can',
        'castle', 'caterpillar', 'cattle', 'chair', 'chimpanzee', 'clock', 'cloud', 'cockroach', 'couch', 'cra', 'crocodile', 'cup', 'dinosaur', 'dolphin', 'elephant', 'flatfish', 'forest', 'fox', 'girl', 'hamster', 'house', 'kangaroo', 'keyboard', 'lamp', 'lawn_mower', 'leopard', 'lion', 'lizard', 'lobster', 'man', 'maple_tree', 'motorcycle', 'mountain', 'mouse', 'mushroom', 'oak_tree', 'orange', 'orchid', 'otter', 'palm_tree', 'pear', 'pickup_truck', 'pine_tree', 'plain', 'plate', 'poppy', 'porcupine', 'possum', 'rabbit', 'raccoon', 'ray', 'road', 'rocket', 'rose', 'sea', 'seal', 'shark', 'shrew', 'skunk', 'skyscraper', 'snail', 'snake', 'spider', 'squirrel', 'streetcar', 'sunflower', 'sweet_pepper', 'table', 'tank', 'telephone', 'television', 'tiger', 'tractor', 'train', 'trout', 'tulip', 'turtle', 'wardrobe', 'whale', 'willow_tree', 'wolf', 'woman', 'worm']
  }

  return HttpResponse(template.render(context, request))


def index(request):
  images = Image.objects.order_by(Lower("timestamp").desc()).all()
  paginator = Paginator(images, 6) # Show 6 contacts per page.

  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  template = loader.get_template('image_recognition/index.html')

  context = {
    'images': page_obj,
    'page_obj': page_obj
  }

  return HttpResponse(template.render(context, request))

def delete(request, image_id):
  image = Image.objects.get(pk=image_id)
  image.delete()

  return index(request)

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

    class_names = ['apple', 'quarium_fish', 'baby', 'bear', 'beaver', 'bed', 'bee', 'beetle', 'bicycle', 'bottle', 'bowl', 'boy', 'bridge', 'bus', 'butterfly', 'camel', 'can',
        'castle', 'caterpillar', 'cattle', 'chair', 'chimpanzee', 'clock', 'cloud', 'cockroach', 'couch', 'cra', 'crocodile', 'cup', 'dinosaur', 'dolphin', 'elephant', 'flatfish', 'forest', 'fox', 'girl', 'hamster', 'house', 'kangaroo', 'keyboard', 'lamp', 'lawn_mower', 'leopard', 'lion', 'lizard', 'lobster', 'man', 'maple_tree', 'motorcycle', 'mountain', 'mouse', 'mushroom', 'oak_tree', 'orange', 'orchid', 'otter', 'palm_tree', 'pear', 'pickup_truck', 'pine_tree', 'plain', 'plate', 'poppy', 'porcupine', 'possum', 'rabbit', 'raccoon', 'ray', 'road', 'rocket', 'rose', 'sea', 'seal', 'shark', 'shrew', 'skunk', 'skyscraper', 'snail', 'snake', 'spider', 'squirrel', 'streetcar', 'sunflower', 'sweet_pepper', 'table', 'tank', 'telephone', 'television', 'tiger', 'tractor', 'train', 'trout', 'tulip', 'turtle', 'wardrobe', 'whale', 'willow_tree', 'wolf', 'woman', 'worm']

    model = tf.keras.models.load_model(
        'image_recognition/nn.h5', custom_objects=None, compile=True, options=None
    )
    
    req = urllib.request.urlopen("http://localhost:8000" + image.image.url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv.imdecode(arr, -1) # 'Load it as it is'
    
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    width = int(32)
    height = int(32)
    dim = (width, height)
    img = cv.resize(img, dim, interpolation = cv.INTER_AREA)

    prediction = model.predict(np.array([img]) / 255)

    image.label = class_names[np.argmax(prediction)]
    image.save()

    return detail(request, image.id)
  else:
    return render(request, 'image_recognition/upload.html')