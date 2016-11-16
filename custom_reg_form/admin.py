from django.contrib import admin
from .models import ExtraInfo
from .forms import ExtraInfoForm

class RegistrationAdmin(admin.ModelAdmin):
    form = ExtraInfoForm
    list_display = ('user','cell_number', 'id_passport_number', 'center', )

admin.site.register(ExtraInfo, RegistrationAdmin)