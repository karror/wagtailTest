
from __future__ import unicode_literals
from graphene import ObjectType, List, resolve_only_args, Schema
from graphene_django import DjangoObjectType
from wagtail.images.models import Image
from ..models import CardPage, Tag, Rate


class CardNode(DjangoObjectType):
    class Meta:
        model = CardPage


class TagNode(DjangoObjectType):
    class Meta:
        model = Tag


class RateNode(DjangoObjectType):
    class Meta:
        model = Rate


class ImageNode(DjangoObjectType):
    class Meta:
        model = Image
        exclude_fields = ['tags']


class Query(ObjectType):
    cards = List(CardNode)
    tags = List(TagNode)
    rates = List(RateNode)
    images = List(ImageNode)

    @resolve_only_args
    def resolve_cards(self):
        return CardPage.objects.all()

    @resolve_only_args
    def resolve_tags(self):
        return Tag.objects.all()

    @resolve_only_args
    def resolve_rates(self):
        return Rate.objects.all()

    @resolve_only_args
    def resolve_rates(self):
        return Image.objects.all()


schema = Schema(query=Query)
