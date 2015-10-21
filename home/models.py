from django.db import models

# Create your models here.

class FeaturedBox(models.Model):
    message = models.TextField(blank = True)

    class Meta:
        verbose_name_plural = "Featured Box"

class LeftPanel(models.Model):
    message = models.TextField(blank = True)

    class Meta:
        verbose_name_plural = "Left Panel"

class CenterPanel(models.Model):
    message = models.TextField(blank = True)

    class Meta:
        verbose_name_plural = "Center Panel"
