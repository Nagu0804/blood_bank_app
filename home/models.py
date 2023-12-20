from django.db import models

class HomePageSlider(models.Model):
    id_number = models.IntegerField(blank=True, null=True )
    title = models.CharField(blank=True, null=True, max_length=20 )
    slider_1 = models.ImageField(upload_to='slider',blank=True, null=True)
    slider_2 = models.ImageField(upload_to='slider',blank=True, null=True)
    slider_3 = models.ImageField(upload_to='slider',blank=True, null=True)

    def __str__(self):
        return self.title

class HomePageBody(models.Model):
    id_vision = models.IntegerField(blank=True, null=True)
    title1 = models.CharField(blank=True, null=True, max_length=20)
    title2 = models.CharField(blank=True, null=True, max_length=20)
    title3 = models.CharField(blank=True, null=True, max_length=20)
    body_img1 = models.ImageField(upload_to='home_body', blank=True, null=True)
    body_img2 = models.ImageField(upload_to='home_body', blank=True, null=True)
    body_img3 = models.ImageField(upload_to='home_body', blank=True, null=True)
    body_text1 = models.TextField(blank=True, null=True)
    body_text2 = models.TextField(blank=True, null=True)
    body_text3 = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title1
