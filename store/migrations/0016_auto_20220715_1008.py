# Generated by Django 3.0.6 on 2022-07-15 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20220715_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='bestsellerstatus',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
