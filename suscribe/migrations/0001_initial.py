# Generated by Django 4.0.4 on 2022-07-15 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suscribtion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]