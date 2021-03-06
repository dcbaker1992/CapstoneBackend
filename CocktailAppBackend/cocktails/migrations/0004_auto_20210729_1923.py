# Generated by Django 3.1.8 on 2021-07-30 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0003_auto_20210729_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('preparation', models.TextField()),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cocktails.user')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='favoriteslist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='review',
            name='cocktail_id',
        ),
        migrations.DeleteModel(
            name='CustomDrink',
        ),
        migrations.DeleteModel(
            name='FavoritesList',
        ),
        migrations.DeleteModel(
            name='Ingredients',
        ),
        migrations.AddField(
            model_name='cocktails',
            name='ingredients',
            field=models.ManyToManyField(blank=True, null=True, to='cocktails.Ingredient'),
        ),
        migrations.AddField(
            model_name='review',
            name='cocktail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cocktails.cocktails'),
        ),
    ]
