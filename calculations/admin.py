from django.contrib import admin
from .models import Relay, Transformer, TransmissionLine  # ... import your models

admin.site.register(Relay)
admin.site.register(Transformer)
admin.site.register(TransmissionLine)
# ... register other models
