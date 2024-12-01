from django.urls import path
from .views import (
	ArticalListView,
	ArticalDetailView, 
	ArticalCreateView,
	ArticalDeleteView,
	# CommentCreateView,
	comment,
)

urlpatterns = [
	path('', ArticalListView.as_view(template_name='home/home.html'), name='home'),
	path('artical/<int:pk>/', ArticalDetailView.as_view(), name='artical_details'),
	path('artical/new_post/', ArticalCreateView.as_view(), name='artical_create'),
	path('artical/<int:pk>/delete', ArticalDeleteView.as_view(), name='artical_delete'),
	path('artical/<int:pk>/add_comment', comment, name='add_comment'),
]