from django.db import models
from django.shortcuts import render

class infoform(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    satus = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name