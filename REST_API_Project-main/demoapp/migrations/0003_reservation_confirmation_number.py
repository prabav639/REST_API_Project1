# Generated by Django 4.0.3 on 2022-04-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_alter_reservation_checkin_alter_reservation_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='confirmation_number',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
