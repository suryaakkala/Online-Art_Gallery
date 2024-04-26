# gallery/urls.py
from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordResetDoneView

urlpatterns = [
    path('', landing_page, name="landing_page"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('home/', home, name='home'),
    path('aboutus/', aboutus,name='aboutus'),
    path('artwork/<int:pk>/', ArtworkDetailView.as_view(), name='artwork-detail'),
    path('cart/', cart, name='cart'),
    path('add-to-cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    # path('remove-from-cart/<int:item_id>/', CartView.remove_from_cart(), name='remove_from_cart'),
    path('resetpwd/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/profile/', UserProfileView.as_view(), name='user-profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('allimages/', all_images, name='all_images'),
    path('upload/', upload_artwork, name='upload_artwork'),
]

