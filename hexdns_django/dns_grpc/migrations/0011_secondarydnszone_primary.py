# Generated by Django 3.0.7 on 2020-06-19 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dns_grpc', '0010_secondarydnszone'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondarydnszone',
            name='primary',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]