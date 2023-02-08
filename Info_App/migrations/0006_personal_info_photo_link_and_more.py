# Generated by Django 4.1.3 on 2022-11-28 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Info_App', '0005_alter_personal_info_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_info',
            name='Photo_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='Phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='membership_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]