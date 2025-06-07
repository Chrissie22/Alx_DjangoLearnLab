from django.urls import path
from .import views
from .views import list_books, LibraryDetailView
from .views import home

app_name = "relationship_app"
urlpatterns = [
    path('', home, name='home'),
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
]
