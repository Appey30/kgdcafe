from django.db import models
from django.contrib.auth.models import User
import psycopg2
from django.utils import timezone
from datetime import datetime
import pytz
#from django.db.models.manager import Manager as GeoManager

# Create your models here.
class Brandcolor(models.Model):
    user = models.IntegerField(blank=True, null=True, default='2')
    text = models.CharField(max_length=7, blank=True, null=True, default='#2c170c')
    button = models.CharField(max_length=7, blank=True, null=True, default='#aa5c31')
    container = models.CharField(max_length=7, blank=True, null=True, default='#d4ad98')
    background = models.CharField(max_length=7, blank=True, null=True, default='#f6eeea')
    identifier = models.CharField(max_length=50, blank=True, null=True, default='#2c170c#aa5c31#d4ad98#f6eeea')

    def __str__(self):
        return str(self.identifier) + " / " + str(self.user)


class ButtonColor(models.Model):
    user = models.IntegerField(blank=True, null=True, default='2')
    color = models.CharField(max_length=7, default='#aa5c31')
    cardcolor = models.CharField(max_length=7, default='#d4ad98')
    textcolor = models.CharField(max_length=7, default='#2c170c')
    backgroundcolor = models.CharField(max_length=7, default='#f6eeea')
    brandname = models.CharField(max_length=50, blank=True, null=True, default='')
    title = models.CharField(max_length=50, blank=True, null=True, default='Black Jack Script')
    subtitle = models.CharField(max_length=50, blank=True, null=True, default='Black Jack Script')
    body = models.CharField(max_length=50, blank=True, null=True, default='sans-serif')
    title_bold = models.CharField(max_length=10, blank=True, null=True, default='')
    title_italic = models.CharField(max_length=10, blank=True, null=True, default='')
    title_underline = models.CharField(max_length=10, blank=True, null=True, default='')
    subtitle_bold = models.CharField(max_length=10, blank=True, null=True, default='')
    subtitle_italic = models.CharField(max_length=10, blank=True, null=True, default='')
    subtitle_underline = models.CharField(max_length=10, blank=True, null=True, default='')
    body_bold = models.CharField(max_length=10, blank=True, null=True, default='')
    body_italic = models.CharField(max_length=10, blank=True, null=True, default='')
    body_underline = models.CharField(max_length=10, blank=True, null=True, default='')

    def __str__(self):
        return str(self.color) + " / " + str(self.user)

class Subcategories(models.Model):
    Subcategorychoices = models.CharField(max_length = 50, blank = False, null = False, default='')
    def __str__(self):
        return str(self.Subcategorychoices)

class Categories(models.Model):
    Categorychoices = models.CharField(max_length = 50, blank = False, null = False, default='')
    def __str__(self):
        return str(self.Categorychoices)

class Sizes(models.Model):
    Sizechoices = models.CharField(max_length=50, blank = False, null = False, default='')
    def __str__(self):
        return str(self.Sizechoices)

class PSizes(models.Model):
    PSizechoices = models.CharField(max_length=50, blank = False, null = False, default='')
    def __str__(self):
        return str(self.PSizechoices)


class user1 (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,blank = False, null = False)
    productname = models.CharField(max_length = 250, blank = False, null = False, default='')
    Category = models.ForeignKey(Categories, on_delete=models.CASCADE, default='',blank = True, null = True)
    Subcategory = models.ForeignKey(Subcategories, on_delete=models.CASCADE, default='',blank = True, null = True)
    Size = models.ForeignKey(Sizes, on_delete = models.CASCADE, default = '',blank = True, null = True)
    PSize = models.ForeignKey(PSizes, on_delete = models.CASCADE, default = '',blank = True, null = True)
    Price = models.IntegerField(blank = False, null = False, default='')
    Cost = models.DecimalField(decimal_places=2,max_digits = 7,blank = False, null = False, default='0.00')
    Qty = models.IntegerField(blank = False, null = False, default='1')
    Promo = models.CharField(max_length = 50, blank = True, null = True, default='')
    PDescription = models.CharField(max_length = 2000, blank = True, null = True, default='')
    def __str__(self):
        return str(self.productname) +" "+ str(self.Size)

class CategoriesCoupon(models.Model):
    CategoryCouponchoices = models.CharField(max_length = 50, blank = False, null = False, default='')
    def __str__(self):
        return str(self.CategoryCouponchoices)

