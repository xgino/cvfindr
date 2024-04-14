from django.db import models

class Service(models.Model):
    SCRAPE_CHOICES = [
        ('200', '200 Emails'),
        ('500', '500 Emails'),
        ('1000+', '1000 Emails'),
    ]

    name = models.CharField(max_length=100, null=True, blank=True)
    emails = models.CharField(max_length=100, choices=SCRAPE_CHOICES, null=True, blank=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name