# Generated by Django 2.2.7 on 2019-12-10 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription_pedago', '0006_auto_20191209_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='demandes_particulieres',
            field=models.CharField(blank=True, default='', max_length=2000, null=True),
        ),
    ]