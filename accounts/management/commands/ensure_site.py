"""Sincroniza el Site de django.contrib.sites con SITE_NAME / SITE_DOMAIN."""
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = (
        "Actualiza nombre y dominio del Site activo (los usa allauth en los "
        "correos de verificación). Idempotente: se puede ejecutar en cada deploy."
    )

    def handle(self, *args, **options):
        name = getattr(settings, 'SITE_NAME', 'TAI 2027')
        domain = getattr(settings, 'SITE_DOMAIN', 'tai-oposiciones.onrender.com')
        site_id = getattr(settings, 'SITE_ID', 1)

        site, created = Site.objects.get_or_create(
            pk=site_id, defaults={'name': name, 'domain': domain}
        )
        if not created and (site.name != name or site.domain != domain):
            site.name = name
            site.domain = domain
            site.save(update_fields=['name', 'domain'])
        Site.objects.clear_cache()

        accion = 'creado' if created else 'actualizado'
        self.stdout.write(self.style.SUCCESS(f'Site {accion}: {site.name} ({site.domain})'))
