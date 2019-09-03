from django.db import models

# Create your models here.


class PlantData(models.Model):
    batch_plant_name = models.CharField(max_length=60, blank=True)
    strain = models.CharField(max_length=60, blank=True)
    phenotype = models.CharField(max_length=60, blank=True)
    planting_date  = models.DateField(null=True, blank=True)
    plant_propagation = models.CharField(max_length=60, blank=True)  # clone, seedling, tissue
    quantity = models.IntegerField(blank=True, null=True)
    mother_plant_id = models.CharField(max_length=60, blank=True)  # foreign
    matriarch_plant = models.CharField(max_length=60, blank=True)  # foreign
    cultivation_location = models.CharField(max_length=60, blank=True)  # foreign
    feeding_schedule = models.CharField(max_length=60, blank=True)
    label_id = models.CharField(max_length=60, blank=True)


class PackagePlant(models.Model):
    item = models.CharField(max_length=60, blank=True)
    storage_location = models.CharField(max_length=60, blank=True)
    date_packaged = models.DateField(null=True, blank=True)
    packaged_plants = models.CharField(max_length=60, blank=True)
    label_id = models.CharField(max_length=60, blank=True)


class DestroyPlant(models.Model):
    waste = models.CharField(max_length=60, blank=True)
    destroy_reason = models.CharField(max_length=60, blank=True)
    destroy_date = models.DateField(null=True, blank=True)


class Harvest(models.Model):
    lot =  models.CharField(max_length=60, blank=True)
    harvest_batch = models.CharField(max_length=60, blank=True)
    original_weight = models.CharField(max_length=60, blank=True)
    current_weight = models.CharField(max_length=60, blank=True)
    waste = models.CharField(max_length=60, blank=True)
    new_harvest_batch_weight = models.CharField(max_length=60, blank=True)
    final_weight = models.CharField(max_length=60, blank=True)
    harvest_date = models.DateField(null=True, blank=True)
    current_moisture = models.CharField(max_length=60, blank=True)
    current_moisture_loss = models.CharField(max_length=60, blank=True)
    storage_area = models.CharField(max_length=60, blank=True)

