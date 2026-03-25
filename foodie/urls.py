
from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="name"),
    path('contact/',views.contact_us, name="contact"),
    path('crud/',views.crud,name="crud"),
    path('cart/',views.add_cart,name="cart"),
    path('signup/',views.SignupPage,name="signup"),
    path('login/',views.LoginPage,name="login"),
    path('logout/',views.LogoutPage,name="logout"),
    path('show/',views.ShowAllProducts,name="showProducts"),
    path('dash/',views.dashboard,name="dash"),
    path('order/', views.orderdet, name="order"),
    path('about/', TemplateView.as_view(template_name='abooutus.html'), name="aboutus"),
    path('payment/', TemplateView.as_view(template_name='payment.html'), name="payment"),
   
    path('',include('chat.urls')),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
