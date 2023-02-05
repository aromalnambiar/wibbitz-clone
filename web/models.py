from django.db import models



class Customers(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to="promoters/")

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email
