from rest_framework import serializers 
from .models import m_vaccination_center
from .models import m_vaccination_center_history


class m_vaccination_centerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = m_vaccination_center 
        fields = '__all__'
   
class m_vaccination_center_historySerializer(serializers.ModelSerializer):
    class Meta:
        model = m_vaccination_center_history
        fields='__all__'
   
