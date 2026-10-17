from .models import Invitacion


def access_requests_processor(request):
    """
    Context processor para notificar al administrador si hay solicitudes
    de acceso pendientes de revisión.
    """
    if hasattr(request, 'user') and request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser):
        count = Invitacion.objects.filter(activo=False).count()
        return {
            'solicitudes_pendientes_count': count
        }
    return {
        'solicitudes_pendientes_count': 0
    }
