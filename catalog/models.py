from django.db import models


class Market(models.Model):

    title = models.CharField(max_length = 200, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length = 200)

    class Meta:
        verbose_name = 'market'
        verbose_name_plural = 'markets'

    def __str__(self):
        return self.title

class Strategy(models.Model):

    title = models.CharField(max_length = 200, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length = 200, unique=True, null=False, blank=False)
    market = models.ManyToManyField(Market)
    cagr = models.DecimalField(max_digits=3, decimal_places=2)
    sharpe = models.DecimalField(max_digits=3, decimal_places=2)
    long_only = models.BooleanField(default=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'strategy'
        verbose_name_plural = 'strategies'

    def __str__(self):
        return self.title