class couponlist (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,blank = False, null = False)
    couponname = models.CharField(max_length = 250, blank = False, null = False, default='')
    category = models.ForeignKey(CategoriesCoupon, on_delete=models.CASCADE, default='',blank = True, null = True)
    code = models.CharField(max_length = 250, blank = False, null = False, default='')
    url = models.CharField(max_length = 1000, blank = False, null = False, default='')

    pieces = models.IntegerField(blank = True, null = True, default='')
    discountamount = models.IntegerField(blank = True, null = True, default='')
    is_withMinimumAmount = models.BooleanField(default = False, blank = True, null = True)
    is_consumable = models.BooleanField(default = False, blank = True, null = True)
    redeemlimit = models.IntegerField(blank = True, null = True, default=0)
    #redeemlimit is the same with redeemnumber
    is_active = models.BooleanField(default = False, blank = True, null = True)
    MinimumAmount = models.IntegerField(blank = True, null = True, default='')

    def __str__(self):
        if self.redeemlimit == 0:
            Redeem = "Redeemed"
        else:
            Redeem = "Not yet Redeemed"
        if self.is_active == "True":
            Active = "Active"
        else:
            Active = "Not Active"
        return str(self.couponname) +" / "+ str(self.category) + " / "+ Redeem + " / "+ Active
      


class punchedprod (models.Model):
    user=models.IntegerField(blank = True, null = True, default='2')
    productname = models.CharField(max_length = 250, blank = True, null = True, default='')
    Category = models.CharField(max_length = 50, blank = True, null = True, default='')
    Subcategory = models.CharField(max_length = 50, default='',blank = True, null = True)
    Size = models.CharField(max_length = 50, default = '',blank = True, null = True)
    PSize = models.CharField(max_length = 50, default = '',blank = True, null = True)
    Price = models.IntegerField(blank = True, null = True, default='')
    Subtotal = models.IntegerField(blank = True, null = True, default='')
    Cost = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Qty = models.IntegerField(blank = True, null = True, default='')
    DateTime= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.productname) +" "+ str(self.Size) +" "+ str(self.PSize)

class punchedprodso (models.Model):
    user=models.IntegerField(blank = True, null = True, default='2')
    productname = models.CharField(max_length = 250, blank = True, null = True, default='')
    Category = models.CharField(max_length = 50, blank = True, null = True, default='')
    Subcategory = models.CharField(max_length = 50, default='',blank = True, null = True)
    Size = models.CharField(max_length = 50, default = '',blank = True, null = True)
    PSize = models.CharField(max_length = 50, default = '',blank = True, null = True)
    Price = models.IntegerField(blank = True, null = True, default='')
    Subtotal = models.IntegerField(blank = True, null = True, default='')
    Cost = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Qty = models.IntegerField(blank = True, null = True, default='')
    DateTime= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.productname) +" "+ str(self.Size) +" "+ str(self.PSize)

class queue1 (models.Model):
    user=models.IntegerField(blank = True, null = True, default='2')
    productname = models.CharField(max_length = 250, blank = True, null = True, default='')
    Category = models.CharField(max_length = 50, blank = True, null = True, default='')
    Subcategory = models.CharField(max_length = 50, default='',blank = True, null = True)
    Size = models.CharField(max_length = 50, default = '',blank = True, null = True)
    PSize = models.CharField(max_length = 50, default = '',blank = True, null = True)
    Price = models.IntegerField(blank = True, null = True, default='')
    Subtotal = models.IntegerField(blank = True, null = True, default='')
    Cost = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Qty = models.IntegerField(blank = True, null = True, default='')
    Bill= models.IntegerField(blank = True, null = True, default='0')
    Change= models.IntegerField(blank = True, null = True, default='0')
    CusName=models.CharField(max_length = 50, blank = True, null = True, default='')
    DateTime= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.productname) +" "+ str(self.Size) +" "+ str(self.PSize)+" "+ str(self.CusName)


class queue2 (models.Model):
    user=models.IntegerField(blank = True, null = True, default='2')
    productname = models.CharField(max_length = 250, blank = True, null = True, default='')
    Category = models.CharField(max_length = 50, blank = True, null = True, default='')
    Subcategory = models.CharField(max_length = 50, default='',blank = True, null = True)
    Size = models.CharField(max_length = 50, default = '',blank = True, null = True)
    PSize = models.CharField(max_length = 50, default = '',blank = True, null = True)
    Price = models.IntegerField(blank = True, null = True, default='')
    Subtotal = models.IntegerField(blank = True, null = True, default='')
    Cost = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Qty = models.IntegerField(blank = True, null = True, default='')
    Bill= models.IntegerField(blank = True, null = True, default='0')
    Change= models.IntegerField(blank = True, null = True, default='0')
    CusName=models.CharField(max_length = 50, blank = True, null = True, default='')
    DateTime= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.productname) +" "+ str(self.Size) +" "+ str(self.PSize)+" "+ str(self.CusName)


