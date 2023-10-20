from django import forms

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