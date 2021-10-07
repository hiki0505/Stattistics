# Generated by Django 3.2.7 on 2021-09-16 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_alter_macrodata_tarix'),
    ]

    operations = [
        migrations.CreateModel(
            name='Macrodata2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarix', models.DateField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('months', models.IntegerField(blank=True, null=True)),
                ('ym', models.BigIntegerField(blank=True, null=True)),
                ('gdp', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('gdp_def', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ngdp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('rgdp', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('rngdp', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('cap_invest', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('nominc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('nomsal', models.CharField(blank=True, max_length=500, null=True)),
                ('budrev', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('budrev_gdp', models.DecimalField(blank=True, db_column='budrev/gdp', decimal_places=2, max_digits=10, null=True)),
                ('budexp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('budexp_gdp', models.DecimalField(blank=True, db_column='budexp/gdp', decimal_places=2, max_digits=10, null=True)),
                ('buddef', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('buddef_gdp', models.DecimalField(blank=True, db_column='buddef/gdp', decimal_places=2, max_digits=10, null=True)),
                ('neer', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('nneer', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('reer', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('nreer', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cr_port', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('vkk', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('vkk_rate', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('cpi_change', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cpi_chg_1', models.DecimalField(blank=True, db_column='cpi_chg_+1', decimal_places=4, max_digits=10, null=True)),
                ('cpi_cumul', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('usdazn', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('brend_oil_price', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'macrodata2',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Macrodata',
        ),
    ]
