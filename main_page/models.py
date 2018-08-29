from django.db import models

# Create your models here.



class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    number= models.CharField(max_length=64)
    text=models.TextField()

    def __str__(self):
        return "Пользователь %s %s" % (self.name, self.email,)

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'A lot of Subscribers'
