# Generated by Django 4.1.6 on 2023-05-03 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Info_App', '0046_alter_personal_info_dom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_info',
            name='DOM',
            field=models.DateField(blank=True, null=True),
        ),
    ]
