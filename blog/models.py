from django.db import models
import uuid

# Create your models here.
class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ext_id = models.CharField(max_length=10, blank=True, null=True)
    tag_text = models.CharField(verbose_name='タグ', max_length=100)

    @classmethod
    def create(cls, ext_id, tag_text):
        return cls(uuid.uuid1(), ext_id, tag_text)


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ext_id = models.CharField(max_length=10, blank=True, null=True)
    body = models.CharField(verbose_name='本文', max_length=1000)
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    @classmethod
    def create(cls, ext_id, body):
        return cls(uuid.uuid1(), ext_id, body)

