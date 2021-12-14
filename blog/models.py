from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Tag(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(BaseModel):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)

    def get_tags(self, obj):
        return "\n".join([str(t) for t in obj.tags.all()])

    def __str__(self):
        return self.title