class queue3 (models.Model):
    user=models.IntegerField(blank = True, null = True, default='2')
    productname = models.CharField(max_length = 250, blank = True, null = True, default='')
    Category = models.CharField(max_length = 50, blank = True, null = True, default='')
    Subcategory = models.CharField(max_length = 50, default='',blank = True, null = True)
    Size = models.CharField(max_length = 50, default = '',blank = True, null = True)
    PSize = models.CharField(max_length = 50, default = '',blank = True, null = True)
    Price = models.IntegerField(blank = True, null = True, default='')
    Subtotal = models.IntegerField(blank = True, null = True, default='')
    Cost = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Qty = models.IntegerField(blank = True, null = True, default='')
    Bill= models.IntegerField(blank = True, null = True, default='0')
    Change= models.IntegerField(blank = True, null = True, default='0')
    CusName=models.CharField(max_length = 50, blank = True, null = True, default='')
    DateTime= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.productname) +" "+ str(self.Size) +" "+ str(self.PSize)+" "+ str(self.CusName)
class saesubcate(models.Model):
    saesubcatchoices = models.CharField(max_length=50, blank = False, null = False, default='')
    def __str__(self):
        return str(self.saesubcatchoices)
class saesubcats(models.Model):
    saesubcatchoices = models.CharField(max_length=50, blank = False, null = False, default='')
    def __str__(self):
        return str(self.saesubcatchoices)
        
class saecat(models.Model):
    saecatchoices = models.CharField(max_length=50, blank = False, null = False, default='')
    def __str__(self):
        return str(self.saecatchoices)
        
class Sales (models.Model):
    user=models.IntegerField(blank = True, null = True, default='2')
    productname = models.CharField(max_length = 250, blank = True, null = True, default='')
    Category = models.CharField(max_length = 50, blank = True, null = True, default='')
    Subcategory = models.CharField(max_length = 50, default='',blank = True, null = True)
    Size = models.CharField(max_length = 50, default = '',blank = True, null = True)
    PSize = models.CharField(max_length = 50, default = '',blank = True, null = True)
    Price = models.IntegerField(blank = True, null = True, default='0')
    Subtotal=models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    GSubtotal = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Cost = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Qty = models.IntegerField(blank = True, null = True, default='0')
    Addons = models.CharField(max_length = 50, default = '',blank = True, null = True)
    QtyAddons = models.IntegerField(blank = True, null = True, default='0')
    Bill= models.IntegerField(blank = True, null = True, default='0')
    Change= models.IntegerField(blank = True, null = True, default='0')
    MOP = models.CharField(max_length = 50, default = '',blank = True, null = True)
    ordertype=models.CharField(max_length = 50, blank = True, null = True, default='Offline')
    gpslat = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    gpslng = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    gpsaccuracy = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    pinnedlat = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    pinnedlng = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00') 
    Province = models.CharField(max_length = 50, blank = True, null = True, default='')
    MunicipalityCity = models.CharField(max_length = 50, blank = True, null = True, default='')
    Barangay = models.CharField(max_length = 50, blank = True, null = True, default='')
    StreetPurok = models.CharField(max_length = 50, blank = True, null = True, default='')
    Housenumber=models.CharField(max_length = 50, blank = True, null = True, default='')
    LandmarksnNotes=models.CharField(max_length = 2000, blank = True, null = True, default='')
    ScheduleTime = models.CharField(max_length = 50, blank = True, null = True, default='')
    Timetodeliver = models.CharField(max_length = 50, blank = True, null = True, default='')
    DeliveryFee=models.IntegerField(blank = True, null = True, default='0')
    contactnumber=models.BigIntegerField(blank = True, null = True, default='09000000000')
    CusName=models.CharField(max_length = 250, blank = True, null = True, default='')
    codecoupon=models.CharField(max_length = 250, blank = True, null = True, default='')
    discount=models.CharField(max_length = 250, blank = True, null = True, default='')
    RequiredMinimumAmount=models.IntegerField(blank = True, null = True, default='0')
    Categoryaes = models.ForeignKey(saecat, on_delete = models.CASCADE, default = '',blank = True, null = True)
    Subcategorys = models.ForeignKey(saesubcats, on_delete = models.CASCADE, default = '',blank = True, null = True)
    Subcategorye = models.ForeignKey(saesubcate, on_delete = models.CASCADE, default = '',blank = True, null = True)
    Amount = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Description = models.CharField(max_length = 50, blank = True, null = True, default='')
    Receipt = models.ImageField(upload_to='Receipt/%Y/%m/%d',blank = True, null = True)
    tokens= models.CharField(max_length = 300, blank = True, null = True, default='')
    DateTime= models.DateTimeField(default=timezone.now)
    def __str__(self):
        monthconvert=['January','February','March','April','May','June','July','August','September','October','November','December',]
        Monthidentifier=monthconvert[int(self.DateTime.strftime('%m'))-1]
        return Monthidentifier +" "+str(self.DateTime.strftime('%d')) +", "+str(self.DateTime.strftime('%Y'))+"   // "+str(self.user) +" "+ str(self.productname) +" "+ str(self.Size) +" "+ str(self.PSize)+" "+ str(self.CusName)+" "+str(self.Categoryaes)
        
