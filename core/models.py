from django.db import models

# Create your models here.


# python manage.py makemigrations
# python manage.py migrate


class Feedback(models.Model):
    name = models.CharField(max_length=32)
    text = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)

    class Meta():
        ordering = ('created',)  # use "-" before to change sort direction

    def __str__(self):
        return f'Feedback from {self.name}: {self.text}'


class Subject(models.Model):
    name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Messanger(models.Model):
    name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Bot(models.Model):
    name = models.CharField(max_length=32, default='')
    subject = models.ForeignKey(Subject, models.PROTECT)
    messanger = models.ForeignKey(Messanger, models.PROTECT)
    is_active = models.BooleanField(default=False)
