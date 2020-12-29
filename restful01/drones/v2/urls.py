from django.conf.urls import url
from .. import views
from . import views as view_v2

urlpatterns = [
    url(r'^vehicle-categories/$',
        views.DroneCategoryList.as_view(),
        name=views.DroneCategoryList.name),
    url(r'^vehicle-categories/(?P<PK>[0-9]+)$',
        views.DroneCategoryDetail.as_view(),
        name=views.DroneCategoryDetail.name),
    url(r'^vehicles/$',
        views.DroneList.as_view(),
        name=views.DroneList.name),
    url(r'^vehicles/(?P<pk>[0-9]+)$',
        views.DroneDetail.as_view(),
        name=views.DroneDetail.name),
    url(r'^pilots/$',
        views.PilotList.as_view(),
        name=views.PilotList.name),
    url(r'^pilots/(?P<pk>[0-9]+)$',
        views.PilotDetail.as_view(),
        name=views.PilotDetail.name),
    url(r'^competitions/$',
        views.CompetitionList.as_view(),
        name=views.CompetitionList.name),
    url(r'^competitions/(?P<pk>[0-9]+)$',
        views.CompetitionDetail.as_view(),
        name=views.CompetitionDetail.name),
    url(r'^$',
        view_v2.ApiRootVersion2.as_view(),
        name=view_v2.ApiRootVersion2.name)


]
