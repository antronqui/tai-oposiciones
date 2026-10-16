# PROYECTO TAI 2027: Plataforma de Preparación para Técnico Auxiliar de Informática (AGE)

## 📌 Enfoque: MVP v1

El MVP se enfoca exclusivamente en la funcionalidad esencial para estudiar y preparar la oposición de forma estructurada:

1. **Importación del temario oficial TAI (Convocatoria de referencia 2026/vigente)**
   - Bloques oficiales:
     - Bloque I: Organización del Estado y Administración Pública.
     - Bloque II: Tecnología básica.
     - Bloque III: Desarrollo de sistemas.
     - Bloque IV: Sistemas y comunicaciones.
   - Trazabilidad oficial (BOE, INAP, Guías ENS/CCN-CERT).
2. **Banco de Exámenes Oficiales INAP**
   - Importación de exámenes pasados con preguntas oficiales y plantillas de soluciones.
   - Vinculación pregunta-tema.
3. **Sistema de Tarjetas de Estudio (Flashcards)**
   - Formato "Una idea por tarjeta".
   - Tipos: Definiciones, Fechas, Organismos, Procedimientos, Comparativas.
4. **Autenticación con Google y Control de Acceso**
   - Integración con `django-allauth` (Google OAuth2).
   - Acceso restringido por lista blanca/invitaciones.
5. **Planificación y Onboarding de Estudio**
   - Configuración inicial: Horas semanales, nivel, fecha objetivo.
   - Generación de plan y cálculo de progreso.
6. **Motor de Repetición Espaciada (Spaced Repetition System - SRS)**
   - Algoritmo de intervalos (1, 3, 7, 15, 30, 60 días).
   - Sesiones adaptativas por tiempo (15, 30, 45, 60 min).
7. **Despliegue y Arquitectura para PythonAnywhere**
   - Django 5.x + SQLite (fácil migración a MySQL / PostgreSQL).
   - Frontend responsive con Bootstrap 5 + Icons.
   - Configuración lista para WSGI en PythonAnywhere.
