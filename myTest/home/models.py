from django.db import models

from wagtail.core.models import Page, ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel


class Tag(ClusterableModel):
    name = models.CharField('name', default='', max_length=50)
    url = models.URLField('url', max_length=300, null=True, blank=True)
    card = ParentalKey('CardPage', on_delete=models.SET_NULL, null=True, blank=True, related_name='tags')

    panels = [
        FieldPanel('name'),
        FieldPanel('url')
    ]


class Rate(ClusterableModel):
    rate = models.PositiveSmallIntegerField('rate', default=10)
    desc = models.CharField('desc', max_length=100, null=True, blank=True)
    color = models.CharField('color', max_length=10, null=True, blank=True)
    card = ParentalKey('CardPage', on_delete=models.SET_NULL, null=True, blank=True, related_name='rates')

    panels = [
        FieldPanel('rate'),
        FieldPanel('desc'),
        FieldPanel('color')
    ]


class CardPage(Page):
    card_type = models.CharField('type', max_length=3, default='exp')
    img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='cards'
    )
    link = models.URLField('link', null=True, blank=True)
    subtitle = models.CharField('subtitle', max_length=300, null=True, blank=True)
    begin = models.CharField('begin', max_length=10, null=True, blank=True)
    end = models.CharField('end', max_length=10, null=True, blank=True)
    text = models.TextField('text', null=True, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('card_type'),
        FieldPanel('text'),
        ImageChooserPanel('img'),
        FieldPanel('link'),
        FieldPanel('begin'),
        FieldPanel('end'),
        InlinePanel('tags', label="Tags"),
        InlinePanel('rates', label="Rates")
    ]

    def save_base(self, raw=False, force_insert=False,
                  force_update=False, using=None, update_fields=None):
        print(str(self.tags))
        super().save_base()
