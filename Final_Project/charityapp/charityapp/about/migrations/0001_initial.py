# Generated by Django 4.2.2 on 2023-07-22 08:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('member_role', models.CharField(max_length=100)),
                ('profile_picture', models.URLField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]