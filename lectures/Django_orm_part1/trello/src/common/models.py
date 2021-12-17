from django.db import models


class BaseDateAuditModel(models.Model):
    """Abstract model. При описі моделі міграції не будуть створюватися.
    Використовується для розширення інших моделей."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