class Dailysales (models.Model):
    user=models.IntegerField(blank = True, null = True, default='2')
    DateTime= models.DateTimeField(default=timezone.now)
    Sales= models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Expenses= models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Startstocks=models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Endstocks=models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Valuestocks=models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Net= models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')

    def __str__(self):
        return str(self.Net)

class submitstockorder (models.Model):
    user=models.IntegerField(blank = True, null = True, default='2')
    productname = models.CharField(max_length = 100, blank = True, null = True, default='')
    Category = models.CharField(max_length = 50, blank = True, null = True, default='')
    Price = models.IntegerField(blank = True, null = True, default='0')
    Subtotal = models.IntegerField(blank = True, null = True, default='0')
    Cost = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Qty = models.IntegerField(blank = True, null = True, default='0')
    CusName=models.CharField(max_length = 50, blank = True, null = True, default='')
    DeliveryAddress=models.CharField(max_length = 100, blank = True, null = True, default='')
    ShippingFee=models.IntegerField(blank = True, null = True, default='0')
    contactnumber=models.BigIntegerField(blank = True, null = True, default='09000000000')
    DateTime= models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.productname) +" "+ str(self.CusName)
        

class acknowledgedstockorder (models.Model):
    user=models.IntegerField(blank = True, null = True, default='2')
    productname = models.CharField(max_length = 100, blank = True, null = True, default='')
    Category = models.CharField(max_length = 50, blank = True, null = True, default='')
    Price = models.IntegerField(blank = True, null = True, default='0')
    Subtotal = models.IntegerField(blank = True, null = True, default='0')
    Cost = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Qty = models.IntegerField(blank = True, null = True, default='0')
    CusName=models.CharField(max_length = 50, blank = True, null = True, default='')
    DeliveryAddress=models.CharField(max_length = 100, blank = True, null = True, default='')
    ShippingFee=models.IntegerField(blank = True, null = True, default='0')
    contactnumber=models.BigIntegerField(blank = True, null = True, default='09000000000')
    DateTime= models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.productname) +" "+ str(self.CusName)

class messengerbag(models.Model):
    fbid=models.BigIntegerField(blank = True, null = True, default=0)
    productname = models.CharField(max_length = 250, blank = True, null = True, default='')
    categ = models.CharField(max_length = 50, blank = True, null = True, default='')
    subcateg = models.CharField(max_length = 50, blank = True, null = True, default='')
    size = models.CharField(max_length = 50, default = '',blank = True, null = True)
    chosenitemprice = models.IntegerField(blank = True, null = True, default=0)
    qty = models.IntegerField(blank = True, null = True, default=0)
    subtotal = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default=0.00)
    def __str__(self):
        return str(self.productname) +" "+ str(self.fbid)

