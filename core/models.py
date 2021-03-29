import datetime
import uuid

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import (
    GenericForeignKey,
    )
from django.db import models

from .constants import *


class GenericModel(models.Model):
    """
    Abstract model with generic fields.
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True


class StatusModel(models.Model):
    """
    Abstract model with status field.
    """
    status = models.CharField(max_length=200,
        choices=default_status,
        default='inactive')

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """
    Abstract model with timestamp fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']


class UUIDModel(models.Model):
    """
    Abstract model with uuid field.
    """
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    class Meta:
        abstract = True


class UploadMethodBase():
    """
    This is base methods to uploads model
    """
    @property
    def directory_prefix(self):
        return 'uploads'

    @property
    def file_exists(self):
        if bool(self.file):
            if self.file.name:
                return self.file.storage.exists(self.file.name)
        return False

    @property
    def file_extension(self):
        filename = self.file.name
        extension = filename.split('.')[-1]
        return extension

    @property
    def file_size(self):
        if self.file_exists:
            return self.file.size
        return None

    def _directory_path(instance, filename):
        """Rename file before save
        """
        ext = filename.split('.')[-1]
        new_filename = '{}.{}'.format(instance.uuid, ext)
        directory_prefix = instance.directory_prefix
        today = datetime.date.today()
        return '{0}/{1}/{2}/{3}/{4}'.format(instance.directory_prefix, today.year, today.month, today.day, new_filename)


class AttachmentModel(UUIDModel, UploadMethodBase):
    """
    Abstract model with generic file field.
    """
    file = models.FileField(upload_to=UploadMethodBase._directory_path,
        null=True,
        blank=True)
    thumbnail = models.ImageField(upload_to=UploadMethodBase._directory_path,
        null=True,
        blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)

    @property
    def thumb_file_exists(self):
        if self.thumbnail is not None:
            if self.thumbnail.name is not None:
                return self.thumbnail.storage.exists(self.thumbnail.name)
        return False


class PictureModel(UUIDModel, UploadMethodBase):
    """
    Abstract model with picture file field.
    """
    file = models.ImageField(upload_to=UploadMethodBase._directory_path,
        null=True,
        blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)
