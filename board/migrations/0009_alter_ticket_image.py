# Generated by Django 3.2.2 on 2021-05-31 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_alter_ticket_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='img'),
        ),
    ]
