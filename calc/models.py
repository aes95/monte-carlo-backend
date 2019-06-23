from django.db import models

# Create your models here.

class Index(models.Model):
    index_name = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    high = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    low = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    adj_close = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    mo_return = models.DecimalField(max_digits=10, decimal_places=7)

    def __str__(self):
        return f'{self.index_name} retured {self.mo_return} in {self.date}'

    #class Meta:
        #unique_together = ('name','date')

