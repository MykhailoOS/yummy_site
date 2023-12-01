# Generated by Django 4.2.7 on 2023-11-27 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DishCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('order', models.PositiveSmallIntegerField()),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
    ]