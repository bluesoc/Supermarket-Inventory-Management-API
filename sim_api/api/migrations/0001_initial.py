# Generated by Django 4.2.11 on 2024-03-31 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('category', models.CharField(max_length=64)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField(blank=True, null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=128, null=True)),
                ('stock', models.BooleanField(default=True)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]
