from django.db import models
from django import forms


class SubscribeForm(forms.Form):
    your_email = forms.CharField(label='Your Email', max_length=100)


class Subscribe(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id) + ' ' + self.email


class MainSlider(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default='')
    description = models.TextField()
    image = models.FileField(upload_to='slider')

    def __str__(self):
        return self.title + ' ' + self.subtitle


class About(models.Model):
    id = models.AutoField(primary_key=True)
    first_part_title = models.CharField(max_length=200)
    second_part_title = models.CharField(max_length=200, default='')
    description = models.TextField()
    image = models.FileField(upload_to='about')

    def __str__(self):
        return self.first_part_title + ' ' + self.second_part_title


class RoadMap(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=200, default='')
    description = models.TextField()
    image = models.FileField(upload_to='roadmap')

    def __str__(self):
        return self.title


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    first_part_title = models.CharField(max_length=200)
    second_part_title = models.CharField(max_length=200, default='')
    description = models.TextField()
    image = models.FileField(upload_to='service')
    m_image1 = models.FileField(upload_to='service/m', null=True)
    m_image1_word1 = models.CharField(max_length=10, default='')
    m_image1_word2 = models.CharField(max_length=10, default='')

    m_image2 = models.FileField(upload_to='service/m', null=True)
    m_image2_word1 = models.CharField(max_length=10, default='')
    m_image2_word2 = models.CharField(max_length=10, default='')

    m_image3 = models.FileField(upload_to='service/m', null=True)
    m_image3_word1 = models.CharField(max_length=10, default='')
    m_image3_word2 = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.first_part_title + ' ' + self.second_part_title


class DonationCase(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='donation_case')
    amount = models.FloatField()

    def __str__(self):
        return self.title


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='news')
    date = models.DateField()

    def __str__(self):
        return self.title
