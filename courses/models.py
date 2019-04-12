from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=20)
    cell_technology = models.CharField(max_length=20)
    cell_manufacturer = models.CharField(max_length=20)
    number_of_cells = models.CharField(max_length=20)
    number_of_cells_in_series = models.CharField(max_length=20)
    number_of_series_strings = models.CharField(max_length=20)
    number_of_diodes = models.CharField(max_length=20)
    product_lenght = models.CharField(max_length=20)
    product_width = models.CharField(max_length=20)
    product_weight = models.CharField(max_length=20)
    superstate_type = models.CharField(max_length=20)
    superstate_manufacturer = models.CharField(max_length=20)
    substrate_type = models.CharField(max_length=20)
    substrate_manufacturer = models.CharField(max_length=20)
    frame_type = models.CharField(max_length=20)
    frame_adhesive = models.CharField(max_length=20)
    encapsulation_type = models.CharField(max_length=20)
    encapsulation_manufacturer = models.CharField(max_length=20)
    junction_box_type = models.CharField(max_length=20)
    junction_box_manufacturer = models.CharField(max_length=20)

class Certificate(models.Model):
    certificate_ID = models.CharField(max_length=20)
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    report_number = models.CharField(max_length=20)
    issue_date = models.CharField(max_length=20)
    model_number = models.ForeignKey(Product, on_delete=models.CASCADE)

class Service(models.Model):
    service_name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    is_FI_required = models.CharField(max_length=20)
    FI_frequency = models.CharField(max_length=20)