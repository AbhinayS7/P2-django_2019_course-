# Generated by Django 4.0 on 2024-04-27 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=200)),
                ('pub_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
