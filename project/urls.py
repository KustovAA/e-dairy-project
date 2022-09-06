from django.urls import path

from datacenter import views

urlpatterns = [
    path('', views.view_classes, name='classes'),
    path('<int:year>/<letter>', views.view_class_info,
        name='class_info'),
    path('<int:year>/<letter>/schedule',
        views.view_schedule, name='schedule'),
    path('schoolkid/<schoolkid_id>', views.view_schoolkid,
        name='schoolkid'),
    path(
        'journal/<int:year>/<letter>/<subject_id>',
        views.view_journal,
        name='journal'
    ),
]
