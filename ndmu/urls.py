#####################################################################
from django.urls import path, include
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, GalleryListView, GalleryCreateView, GalleryHomeListView
from django.views.generic.base import RedirectView
#####################################################################


urlpatterns = [
	path('announcements/comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
	path('announcements/comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
	path('announcements/post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
	path('error-404-demo/', views.error_404_demo, name='error_404_demo'),
	#home tab
	path('home/', GalleryHomeListView.as_view(), name='ndmu-home'),
	path('', views.superhome, name="ndmu-superhome"),
	#########################################################################
	#about tab
    path('about/', views.about, name='ndmu-about'),
	path('about/history/', views.history, name='ndmu-history'),
	path('about/contact/', views.contact, name='ndmu-contact'),
	path('about/board-of-trustees/', views.trustees, name='ndmu-trustees'),
	path('about/administration/', views.administration, name='ndmu-administration'),
	path('about/vision-mission/', views.vision, name='ndmu-vision'),
	path('about/objectives/', views.objectives, name='ndmu-objectives'),
	path('about/core-values/', views.corevalues, name='ndmu-corevalues'),
	path('about/citation-and-awards/', views.citationsandawards, name='ndmu-citation'),
	path('about/core-values/', views.corevalues, name='ndmu-corevalues'),
	path('about/university-colors/', views.universitycolors, name='ndmu-colors'),
	path('about/university-hymn/', views.hymn, name='ndmu-hymn'),	
	path('about/university-seal/', views.seal, name='ndmu-seal'),
	path('about/marist-brothers/', views.maristbrothers, name='ndmu-brothers'),
	path('about/shs-strands/', views.strands, name='ndmu-strands'),
	path('about/school-facilities/', views.schoolfacilities, name='ndmu-facilities'),
	path('about/developers/', views.developers, name='ndmu-developers'),
    #########################################################################
    #announcements tab
	path('announcements/post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	path('announcements/post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('announcements/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('announcements/new/', PostCreateView.as_view(), name='post-create'),
    path('announcements/',  PostListView.as_view(), name='ndmu-announcements'),

    #########################################################################
    #user tag
	path('user/<username>/', UserPostListView.as_view(), name='user-posts'),
	#########################################################################
	#teacher tag
	path('shs-teachers/', views.teachers, name='ndmu-teachers'),
	#gallery
	path('gallery/', GalleryListView.as_view(), name='ndmu-gallery'),
	path('gallery/upload/', GalleryCreateView.as_view(), name='ndmu-gallery-upload'),

	path('game/', views.game, name='game-test'),
]
