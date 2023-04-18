from django.db import models


class Object(models.Model):
    object_id = models.CharField(max_length=200, primary_key=True)
    batch_id = models.CharField(max_length=200, null=True)
    data = models.JSONField()
