#gallery/views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import *
from django.contrib.auth.views import LoginView, PasswordResetView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from .forms import CustomUserCreationForm , ArtworkForm

def landing_page(request):
    return render(request, 'gallery/landingpage.html')

class UserProfileView(TemplateView):
    template_name = 'gallery/user_profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'user': request.user})

class CustomLoginView(LoginView):
    template_name = 'gallery/login.html'
    def get_success_url(self):
        # Define the URL to redirect to after login
        return reverse('home')
class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        # You can add any additional logic here if needed
        from django.contrib.auth import logout
        logout(request)
        return redirect('login')
import logging

logger = logging.getLogger(__name__)  
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'gallery/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        logger.debug(f'User {self.object.username} successfully signed up!')
        return response

class CustomPasswordResetView(PasswordResetView):
    template_name = 'gallery/password_reset.html'

class ArtworkListView(ListView):
    model = Artwork
    template_name = 'gallery/artwork_list.html'
    context_object_name = 'artworks'


class ArtworkDetailView(DetailView):
    model = Artwork
    template_name = 'gallery/artwork_detail.html'
    context_object_name = 'artwork'

@login_required(login_url='login')
def home(request):
    artworks = Artwork.objects.all()
    return render(request, 'gallery/home.html', {'artworks': artworks})

def aboutus(request):
    return render(request, 'gallery/aboutus.html')

def all_images(request):
    artworks = Artwork.objects.all()
    return render(request, 'gallery/all_images.html', {'artworks': artworks})

def upload_artwork(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page
    else:
        form = ArtworkForm()
    return render(request, 'gallery/upload_artwork.html', {'form': form})

def add_to_cart(request, artwork_id):
    if 'cart' not in request.session:
        request.session['cart'] = {}
    cart = request.session['cart']
    if artwork_id in cart:
        cart[artwork_id] += 1
    else:
        cart[artwork_id] = 1
    request.session.modified = True
    return redirect('cart')

def cart(request):
    cart_items = {}
    total_amount = 0
    for artwork_id, quantity in request.session.get('cart', {}).items():
        artwork = Artwork.objects.get(pk=artwork_id)
        cart_items[artwork] = quantity
        total_amount += artwork.price * quantity
    return render(request, 'gallery/cart.html', {'cart_items': cart_items, 'total_amount': total_amount})