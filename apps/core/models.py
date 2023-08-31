import uuid

from django.db import models


class UUIDPrimaryModel(models.Model):
    uid = models.UUIDField("UUID", default=uuid.uuid4, primary_key=True)

    class Meta:
        abstract = True