class Customer(models.Model):
    Admin=models.IntegerField(blank = True, null = True, default='2')
    Customername = models.CharField(max_length = 250, blank = True, null = True, default='')
    codecoupon=models.CharField(max_length = 250, blank = True, null = True, default='')
    discount=models.CharField(max_length = 250, blank = True, null = True, default='')
    Province = models.CharField(max_length = 50, blank = True, null = True, default='')
    MunicipalityCity = models.CharField(max_length = 50, blank = True, null = True, default='')
    Barangay = models.CharField(max_length = 250, blank = True, null = True, default='')
    StreetPurok = models.CharField(max_length = 50, blank = True, null = True, default='')
    Housenumber=models.CharField(max_length = 50, blank = True, null = True, default='')
    LandmarksnNotes=models.CharField(max_length = 2000, blank = True, null = True, default='')
    DeliveryFee=models.IntegerField(blank = True, null = True, default='0')
    contactnumber=models.BigIntegerField(blank = True, null = True, default='09000000000')
    Bill=models.IntegerField(blank = True, null = True, default='0')
    Change= models.IntegerField(blank = True, null = True, default='0')
    productname = models.CharField(max_length = 250, blank = True, null = True, default='')
    Category = models.CharField(max_length = 50, blank = True, null = True, default='')
    Subcategory = models.CharField(max_length = 50, blank = True, null = True, default='')
    Size = models.CharField(max_length = 50, default = '',blank = True, null = True)
    Addons = models.CharField(max_length = 50, default = '',blank = True, null = True)
    QtyAddons = models.IntegerField(blank = True, null = True, default='0')
    PSize = models.CharField(max_length = 50, default = '',blank = True, null = True)
    Price = models.IntegerField(blank = True, null = True, default='0')
    Subtotal = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    GSubtotal = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Cost = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Qty = models.IntegerField(blank = True, null = True, default='0')
    MOP = models.CharField(max_length = 50, default = '',blank = True, null = True)
    ordertype = models.CharField(max_length = 50, default = '',blank = True, null = True)
    Timetodeliver = models.CharField(max_length = 50, default = '',blank = True, null = True)
    ScheduleTime = models.CharField(max_length = 50, default = '',blank = True, null = True)
    gpslat = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    gpslng = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    gpsaccuracy = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    pinnedlat = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    pinnedlng = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    tokens= models.CharField(max_length = 300, blank = True, null = True, default='')
    DateTime= models.DateTimeField(default=timezone.now)
    def __str__(self):

        return str(self.productname) +" / "+ str(self.Customername)+" / "+ str(self.Admin)+" / "+ str(self.Barangay)

class Acceptorder(models.Model):
    Admin=models.IntegerField(blank = True, null = True, default='2')
    Customername = models.CharField(max_length = 250, blank = True, null = True, default='')
    codecoupon=models.CharField(max_length = 250, blank = True, null = True, default='')
    discount=models.CharField(max_length = 250, blank = True, null = True, default='')
    Province = models.CharField(max_length = 50, blank = True, null = True, default='')
    MunicipalityCity = models.CharField(max_length = 50, blank = True, null = True, default='')
    Barangay = models.CharField(max_length = 50, blank = True, null = True, default='')
    StreetPurok = models.CharField(max_length = 50, blank = True, null = True, default='')
    Housenumber=models.CharField(max_length = 50, blank = True, null = True, default='')
    LandmarksnNotes=models.CharField(max_length = 2000, blank = True, null = True, default='')
    DeliveryFee=models.IntegerField(blank = True, null = True, default='0')
    Rider = models.CharField(max_length = 50, blank = True, null = True, default='')
    contactnumber=models.BigIntegerField(blank = True, null = True, default='09000000000')
    Bill=models.IntegerField(blank = True, null = True, default='0')
    Change= models.IntegerField(blank = True, null = True, default='0')
    ETA = models.CharField(max_length = 50, blank = True, null = True, default='')
    productname = models.CharField(max_length = 250, blank = True, null = True, default='')
    Category = models.CharField(max_length = 50, blank = True, null = True, default='')
    Subcategory = models.CharField(max_length = 50, blank = True, null = True, default='')
    Size = models.CharField(max_length = 50, default = '',blank = True, null = True)
    Addons = models.CharField(max_length = 50, default = '',blank = True, null = True)
    QtyAddons = models.IntegerField(blank = True, null = True, default='0')
    PSize = models.CharField(max_length = 50, default = '',blank = True, null = True)
    Price = models.IntegerField(blank = True, null = True, default='0')
    Subtotal = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    GSubtotal = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Cost = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Qty = models.IntegerField(blank = True, null = True, default='0')
    MOP = models.CharField(max_length = 50, default = '',blank = True, null = True)
    ordertype = models.CharField(max_length = 50, default = '',blank = True, null = True)
    Timetodeliver = models.CharField(max_length = 50, default = '',blank = True, null = True)
    ScheduleTime = models.CharField(max_length = 50, default = '',blank = True, null = True)
    gpslat = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    gpslng = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    gpsaccuracy = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    pinnedlat = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    pinnedlng = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    tokens= models.CharField(max_length = 300, blank = True, null = True, default='')
    DateTime= models.DateTimeField(default=timezone.now)
    def __str__(self):

        return str(self.productname) +" / "+ str(self.Customername)+" / "+ str(self.Admin)+" / "+ str(self.Barangay)
        
