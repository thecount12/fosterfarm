from django.contrib import admin

# Register your models here.

from branch.models import BranchSite


class BranchAdmin(admin.ModelAdmin):
    list_display = ["facility_name"]


admin.site.register(BranchSite, BranchAdmin)
