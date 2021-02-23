from django.contrib import admin
from .models import m_vaccination_center
from .models import m_vaccination_center_history


admin.site.register(m_vaccination_center)
admin.site.register(m_vaccination_center_history)