class Rejectorder(models.Model):
    Admin=models.IntegerField(blank = True, null = True, default='2')
    Customername = models.CharField(max_length = 50, blank = True, null = True, default='')
    codecoupon=models.CharField(max_length = 250, blank = True, null = True, default='')
    discount=models.CharField(max_length = 250, blank = True, null = True, default='')
    Province = models.CharField(max_length = 50, blank = True, null = True, default='')
    MunicipalityCity = models.CharField(max_length = 50, blank = True, null = True, default='')
    Barangay = models.CharField(max_length = 50, blank = True, null = True, default='')
    StreetPurok = models.CharField(max_length = 50, blank = True, null = True, default='')
    Housenumber=models.CharField(max_length = 50, blank = True, null = True, default='')
    LandmarksnNotes=models.CharField(max_length = 2000, blank = True, null = True, default='')
    DeliveryFee=models.IntegerField(blank = True, null = True, default='0')
    contactnumber=models.BigIntegerField(blank = True, null = True, default='09000000000')
    Bill=models.IntegerField(blank = True, null = True, default='0')
    Change= models.IntegerField(blank = True, null = True, default='0')
    productname = models.CharField(max_length = 250, blank = True, null = True, default='')
    Category = models.CharField(max_length = 50, blank = True, null = True, default='')
    Subcategory = models.CharField(max_length = 50, blank = True, null = True, default='')
    Size = models.CharField(max_length = 50, default = '',blank = True, null = True)
    Addons = models.CharField(max_length = 50, default = '',blank = True, null = True)
    QtyAddons = models.IntegerField(blank = True, null = True, default='0')
    PSize = models.CharField(max_length = 50, default = '',blank = True, null = True)
    Price = models.IntegerField(blank = True, null = True, default='0')
    Subtotal = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    GSubtotal = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Cost = models.DecimalField(decimal_places=2,max_digits = 7,blank = True, null = True, default='0.00')
    Qty = models.IntegerField(blank = True, null = True, default='0')
    MOP = models.CharField(max_length = 50, default = '',blank = True, null = True)
    ordertype = models.CharField(max_length = 50, default = '',blank = True, null = True)
    Timetodeliver = models.CharField(max_length = 50, default = '',blank = True, null = True)
    ScheduleTime = models.CharField(max_length = 50, default = '',blank = True, null = True)
    gpslat = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    gpslng = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    gpsaccuracy = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    pinnedlat = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    pinnedlng = models.DecimalField(decimal_places=20,max_digits = 50,blank = True, null = True, default='0.00')
    tokens= models.CharField(max_length = 300, blank = True, null = True, default='')
    DateTime= models.DateTimeField(default=timezone.now)
    def __str__(self):

        return str(self.productname) +" / "+ str(self.Customername)+" / "+ str(self.Admin)+" / "+ str(self.Barangay)


class timesheet(models.Model):
    Admin=models.IntegerField(blank = True, null = True, default='2')
    Employeename = models.CharField(max_length = 50, blank = True, null = True, default='')
    Day = models.CharField(max_length = 50, blank = True, null = True, default='')
    Timein = models.CharField(max_length = 50, blank = True, null = True, default='')
    Timeout = models.CharField(max_length = 50, blank = True, null = True, default='')
    Totalmins = models.IntegerField(blank = True, null = True, default='0')
    #Productimg = models.ImageField(upload_to='Employeeattendance',blank = True, null = True)
    Sales = models.IntegerField(blank = True, null = True, default='0')
    Identifybonus = models.CharField(max_length = 50, blank = True, null = True, default='No Bonus')
    ASLbalance = models.IntegerField(blank = True, null = True, default='0')
    ISalary=models.IntegerField(blank = True, null = True, default='0')
    FSalary=models.IntegerField(blank = True, null = True, default='0')
    DateTime= models.DateTimeField(default=timezone.now)
    def __str__(self): 
        monthconvert=['January','February','March','April','May','June','July','August','September','October','November','December',]
        Monthidentifier=monthconvert[int(self.DateTime.strftime('%m'))-1]
        return Monthidentifier +" "+str(self.DateTime.strftime('%d')) +", "+str(self.DateTime.strftime('%Y'))+"   // "+ str(self.Admin)+" "+ str(self.Employeename)

