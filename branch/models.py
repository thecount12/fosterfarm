from django.db import models

# Create your models here.


class BranchSite(models.Model):
    facility_name = models.CharField(max_length=60, blank=True)
    facility_type = models.CharField(max_length=30, blank=True)  # cultivation infusion etc...
    city_name = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    zip_code = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.facility_name

    def __str__(self):
        return self.facility_name
