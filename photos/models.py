from django.db import models


class Photo(models.Model):
    caption = models.CharField(max_length=100)
    src = models.ImageField(
        width_field='width', height_field='height', upload_to='photos/%Y/%m/%d/')
    width = models.IntegerField(editable=False, null=True)
    height = models.IntegerField(editable=False, null=True)

    def __str__(self):
        return self.caption
