from django.conf.urls import url, include
from django.views.generic import TemplateView

from utils import user_is_student

from . import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='student_dashboard'),
    url(r'^train/$', views.dashboard),
    url(r'^test/finished/$', TemplateView.as_view(template_name="student/test/list_finished.haml"), name='student_test_finished'),
    url(r'^test/(?P<pk>\d+)/$', views.pass_test, name='student_pass_test'),
    url(r'^test/(?P<pk>\d+)/start/$', views.start_test, name='student_start_test'),
    url(r'^pedagogical/(?P<type>.+)/(?P<id>.+)/rate/$', views.create_rate, name='create_rate'),
    url(r'^pedagogical/(?P<type>.+)/(?P<id>.+)/makerating/$', views.get_rate_vote, name='get_rate_vote'),
    url(r'^pedagogical/(?P<type>.+)/(?P<id>.+)/average/$', views.get_average, name='get_average'),
    url(r'^pedagogical/(?P<type>.+)/(?P<slug>[a-zA-Z0-9_-]+)/$', user_is_student(views.skill_pedagogic_ressources), name='student_skill_pedagogic_ressources'),

    url(r'^train/', include('train.urls')),
]
