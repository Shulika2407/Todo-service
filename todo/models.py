from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("todo:todo-list", kwargs={"pk": self.pk})


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["done", "-datetime"]

    def get_absolute_url(self):
        return reverse("todo:todo-list", kwargs={"pk": self.pk})
