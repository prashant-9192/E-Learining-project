from django.db import models

# Create your models here.

class contact_form_tbl(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    age=models.IntegerField()
    contact=models.IntegerField()

class contact_map_tbl(models.Model):
    contact_info=models.CharField(max_length=100)
    contact_map=models.CharField(max_length=500)


class Our_team_tbl(models.Model):
    our_team_img=models.ImageField(upload_to="static/img",null=True,default=None)
    our_team_f_link=models.CharField(max_length=100)
    our_team_t_link=models.CharField(max_length=100)
    our_team_i_link=models.CharField(max_length=100)
    our_team_name=models.CharField(max_length=100)
    our_team_destination=models.CharField(max_length=200)

class Courses_tbl(models.Model):
    courses_image=models.ImageField(upload_to="static/img",null=True,default=None)
    courses_price=models.IntegerField()
    courses_rating=models.IntegerField(default=5)
    courses_rating_count=models.IntegerField()
    courses_title=models.CharField(max_length=200)
    courses_instructor=models.CharField(max_length=100)
    courses_duration=models.CharField(max_length=20)
    courses_students=models.IntegerField()

class Courses_Categories_tbl(models.Model):
    courses_categories_img1=models.ImageField(upload_to="static/img",null=True,default=None)
    courses_name1 = models.CharField(max_length=100, default="Unknown")
    courses_categories_img2=models.ImageField(upload_to="static/img",null=True,default=None)
    courses_name2 = models.CharField(max_length=100, default="Unknown")
    courses_categories_img3=models.ImageField(upload_to="static/img",null=True,default=None)
    courses_name3 = models.CharField(max_length=100, default="Unknown")
    courses_categories_img4=models.ImageField(upload_to="static/img",null=True,default=None)
    courses_name4 = models.CharField(max_length=100, default="Unknown")

class Coureses_list_tbl(models.Model):
    courses_list1=models.CharField(max_length=100)
    courses_list2=models.CharField(max_length=100)
    courses_list3=models.CharField(max_length=100)
    courses_list4=models.CharField(max_length=100)



class About_tbl(models.Model):
    about_title=models.CharField(max_length=100)
    about_info1=models.CharField(max_length=200)
    about_info2=models.CharField(max_length=200)
    about_img=models.ImageField(upload_to="static/img",null=True,default=None)

class About_features_tbl(models.Model):
    About_features=models.CharField(max_length=100)

class About_card(models.Model):
    card_title=models.CharField(max_length=100)
    card_info=models.CharField(max_length=500)
    card_icon=models.CharField(max_length=100)


class Testimonial_tbl(models.Model):
    client_name1 = models.CharField(max_length=50, null=True, blank=True, default="")
    profession1 = models.CharField(max_length=50, null=True, blank=True, default="")
    message1 = models.CharField(max_length=200, null=True, blank=True, default="")
    image1 = models.ImageField(upload_to="static/img", null=True, blank=True, default=None)

    client_name2 = models.CharField(max_length=50, null=True, blank=True, default="")
    profession2 = models.CharField(max_length=50, null=True, blank=True, default="")
    message2 = models.CharField(max_length=200, null=True, blank=True, default="")
    image2 = models.ImageField(upload_to="static/img", null=True, blank=True, default=None)

    client_name3 = models.CharField(max_length=50, null=True, blank=True, default="")
    profession3 = models.CharField(max_length=50, null=True, blank=True, default="")
    message3 = models.CharField(max_length=200, null=True, blank=True, default="")
    image3 = models.ImageField(upload_to="static/img", null=True, blank=True, default=None)


class BookOrder_tbl(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    select_book=models.CharField(max_length=100,choices=[("Learn HTML & CSS", "Learn HTML & CSS"),("JavaScript Essentials", "JavaScript Essentials"),("Mastering Photoshop", "Mastering Photoshop"),("UI/UX Design Guide", "UI/UX Design Guide"),("Illustrator for Beginners", "Illustrator for Beginners"),])
    quantity=models.IntegerField()
    delivery_date=models.DateField()
    address=models.CharField(max_length=255)
    payment_method=models.CharField(max_length=100,choices=[("UPI", "UPI"),("Cash On Delivery", "Cash On Delivery"),("Credit/Debit Card", "Credit/Debit Card"),])

class About_Carousel(models.Model):
    Carousel_title=models.CharField(max_length=200)
    Carousel_subtitle=models.CharField(max_length=300, blank=True, null=True)
    Carousel_description=models.CharField(max_length=500)
    Carousel_image=models.ImageField(upload_to="static/img", null=True, blank=True, default=None)
    
class About_Carousel_img(models.Model):
    image=models.ImageField(upload_to="static/img", null=True, blank=True, default=None)

class Courses_Carousel_img(models.Model):
    image=models.ImageField(upload_to="static/img", null=True, blank=True, default=None)

class Team_Carousel_img(models.Model):
    image=models.ImageField(upload_to="static/img", null=True, blank=True, default=None)

class Testimonial_Carousel_img(models.Model):
    image=models.ImageField(upload_to="static/img", null=True, blank=True, default=None)

class Contact_Carousel_img(models.Model):
    image=models.ImageField(upload_to="static/img", null=True, blank=True, default=None)

class Order_Carousel_img(models.Model):
    image=models.ImageField(upload_to="static/img", null=True, blank=True, default=None)
    
      
