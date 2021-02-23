from django.urls import path,include
from vaccination import views 
 
urlpatterns = [ 
    path('',views.apiOverview),
    path('vaccenters/new_vac_centers', views.m_vaccination_center_list),
    path('vaccenters/update_vac_centers/<str:code>', views.update_vac_center_status),
    path('vaccenters/vac_centre_approvals/<int:workflow_seq_no>/<str:user_id>/', views.vaccination_center_approval),
    path('vaccenters/<str:code>', views.m_vaccination_center_code),
    path('vaccenters_zip_code/<str:zip_code>', views.m_vaccination_center_zip_code),
    path('vaccenters_key_level_2/<str:key_level2_jurisdiction_code>', views.m_vaccination_center_key_level2),   
    path('vaccenters_key_level_1/<str:key_level1_jurisdiction_code>', views.m_vaccination_center_key_level1),
    path('vaccenters_ou_code/<str:ou_code>', views.m_vaccination_center_ou_code),
    path('vaccenters_admin_code/<str:admin_code>', views.m_vaccination_center_admin_code),   
    path('vaccenters/history', views.m_vaccination_center_history_list),
]
