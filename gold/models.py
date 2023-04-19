from django.db import models

class Bitcoin(models.Model):
    title = models.CharField(max_length=50,)
    dema = models.CharField(max_length=50, default='n/a')
    ema = models.CharField(max_length=50, default='n/a')
    ht = models.CharField(max_length=50, default='n/a')
    kama = models.CharField(max_length=50, default='n/a')
    sar = models.CharField(max_length=50, default='n/a')
    sma = models.CharField(max_length=50, default='n/a')
    trima = models.CharField(max_length=50, default='n/a')
    wma = models.CharField(max_length=50, default='n/a')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
