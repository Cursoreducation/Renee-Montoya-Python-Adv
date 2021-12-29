from django.db import models

from src.common.querysets import SoftDeleteModelQuerySet


class BaseDateAuditModel(models.Model):
    """Abstract model. При описі моделі міграції не будуть створюватися.
    Використовується для розширення інших моделей."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteAuditModel(BaseDateAuditModel):
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteModelQuerySet.as_manager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)
