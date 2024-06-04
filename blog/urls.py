from django.urls import path
from django.views.decorators.cache import never_cache, cache_page

from blog.apps import BlogConfig
from blog.views import (MaterialCreateView, MaterialListView, MaterialDetailView,
                        MaterialUpdateView, MaterialDeleteView)

app_name = BlogConfig.name

urlpatterns = [
    path('create/', never_cache(MaterialCreateView.as_view()), name="create"),
    path('', cache_page(60)(MaterialListView.as_view()), name="list"),
    path('view/<int:pk>/', cache_page(60)(MaterialDetailView.as_view()), name="view"),
    path('edit/<int:pk>/', never_cache(MaterialUpdateView.as_view()), name="edit"),
    path('delete/<int:pk>/', never_cache(MaterialDeleteView.as_view()), name="delete"),
]
