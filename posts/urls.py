from django.urls import path
from posts.views import hello, get_index, get_contacts, get_about, get_post, create_post, update_post

urlpatterns = [
    path('hello/', hello, name='hello-views'),
    path("", get_index ,name="index-page"),
    path("contacts/", get_contacts ,name="contacts-page"),
    path("about/", get_about ,name="about-page"),
    path("details/", get_post ,name=None),
    path("update/", update_post ,name=None),
    path("create/", create_post ,name=None),

]