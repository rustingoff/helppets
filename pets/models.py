from django.db import models


class MainSlider(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='slider')

    def __str__(self):
        return self.title


class About(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='about')

    def __str__(self):
        return self.title


class RoadMap(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='roadmap')

    def __str__(self):
        return self.title


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='service')
    micro_images = models.FileField(upload_to='service', null=True, blank=True)

    def __str__(self):
        return self.title


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
