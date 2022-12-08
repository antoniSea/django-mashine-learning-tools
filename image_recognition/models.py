from django.db import models

# imgage model with image field and label field and timestamp field
class Image(models.Model):
    image = models.ImageField(upload_to="static/uploads/")
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    label = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label