from django.db import models

class infoModel(models.Model):
    tracker = models.CharField('link',max_length=10, blank=True)
    notes = models.CharField('notes',max_length=50,blank=True)
    clicked = models.BooleanField(null=True)

class pingModel(models.Model):
    ip = models.CharField(max_length=20)
    timee = models.DateTimeField(auto_now_add=True)
    incoming = models.ForeignKey(infoModel, on_delete=models.PROTECT,related_name='ongoing')