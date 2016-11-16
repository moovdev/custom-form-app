from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
CENTER = (
        ('Johannesburg - Central', 'Johannesburg-Central'),
        ('Soweto - Jabavu', 'Soweto - Jabavu'),
        ('Soweto - Emndeni', 'Soweto - Emndeni'),
        ('Alexandra', 'Alexandra'),
        ('Orange Farm', 'Orange Farm'),
        ('Westbury', 'Westbury'),
        ('Sandton', 'Sandton'),
        ('Diepsloot', 'Diepsloot'),
        ('Ivory Park', 'Ivory Park'),
        ('Eldorado Park', 'Eldorado Park'),
        ('Poortjie', 'Poortjie'),
        ('Cosmo City', 'Cosmo City'),
    )
class ExtraInfo(models.Model):

    cell_number = models.CharField(_("Cell Number"),max_length=10)
    id_passport_number = models.CharField(_("ID/Passport Number"),max_length=10)
    center = models.CharField(_("Center"),max_length=50, choices=CENTER)
    user = models.OneToOneField(USER_MODEL, null=True)
