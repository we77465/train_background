from django import forms
from django.db import models
from .models import Vendor, food

#class VendorForm(forms.ModelForm):
#    class Meta:
#        model = Vendor
#        fields = '__all__'


from django.utils.translation import gettext_lazy as _ # 新增

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        # 新增 labels 對應
        labels = {
            'vendor_name': _('攤販名稱'),
            'store_name' : _('店名'),
            'phone_number' : _('電話'),
            'address' : _('地址'),
        }

class RawVendorForm(forms.Form):
    vendor_name = forms.CharField()
    store_name = forms.CharField()
    phone_number = forms.CharField()
    
# Model - Vendor 
class Form_Vendor(models.Model):
	vendor_name = models.CharField(max_length = 20) # 攤販的名稱
	store_name = models.CharField(max_length = 10) # 攤販店家的名稱
	phone_number = models.CharField(max_length = 20) # 攤販的電話號碼
	address = models.CharField(max_length = 100) # 攤販的地址