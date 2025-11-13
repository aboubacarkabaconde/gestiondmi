"""
WSGI config for pme_manager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see:
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# ==========================
# 🔧 Configuration du chemin du projet
# ==========================
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_PATH = str(BASE_DIR)

# Ajout du projet au sys.path (utile sur PythonAnywhere ou WSGI classique)
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)

# ==========================
# 🧩 Définition du module de configuration Django
# ==========================
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pme_manager.settings")

# ==========================
# 🚀 Application WSGI
# ==========================
application = get_wsgi_application()
