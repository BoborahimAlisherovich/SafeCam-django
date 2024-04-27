from django.urls import path
from .views import home_view,about_view,blog_view,contact_view,detail_view,price_view,service_view,team_view,testimonial_view



urlpatterns = [
    path('',home_view, name="home-page"),
    path('about/',about_view, name="about-page"),
    path('blog/',blog_view, name="blog-page"),
    path('contact/',contact_view, name="contact-page"),
    path('detail/',detail_view, name="detail-page"),
    path('price/',price_view, name="price-page"),
    path('service/',service_view, name="service-page"),
    path('team/',team_view, name="team-page"),

    path('testimonial/',testimonial_view, name="testimonial-page"),


]