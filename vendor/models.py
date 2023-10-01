from django.db import models
from django.contrib import admin
# Create your models here.
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=20)
    store_name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length = 20) # 攤販的電話號碼
    address = models.CharField(max_length = 100) # 攤販的地址
    def __str__(self):
        return self.vendor_name
    
class food(models.Model):
    food_name = models.CharField(max_length=30)
    price_name = models.DecimalField(max_digits=3,decimal_places=0)
    food_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE) # 代表這食物是由哪一個攤販所做的
    def __str__(self):
        return self.food_name
    

class VendorAdmin(admin.ModelAdmin):
	list_display = ('id', 'vendor_name') 
     


# @admin.register(Vendor)
# class VendorAdmin(admin.ModelAdmin):
#     # 這裡我一併將 Vendor 類別 其它的欄位都加進來了
# 	list_display = ['id', 'vendor_name', 'store_name', 'phone_number', 'address']
     
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Vendor._meta.fields]
    # 上下兩者目的相同
    # list_display = ['id', 'vendor_name', 'store_name', 'phone_number', 'address']

from django.utils.translation import gettext_lazy as _

# 自行宣告 類別
class Morethanfifty(admin.SimpleListFilter):

	title = _('price')
	parameter_name = 'compareprice' # url最先要接的參數

	def lookups(self, request, model_admin):
		return (
			('>50',_('>50')), # 前方對應下方'>50'(也就是url的request)，第二個對應到admin顯示的文字
			('<=50',_('<=50')),
		)
    # 定義查詢時的過濾條件
	def queryset(self, request, queryset):
		if self.value() == '>50':
			return queryset.filter(price_name__gt=50)
		if self.value() == '<=50':
			return queryset.filter(price_name__lte=50)
            
@admin.register(food)
class FoodAdmin(admin.ModelAdmin):
	list_display = [field.name for field in food._meta.fields]
    # 將 Morethanfifty 填入
	list_filter = (Morethanfifty,)
	ordering = ['price_name',]