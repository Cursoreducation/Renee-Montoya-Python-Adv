import factory
from factory import fuzzy

from apps.dealers.models import Dealer, City, Address, Country


class CountryFactory(factory.DjangoModelFactory):
    name = fuzzy.FuzzyText()

    class Meta:
        model = Country


class CityFactory(factory.DjangoModelFactory):
    name = fuzzy.FuzzyText()
    country = factory.SubFactory(CountryFactory)

    class Meta:
        model = City


class AddressFactory(factory.DjangoModelFactory):
    address1 = fuzzy.FuzzyText()
    address2 = fuzzy.FuzzyText()
    zip_code = fuzzy.FuzzyInteger(low=0, high=9999)
    city = factory.SubFactory(CityFactory)

    class Meta:
        model = Address


class DealerFactory(factory.DjangoModelFactory):
    address = factory.SubFactory(AddressFactory)

    class Meta:
        model = Dealer
