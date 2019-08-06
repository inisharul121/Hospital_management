from django.contrib import admin
from appointment import models
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from appointment import models


# Register your models here.


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'user_type', 'first_name', 'last_name', 'password']
    list_display = ('user_type',)
    list_filter = ('user_type',)

admin.site.register(models.Patient)
admin.site.register(models.Doctor)
admin.site.register(models.Department)
admin.site.register(models.Appointment)