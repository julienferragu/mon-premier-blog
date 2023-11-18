# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activity(models.Model):
    id_activity = models.TextField(primary_key=True)
    availability = models.TextField()
    category = models.ForeignKey('Category', models.DO_NOTHING, db_column='category')

    class Meta:
        managed = False
        db_table = 'Activity'


class Category(models.Model):
    id_category = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Category'


class Mountaineer(models.Model):
    id_mountaineer = models.TextField(primary_key=True)
    nationality = models.TextField()
    activity = models.ForeignKey(Activity, models.DO_NOTHING, db_column='activity')
    state = models.TextField()
    oxygen = models.TextField()

    class Meta:
        managed = False
        db_table = 'Mountaineer'
