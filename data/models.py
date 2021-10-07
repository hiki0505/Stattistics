# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Macrodata2(models.Model):
    tarix = models.DateField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    months = models.IntegerField(blank=True, null=True)
    ym = models.BigIntegerField(blank=True, null=True)
    gdp = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    gdp_def = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ngdp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rgdp = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    rngdp = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    cap_invest = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nominc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nomsal = models.CharField(max_length=500, blank=True, null=True)
    budrev = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    budrev_gdp = models.DecimalField(db_column='budrev/gdp', max_digits=10, decimal_places=2, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    budexp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    budexp_gdp = models.DecimalField(db_column='budexp/gdp', max_digits=10, decimal_places=2, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    buddef = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    buddef_gdp = models.DecimalField(db_column='buddef/gdp', max_digits=10, decimal_places=2, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    neer = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nneer = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reer = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nreer = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cr_port = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vkk = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vkk_rate = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    cpi_change = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cpi_chg_1 = models.DecimalField(db_column='cpi_chg_+1', max_digits=10, decimal_places=4, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cpi_cumul = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    usdazn = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    brend_oil_price = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'macrodata2'
