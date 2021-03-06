from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from Events import views,classviews
from django.db.models import *


urlpatterns=[

    # url(r'^staff/(?P<id>[A-Za-z0-9]+)',views),
    # url(r'^$',views.dashboard),
    url(r'^$',classviews.dashboard.as_view(),name='dashboard'),
    url(r'^register_event/see/(?P<id>[A-Za-z0-9 -]+)',views.geteventcontent,name='eventdetail'),
    url(r'^register_event/see$',classviews.eventslist.as_view(),name='eventdata'),
    url(r'^register_event/$',login_required(views.get_eventregistrationform),name="event_registration"),
    url(r'^staff/(?P<id>[A-Za-z0-9 -]+)/view_events',views.getidcontent,name='eventslist'),
    url(r'^staff/all/$',classviews.facultylist.as_view(),name='facultydata'),
    url(r'^logout1$',views.logout1,name="logout"),
    url(r'^edit/(?P<id>[A-Za-z0-9 -]+)',views.editEvent,name="edit_event"),
    url(r'^end/(?P<pk>[A-Za-z0-9 -]+)',classviews.EndEvent.as_view(),name="end_event"),
    url(r'^delete/(?P<pk>[A-Za-z0-9 -]+)',classviews.EventDeleteView.as_view(),name="end_event"),
    url(r'^resources/(?P<date1>[0-9 -]+)',views.resview),

    #
    # url(r'^event_snippets/$',views.snippet_list),
    # url(r'^event_snippets/(?P<eventid>([A-Za-z0-9]|-)+)',views.snippet_detail),

]