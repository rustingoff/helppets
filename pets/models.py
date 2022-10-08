from django.db import models


class MainSlider(models.Model):
    id = models.AutoField(primary_key=True)
    first_part_title = models.CharField(max_length=200)
    second_part_title = models.CharField(max_length=200, default='')
    description = models.TextField()
    image = models.FileField(upload_to='slider')

    def __str__(self):
        return self.first_part_title + ' ' + self.second_part_title


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
    m_image2 = models.FileField(upload_to='service/m', null=True)
    m_image3 = models.FileField(upload_to='service/m', null=True)

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
