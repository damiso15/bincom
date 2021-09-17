from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator

# Create your models here.


class AgentName(models.Model):
    name_id = models.AutoField(validators=[MaxValueValidator(11)], primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = PhoneNumberField(max_length=13)
    polling_unit_unique_id = models.IntegerField(validators=[MaxValueValidator(11)])


class AnnouncedLGAResults(models.Model):
    result_id = models.AutoField(validators=[MaxValueValidator(11)], primary_key=True)
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField(validators=[MaxValueValidator(11)])
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)


class AnnouncedPUResults(models.Model):
    result_id = models.AutoField(validators=[MaxValueValidator(11)], primary_key=True)
    polling_unit_unique_id = models.IntegerField(validators=[MaxValueValidator(50)])
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField(validators=[MaxValueValidator(11)])
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)


class AnnouncedStateResults(models.Model):
    result_id = models.AutoField(validators=[MaxValueValidator(11)], primary_key=True)
    state_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField(validators=[MaxValueValidator(11)])
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)


class AnnouncedWardResults(models.Model):
    result_id = models.AutoField(validators=[MaxValueValidator(11)], primary_key=True)
    ward_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField(validators=[MaxValueValidator(11)])
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)


class LGA(models.Model):
    unique_id = models.AutoField(validators=[MaxValueValidator(11)], primary_key=True)
    lga_id = models.IntegerField(validators=[MaxValueValidator(11)])
    lga_name = models.CharField(max_length=50)
    state_id = models.IntegerField(validators=[MaxValueValidator(50)])
    lga_description = models.TextField(blank=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(null=True)
    user_ip_address = models.CharField(max_length=50)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('lga_polling_result', args=[str(self.unique_id)])


class Party(models.Model):
    id = models.AutoField(validators=[MaxValueValidator(11)], primary_key=True)
    party_id = models.CharField(max_length=11)
    party_name = models.CharField(max_length=11)


class PollingUnit(models.Model):
    unique_id = models.AutoField(validators=[MaxValueValidator(11)], primary_key=True)
    polling_unit_id = models.IntegerField(validators=[MaxValueValidator(11)])
    ward_id = models.IntegerField(validators=[MaxValueValidator(11)])
    lga_id = models.IntegerField(validators=[MaxValueValidator(11)])
    unique_ward_id = models.IntegerField(validators=[MaxValueValidator(11)], null=True)
    polling_unit_number = models.CharField(max_length=50, null=True)
    polling_unit_name = models.CharField(max_length=50, null=True)
    polling_unit_description = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=255, null=True)
    long = models.CharField(max_length=255, null=True)
    entered_by_user = models.CharField(max_length=50, null=True)
    date_entered = models.DateTimeField(null=True)
    user_ip_address = models.CharField(max_length=50, null=True)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('polling_unit_result', args=[str(self.unique_id)])


class States(models.Model):
    state_id = models.AutoField(validators=[MaxValueValidator(11)], primary_key=True)
    state_name = models.CharField(max_length=50)


class Ward(models.Model):
    unique_id = models.AutoField(validators=[MaxValueValidator(11)], primary_key=True)
    ward_id = models.IntegerField(validators=[MaxValueValidator(11)])
    ward_name = models.CharField(max_length=50)
    lga_id = models.IntegerField(validators=[MaxValueValidator(50)])
    ward_description = models.TextField(blank=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(null=True)
    user_ip_address = models.CharField(max_length=50)
