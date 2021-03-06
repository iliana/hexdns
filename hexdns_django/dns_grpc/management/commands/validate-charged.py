from django.core.management.base import BaseCommand
from django.conf import settings
import django_keycloak_auth.clients
from dns_grpc import models, views
import requests


class Command(BaseCommand):
    help = 'Checks that every non charged zone is accessible by the user'

    def handle(self, *args, **options):
        user_zones = {}
        client_token = django_keycloak_auth.clients.get_access_token()

        for zone in models.DNSZone.objects.all():
            if zone.charged:
                continue

            user = zone.get_user()

            if user.username not in user_zones:
                user_zones[user.username] = {
                    "user": user,
                    "zones": [zone]
                }
            else:
                user_zones[user.username]["zones"].append(zone)

        for user, data in user_zones.items():
            r = requests.put(f"{settings.DOMAINS_URL}/api/internal/domains/{user}/", json={
                "domains": list(map(lambda z: {
                    "domain": z.zone_root
                }, data["zones"]))
            }, headers={
                "Authorization": f"Bearer {client_token}"
            })
            r.raise_for_status()
            rdata = r.json()
            domains = {}
            for domain in rdata["domains"]:
                domains[domain["domain"]] = domain["access"]

            for zone in data["zones"]:
                if zone.zone_root in domains:
                    if not domains[zone.zone_root]:
                        print(f"Setting {zone.zone_root} to charged")
                        zone.charged = True
                        zone.save()

            views.log_usage(data["user"], off_session=True)
