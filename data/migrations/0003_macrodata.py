# Generated by Django 3.2.7 on 2021-09-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data', '0002_delete_macrodata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Macrodata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarix', models.DateField()),
                ('year', models.IntegerField(blank=True, null=True)),
                ('month', models.IntegerField(blank=True, null=True)),
                ('ym', models.BigIntegerField(blank=True, null=True)),
                ('gdp', models.FloatField(blank=True, null=True)),
                ('gdp_def', models.FloatField(blank=True, null=True)),
                ('ngdp', models.FloatField(blank=True, null=True)),
                ('rgdp', models.FloatField(blank=True, null=True)),
                ('rngdp', models.FloatField(blank=True, null=True)),
                ('cap_invest', models.FloatField(blank=True, null=True)),
                ('nominc', models.FloatField(blank=True, null=True)),
                ('budrev', models.FloatField(blank=True, null=True)),
                ('budrev_gdp', models.FloatField(blank=True, db_column='budrev/gdp', null=True)),
                ('budexp', models.FloatField(blank=True, null=True)),
                ('budexp_gdp', models.FloatField(blank=True, db_column='budexp/gdp', null=True)),
                ('buddef', models.FloatField(blank=True, null=True)),
                ('buddef_gdp', models.FloatField(blank=True, db_column='buddef/gdp', null=True)),
                ('neer', models.FloatField(blank=True, null=True)),
                ('nneer', models.FloatField(blank=True, null=True)),
                ('reer', models.FloatField(blank=True, null=True)),
                ('nreer', models.FloatField(blank=True, null=True)),
                ('cr_port', models.FloatField(blank=True, null=True)),
                ('vkk', models.FloatField(blank=True, null=True)),
                ('vkk_rate', models.FloatField(blank=True, null=True)),
                ('cpi_change', models.FloatField(blank=True, null=True)),
                ('cpi_chg_1', models.FloatField(blank=True, db_column='cpi_chg_+1', null=True)),
                ('cpi_cumul', models.FloatField(blank=True, null=True)),
                ('usdazn', models.FloatField(blank=True, null=True)),
                ('brent_oil_price', models.FloatField(blank=True, null=True)),
                ('nomsal', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
