from django.db import models
from datetime import datetime
# from django.db.models.fields import DecimalField
from django.utils import timezone


CATEGORY_CHOICES ={
  ("S", "shirt"),
  ("SW", "Sports Wear"),
  ("OW", "Outwear")
}
LABEL_CHOICES = {
  ('P', 'primary'),
  ('S', 'secondary'),
  ('D', 'danger')
}

class Product(models.Model):
  title = models.CharField(max_length=100)
  price = models. DecimalField(decimal_places=2, max_digits=100)
  discount_price = models.DecimalField(decimal_places=2, max_digits=100)
  featured = models.BooleanField(default=True)
  category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
  label = models.CharField(choices=LABEL_CHOICES, max_length=1)
  description = models.TextField()
  quantity_available = models.IntegerField(default=1)


  def __str__(self):
        return self.title
  def is_recently_added(self):
    return self.upload_date >= timezone.now() - datetime.timedelta(days=7)