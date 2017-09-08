from __future__ import unicode_literals

from django.db import models


STRATEGY_CHOICES = (
    ('38344', 'AN No Tax BB (10%)'),
    ('38345', 'AN No Tax No BB (10%)'),
    ('38346', 'AN OS BB (10%)'),
    ('38347', 'AN OS No BB (10%)'),
    ('38342', 'AN Tax BB (10%)'),
    ('38343', 'AN Tax No BB (10%)'),
    ('38449', 'BB (5% No Tax)'),
    ('38450', 'BB (5% Tax)'),
    ('38435', 'CM BB'),
    ('38436', 'CM No BB'),
    ('23303', 'Managed Items Strategy (All)'),
    ('38451', 'No BB (5% No Tax)'),
    ('38452', 'No BB (5% Tax)'),
    ('38567', 'OS BB (5%)'),
    ('38568', 'OS No BB (5%)')
)


class Product(models.Model):
    sku = models.CharField('SKU',max_length=100, null=True, blank=True)
    asin = models.CharField('ASIN',max_length=100, null=True, blank=True)
    title = models.CharField('Title', max_length=1000, null=True, blank=True)
    bb_status = models.BooleanField('BB Status', default=False)
    bb_owner = models.CharField('Who Has BB', max_length=100, null=True, blank=True)
    our_min_price = models.FloatField('Our Min Price', null=True, blank=True)
    bb_price = models.FloatField('BuyBox Price', null=True, blank=True)
    appeagle_strategy = models.CharField('Appeagle Strategy', max_length=10, 
    									 choices=STRATEGY_CHOICES, null=True, blank=True)
    prime_az = models.BooleanField('Prime/AZ', default=False)
    num_orders = models.IntegerField('No. Of Orders w/in 30 Days ', default=0, null=True, blank=True) 
    added_at = models.DateTimeField('Added Time', auto_now_add=True)
    updated_at = models.CharField('Updated Time', max_length=30, null=True, blank=True)

    def __unicode__(self):
        return self.asin
        

class ProductHistory(models.Model):
    sku = models.CharField('SKU',max_length=100, null=True, blank=True)
    asin = models.CharField('ASIN',max_length=100, null=True, blank=True)
    title = models.CharField('Title', max_length=1000, null=True, blank=True)
    bb_status = models.BooleanField('BB Status', default=False)
    bb_owner = models.CharField('Who Has BB', max_length=100, null=True, blank=True)
    our_min_price = models.FloatField('Our Min Price', null=True, blank=True)
    bb_price = models.FloatField('BuyBox Price', null=True, blank=True)
    appeagle_strategy = models.CharField('Appeagle Strategy', max_length=10, 
    									 choices=STRATEGY_CHOICES, null=True, blank=True)
    prime_az = models.BooleanField('Prime/AZ', default=False)
    num_orders = models.IntegerField('No. Of Orders w/in 30 Days ', default=0, null=True, blank=True) 
    updated_at = models.CharField('Updated Time', max_length=30, null=True, blank=True)

    def __unicode__(self):
        return self.asin


class Interval(models.Model):
    interval = models.FloatField(help_text="Interval in hour")

    def __unicode__(self):
        return str(self.interval)
