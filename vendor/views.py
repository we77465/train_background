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