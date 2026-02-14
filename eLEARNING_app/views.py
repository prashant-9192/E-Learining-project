from django.shortcuts import render,redirect
from .models import contact_form_tbl,Coureses_list_tbl,Order_Carousel_img,About_Carousel_img,Testimonial_Carousel_img,Team_Carousel_img,Courses_Carousel_img,Contact_Carousel_img,About_tbl,About_Carousel,About_card,Coureses_list_tbl,BookOrder_tbl,About_features_tbl,contact_map_tbl,Our_team_tbl,Courses_tbl,Courses_Categories_tbl,Testimonial_tbl

# Create your views here.
def Home_Page_View(request):
    about_data=About_tbl.objects.first()
    about_features_data=About_features_tbl.objects.all()
    our_team_data=Our_team_tbl.objects.all()
    courses_data = Courses_tbl.objects.all()
    courses_categories_data=Courses_Categories_tbl.objects.first()
    About_card_data=About_card.objects.all()
    testimonial_data=Testimonial_tbl.objects.all()
    About_Carousel_data=About_Carousel.objects.all()
    courses_list_data=Coureses_list_tbl.objects.all()
    return render(request,'index.html',{'courses_list_data':courses_list_data,'About_Carousel_data':About_Carousel_data,'testimonial_data':testimonial_data,'About_card_data':About_card_data,'courses_categories_data':courses_categories_data,'courses_data':courses_data,'about_data':about_data,'about_features_data':about_features_data,'our_team_data':our_team_data})


def About_Page_View(request):
    about_data=About_tbl.objects.first()
    about_features_data=About_features_tbl.objects.all()
    our_team_data=Our_team_tbl.objects.all()
    About_card_data=About_card.objects.all()
    About_Carousel_img_data=About_Carousel_img.objects.first()
    return render(request, 'about.html',{'About_Carousel_img_data':About_Carousel_img_data,'About_card_data':About_card_data,'our_team_data':our_team_data,'about_data': about_data,'about_features_data': about_features_data})

def Contact_Page_View(request):
    contact_data=contact_map_tbl.objects.first()
    Contact_Carousel_img_data=Contact_Carousel_img.objects.first()
    if request.method=="GET":
        return render(request,'contact.html',{'Contact_Carousel_img_data':Contact_Carousel_img_data,'contact_data':contact_data})

    else:
        contact_form_tbl(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            confirm_password=request.POST.get('confirm_password'),
            age=request.POST.get('age'),
            contact=request.POST.get('contact'),
            ).save()

        return redirect('contact')
    


def Courses_Page_View(request):
    courses_data = Courses_tbl.objects.all()
    courses_list_data=Coureses_list_tbl.objects.all()
    courses_categories_data=Courses_Categories_tbl.objects.first()
    testimonial_data=Testimonial_tbl.objects.all()
    Courses_Carousel_img_data=Courses_Carousel_img.objects.first()
    return render(request, 'courses.html', {
        'courses_data': courses_data,
        'courses_categories_data': courses_categories_data,
        'courses_list_data':courses_list_data,
        'testimonial_data':testimonial_data,
        'Courses_Carousel_img_data':Courses_Carousel_img_data
    })

def Order_Page_View(request):
    Order_Carousel_img_data=Order_Carousel_img.objects.first()
    if request.method=="GET":
        return render(request,'Order.html',{'Order_Carousel_img_data':Order_Carousel_img_data})
    else:
        BookOrder_tbl(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
            select_book=request.POST.get('select_book'),
            quantity=request.POST.get('quantity'),
            delivery_date=request.POST.get('delivery_date'),
            address=request.POST.get('address'),
            payment_method=request.POST.get('payment_method')
            ).save()
        return redirect('Order')
    

def Our_Team_Page_View(request):
    our_team_data=Our_team_tbl.objects.all()
    Team_Carousel_img_data=Team_Carousel_img.objects.first()

    return render(request,'our_team.html',{'Team_Carousel_img_data':Team_Carousel_img_data,'our_team_data':our_team_data})
    
def Page_View(request):
    return render(request,'page.html')

def show_order_Page_View(request):
    return render(request,'show-order.html')

def Testimonial_Page_View(request):
    testimonial_data=Testimonial_tbl.objects.all()
    Testimonial_Carousel_img_data=Testimonial_Carousel_img.objects.first()
    return render(request,'testimonial.html',{'Testimonial_Carousel_img_data':Testimonial_Carousel_img_data,'testimonial_data':testimonial_data})

