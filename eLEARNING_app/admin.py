from django.contrib import admin
from .models import contact_form_tbl,About_Carousel_img,Order_Carousel_img,Contact_Carousel_img,Testimonial_Carousel_img,Team_Carousel_img,Courses_Carousel_img,About_Carousel,About_card,BookOrder_tbl,Coureses_list_tbl,Testimonial_tbl,contact_map_tbl,Our_team_tbl,Courses_tbl,Courses_Categories_tbl,About_tbl,About_features_tbl
# Register your models here.

class Admin_contact_form_tbl(admin.ModelAdmin):
    list_display=['username','password','confirm_password','age','contact']

admin.site.register(contact_form_tbl,Admin_contact_form_tbl)


class Admin_contact_map_tbl(admin.ModelAdmin):
    list_display=['contact_info','contact_map']

admin.site.register(contact_map_tbl,Admin_contact_map_tbl)

class Admin_Our_team_tbl(admin.ModelAdmin):
    list_display=['our_team_img','our_team_name','our_team_destination','our_team_f_link','our_team_t_link','our_team_i_link']
admin.site.register(Our_team_tbl,Admin_Our_team_tbl)

class Admin_Courses_tbl(admin.ModelAdmin):
    list_display=['courses_image','courses_price','courses_rating','courses_rating_count','courses_title','courses_instructor','courses_duration','courses_students']
admin.site.register(Courses_tbl,Admin_Courses_tbl)

class Admin_Courses_Categories_tbl(admin.ModelAdmin):
    list_display=['courses_categories_img1','courses_name1','courses_categories_img2','courses_name2','courses_categories_img3','courses_name3','courses_categories_img4','courses_name4']
admin.site.register(Courses_Categories_tbl,Admin_Courses_Categories_tbl)

class Admin_About_tbl(admin.ModelAdmin):
    list_display=['about_title','about_info1','about_info2','about_img']
admin.site.register(About_tbl,Admin_About_tbl)

class Admin_About_features_tbl(admin.ModelAdmin):
    list_display=['About_features']
admin.site.register(About_features_tbl,Admin_About_features_tbl)

class Admin_About_card(admin.ModelAdmin):
    list_display=['card_title','card_info','card_icon']
admin.site.register(About_card,Admin_About_card)

class Admin_Testimonial_tbl(admin.ModelAdmin):
    list_display=['client_name1','profession1','message1','image1','client_name2','profession2','message2','image2','client_name3','profession3','message3','image3']
admin.site.register(Testimonial_tbl,Admin_Testimonial_tbl)


class Admin_BookOrder_tbl(admin.ModelAdmin):
    list_display=['name','email','password','select_book','quantity','delivery_date','address','payment_method']
admin.site.register(BookOrder_tbl,Admin_BookOrder_tbl)

class Admin_Coureses_list_tbl(admin.ModelAdmin):
    list_display=['courses_list1','courses_list2','courses_list3','courses_list4']
admin.site.register(Coureses_list_tbl,Admin_Coureses_list_tbl)

class Admin_About_Carousel(admin.ModelAdmin):
    list_display=['Carousel_title','Carousel_subtitle','Carousel_description','Carousel_image']
admin.site.register(About_Carousel,Admin_About_Carousel)



class Admin_About_Carousel_img(admin.ModelAdmin):
    list_display=['image']
admin.site.register(About_Carousel_img,Admin_About_Carousel_img)

class Admin_Courses_Carousel_img(admin.ModelAdmin):
    list_display=['image']
admin.site.register(Courses_Carousel_img,Admin_Courses_Carousel_img)

class Admin_Team_Carousel_img(admin.ModelAdmin):
    list_display=['image']
admin.site.register(Team_Carousel_img,Admin_Team_Carousel_img)

class Admin_Testimonial_Carousel_img(admin.ModelAdmin):
    list_display=['image']
admin.site.register(Testimonial_Carousel_img,Admin_Testimonial_Carousel_img)

class Admin_Contact_Carousel_img(admin.ModelAdmin):
    list_display=['image']
admin.site.register(Contact_Carousel_img,Admin_Contact_Carousel_img)

class Admin_Order_Carousel_img(admin.ModelAdmin):
    list_display=['image']
admin.site.register(Order_Carousel_img,Admin_Order_Carousel_img)