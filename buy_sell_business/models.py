from django.db import models


class Company_Details(models.Model):
    # section 1, main presentation
    name = models.CharField(max_length=150) #
    main_gallery = models.FileField(null=True, blank=True)
    photo_gallery = models.FileField(null=True, blank=True)

    # section 2, inside descriptions
    asking_price = models.CharField(max_length=15)
    cash_flow = models.CharField(max_length=15)
    gross_revenue = models.CharField(max_length=15)
    inventory = models.CharField(max_length=15)
    ebitda = models.CharField(max_length=15)
    established = models.CharField(max_length=15)
    ff_e = models.CharField(max_length=15)


    # section 3, important information under section 1
    descriptions = models.TextField()
    detailed_information = models.CharField(max_length=200),

    #section 4, listind_statics

    # section 5, map business location
    google_map = models.CharField(max_length=200)

    # DETAIL INFORMATION
    inventory_ins = models.CharField(max_length=200)
    real_estate = models.CharField(max_length=200)
    building_sf = models.CharField(max_length=200)
    employees = models.CharField(max_length=200)
    f_f_e = models.CharField(max_length=200)
    facilities = models.CharField(max_length=200)
    competition = models.CharField(max_length=200)
    growth_expansion = models.CharField(max_length=200)
    support_training = models.CharField(max_length=200)
    reason_selling = models.CharField(max_length=200)
    home_based = models.CharField(max_length=200)
    website = models.CharField(max_length=200)


# the consumer sees this after buy premium plan
class Listing_Statistics(models.Model):
    saved_this_listing = models.CharField(max_length=200)
    days_active_on_site = models.CharField(max_length=200)
    appeared_in_search = models.CharField(max_length=200)
    listing_detail_views = models.CharField(max_length=200)

# message for the buyer
class Contact_The_Seller(models.Model):
    full_name = models.CharField(max_length=200)
    your_phone = models.CharField(max_length=200)
    your_email = models.CharField(max_length=200)
    your_zip = models.CharField(max_length=200)
    amount_invest = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    send_newsletter = models.CharField(max_length=200)