# Generated by Django 3.1.8 on 2021-08-03 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0012_auto_20210730_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
