# Generated by Django 3.0.8 on 2021-09-16 10:26

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentName',
            fields=[
                ('name_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(11)])),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=13, region=None)),
                ('polling_unit_unique_id', models.IntegerField(validators=[django.core.validators.MaxValueValidator(11)])),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncedLGAResults',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(11)])),
                ('lga_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField(validators=[django.core.validators.MaxValueValidator(11)])),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncedPUResults',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(11)])),
                ('polling_unit_unique_id', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50)])),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField(validators=[django.core.validators.MaxValueValidator(11)])),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncedStateResults',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(11)])),
                ('state_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField(validators=[django.core.validators.MaxValueValidator(11)])),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncedWardResults',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(11)])),
                ('ward_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField(validators=[django.core.validators.MaxValueValidator(11)])),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LGA',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(11)])),
                ('lga_id', models.IntegerField(validators=[django.core.validators.MaxValueValidator(11)])),
                ('lga_name', models.CharField(max_length=50)),
                ('state_id', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50)])),
                ('lga_description', models.TextField(blank=True)),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField(default=None)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(11)])),
                ('party_id', models.CharField(max_length=11)),
                ('party_name', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='PollingUnit',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(11)])),
                ('polling_unit_id', models.IntegerField(validators=[django.core.validators.MaxValueValidator(11)])),
                ('ward_id', models.IntegerField(validators=[django.core.validators.MaxValueValidator(11)])),
                ('lga_id', models.IntegerField(validators=[django.core.validators.MaxValueValidator(11)])),
                ('unique_ward_id', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(11)])),
                ('polling_unit_number', models.CharField(max_length=50, null=True)),
                ('polling_unit_name', models.CharField(max_length=50, null=True)),
                ('polling_unit_description', models.TextField(blank=True, null=True)),
                ('lat', models.CharField(max_length=255, null=True)),
                ('long', models.CharField(max_length=255, null=True)),
                ('entered_by_user', models.CharField(max_length=50, null=True)),
                ('date_entered', models.DateTimeField(null=True)),
                ('user_ip_address', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(11)])),
                ('state_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(11)])),
                ('ward_id', models.IntegerField(validators=[django.core.validators.MaxValueValidator(11)])),
                ('ward_name', models.CharField(max_length=50)),
                ('lga_id', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50)])),
                ('ward_description', models.TextField(blank=True)),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField(null=True)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
    ]