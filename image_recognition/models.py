from django.db import models

# imgage model with image field and label field and timestamp field
class Image(models.Model):
    image = models.ImageField(upload_to="static/uploads/")
    # abstract user model related to image model with one to many relationship user_id field
    # user_id = models.ForeignKey(models.user, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label