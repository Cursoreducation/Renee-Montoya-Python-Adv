import factory

from apps.photos.models import Photo


class PhotoFactory(factory.DjangoModelFactory):
    class Meta:
        model = Photo
