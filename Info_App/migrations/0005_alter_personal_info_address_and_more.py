# Generated by Django 4.1.3 on 2022-11-28 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Info_App', '0004_alter_personal_info_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_info',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='email_id',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='member_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='membership_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
