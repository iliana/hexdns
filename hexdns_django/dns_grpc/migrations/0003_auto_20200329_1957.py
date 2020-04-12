# Generated by Django 3.0.4 on 2020-03-29 19:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dns_grpc", "0002_auto_20200329_1610"),
    ]

    operations = [
        migrations.CreateModel(
            name="CNAMERecord",
            fields=[
                (
                    "dnszonerecord_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="dns_grpc.DNSZoneRecord",
                    ),
                ),
                ("alias", models.CharField(max_length=255)),
            ],
            bases=("dns_grpc.dnszonerecord",),
        ),
        migrations.CreateModel(
            name="ReverseDNSZone",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("zone_root_address", models.GenericIPAddressField()),
                (
                    "zone_root_prefix",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MaxValueValidator(128)]
                    ),
                ),
                ("last_modified", models.DateTimeField()),
            ],
            options={
                "verbose_name": "Reverse DNS Zone",
                "verbose_name_plural": "Reverse DNS Zones",
            },
        ),
        migrations.AddField(
            model_name="addressrecord",
            name="auto_reverse",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="dnszonerecord", name="ttl", field=models.PositiveIntegerField(),
        ),
        migrations.CreateModel(
            name="ReverseDNSZoneRecord",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("record_name", models.CharField(default="@", max_length=255)),
                ("ttl", models.PositiveIntegerField()),
                (
                    "zone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dns_grpc.ReverseDNSZone",
                    ),
                ),
            ],
        ),
    ]
