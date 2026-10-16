from django.db import models


class Bloque(models.Model):
    """
    Bloque temático oficial de la oposición (Ej: I. Organización del Estado)
    """
    numero = models.PositiveIntegerField(unique=True, help_text="Número de Bloque (1, 2, 3, 4)")
    nombre = models.CharField(max_length=200, help_text="Nombre oficial del bloque")
    descripcion = models.TextField(blank=True)
    icono = models.CharField(max_length=50, default='bi-folder', help_text="Clase de icono Bootstrap Icons (ej: bi-shield-check)")

    class Meta:
        verbose_name = "Bloque"
        verbose_name_plural = "Bloques"
        ordering = ['numero']

    def __str__(self):
        return f"Bloque {self.numero}: {self.nombre}"


class Tema(models.Model):
    """
    Tema oficial del programa TAI
    """
    bloque = models.ForeignKey(Bloque, on_delete=models.CASCADE, related_name='temas')
    numero = models.PositiveIntegerField(help_text="Número de tema dentro del bloque o general")
    titulo = models.CharField(max_length=255, help_text="Título oficial del tema")
    descripcion = models.TextField(blank=True)
    resumen_estudio = models.TextField(blank=True, help_text="Desarrollo ejecutivo de alto impacto del tema (máx 2 páginas)")
    
    # Trazabilidad Oficial (Principio 2)
    fuente_oficial = models.CharField(max_length=255, default='BOE / INAP', help_text="Organismo emisor o norma (BOE, INAP, CCN-CERT)")
    url_oficial = models.URLField(blank=True, help_text="Enlace a la fuente original oficial")
    fecha_consulta = models.DateField(null=True, blank=True)
    ultima_revision = models.DateField(auto_now=True)
    version_normativa = models.CharField(max_length=100, blank=True, help_text="Versión o estado normativo consolidado")

    class Meta:
        verbose_name = "Tema"
        verbose_name_plural = "Temas"
        ordering = ['bloque__numero', 'numero']
        unique_together = ('bloque', 'numero')

    def __str__(self):
        return f"B{self.bloque.numero}T{self.numero} - {self.titulo}"


class Subtema(models.Model):
    """
    Subtema o epígrafe dentro de un tema oficial
    """
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='subtemas')
    titulo = models.CharField(max_length=255)
    orden = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Subtema"
        verbose_name_plural = "Subtemas"
        ordering = ['tema', 'orden']

    def __str__(self):
        return f"{self.tema} > {self.titulo}"


class Concepto(models.Model):
    """
    Concepto atómico dentro de un subtema (Base de la tarjeta / 'Una idea')
    """
    subtema = models.ForeignKey(Subtema, on_delete=models.CASCADE, related_name='conceptos')
    titulo = models.CharField(max_length=255)
    contenido = models.TextField(help_text="Explicación detallada orientada a aprendizaje progresivo")
    resumen = models.TextField(blank=True, help_text="Resumen conciso (1 párrafo)")
    fuente_oficial = models.CharField(max_length=255, blank=True)
    url_fuente = models.URLField(blank=True)

    class Meta:
        verbose_name = "Concepto"
        verbose_name_plural = "Conceptos"

    def __str__(self):
        return f"{self.subtema.tema} - {self.titulo}"
