from django.db import models


class SoftDeleteModelQuerySet(models.QuerySet):
    def delete(self):
        """Soft delete"""
        return super().update(is_deleted=True)

    def hard_delete(self):
        """Remove records from db"""
        return super().delete()

    def deleted(self) -> models.QuerySet:
        return self.filter(is_deleted=True)

    def active(self) -> models.QuerySet:
        return self.filter(is_deleted=False)
