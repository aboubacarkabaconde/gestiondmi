"""
ASGI config for pme_manager project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see:
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from pathlib import Path
import sys
from django.core.asgi import get_asgi_application

# ==========================
# 🔧 Configuration du chemin du projet
# ==========================
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_PATH = str(BASE_DIR)

# Ajout du dossier du projet dans le sys.path (utile sous Docker/PythonAnywhere)
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)

# ==========================
# 🧩 Module de configuration Django
# ==========================
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pme_manager.settings")

# ==========================
# 🚀 Application ASGI
# ==========================
application = get_asgi_application()

"""from channels.routing import ProtocolTypeRouter, URLRouter
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # "websocket": AuthMiddlewareStack(URLRouter(...))
})"""