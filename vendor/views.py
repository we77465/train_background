from django.shortcuts import render
from .models import Vendor

# Create your views here.
def showtemplate(request):
    vendor_list = Vendor.objects.all() # 把所有 Vendor 的資料取出來
    context = {'vendor_list': vendor_list} # 建立 Dict對應到Vendor的資料，
    return render(request, 'vendors/vendor_detail.html', context)

#from django.shortcuts import render
#from .models import Vendor
## Create your views here.
#def showtemplate(request):
#    vendor_list = Vendor.objects.all()
#    context = {'vendor_list': vendor_list}
#    # print(vendor_list)
#    return render(request, 'vendors/vendor_detail.html', context)


from .forms import VendorForm # 要記得 import 相對應的 Model Form 唷!
from .forms import RawVendorForm # 新增 RawVendorForm

# 新增
def vendor_create_view(request):
    form = RawVendorForm(request.POST or None)
    if form.is_valid():
        Vendor.objects.create(**form.cleaned_data) # 新增
        form = RawVendorForm()
    context = {
        'form' : form
    }
    return render(request, "vendors/vendor_create.html", context)