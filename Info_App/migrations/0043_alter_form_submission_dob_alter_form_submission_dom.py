# Generated by Django 4.1.6 on 2023-05-04 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Info_App', '0042_alter_form_submission_member_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_submission',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='form_submission',
            name='DOM',
            field=models.DateField(blank=True, null=True),
        ),
    ]