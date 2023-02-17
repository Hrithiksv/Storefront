from django.db import models

# Create your models here.


class Topics(models.Model):

    text = models.CharField(max_length=200)
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):

    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    text = models.TextField()  # textField doesnt need the size limit
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."
