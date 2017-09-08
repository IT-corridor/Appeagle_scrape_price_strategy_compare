import os
import csv
import pdb
import datetime
import mimetypes

from django.contrib import admin
from django.utils.encoding import smart_str
from wsgiref.util import FileWrapper
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin import SimpleListFilter
from django.http import HttpResponse
from django.forms.models import model_to_dict

from .models import *


class RunTimeFilter(SimpleListFilter):
    title = 'RunTime'
    parameter_name = 'runtime'

    def lookups(self, request, model_admin):
        return [(ii.id, str(ii.run_at)) for ii in RunTime.objects.all().order_by('-id')]

    def queryset(self, request, queryset):
        return queryset.filter(run_at=RunTime.objects.all().order_by('-id')[0])


class ProductAdmin(admin.ModelAdmin):
    list_display = ['sku', 'asin_his', 'title', 'bb_status', 'our_min_price', 
                    'bb_price', 'appeagle_strategy', 
                    'num_orders', 'added_at', 'updated_at']
    search_fields = ['sku', 'asin']

    actions = ['export_products']
    # list_filter = (RunTimeFilter,)

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        self.runtime = request.GET.get('runtime')
        return qs

    def asin_his(self, obj):
        return u'<a href="/admin/general/producthistory/?o=9&q={0}">{0}</a>'.format(obj.asin)
    asin_his.allow_tags = True
    asin_his.short_description = "ASIN"

    def export_products(self, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        ids = ','.join([str(item.id) for item in queryset])
        fields = [f.name for f in Product._meta.get_fields() 
                  if f.name not in ['id', 'is_new']]

        path = datetime.datetime.now().strftime("/tmp/.bb_products_%Y_%m_%d_%H_%M_%S.csv")
        self.write_report(queryset, path, fields)
        wrapper = FileWrapper( open( path, "r" ) )
        content_type = mimetypes.guess_type( path )[0]

        response = HttpResponse(wrapper, content_type = content_type)
        response['Content-Length'] = os.path.getsize( path ) 
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str( os.path.basename( path ) ) 
        return response

    export_products.short_description = "Export products as CSV file" 

    def write_report(self, queryset, path, result_csv_fields):
        result = open(path, 'w')
        result_csv = csv.DictWriter(result, fieldnames=result_csv_fields)
        result_csv.writeheader()

        for product in queryset:
            product_ = model_to_dict(product, fields=result_csv_fields)
            for key, val in product_.items():
                if type(val) not in (float, int, long, bool, datetime.datetime) and val:
                    product_[key] = val.encode('utf-8')

            try:
                result_csv.writerow(product_)
            except Exception, e:
                print product_

        result.close()

    def bb_price_prev(self, obj):
        # pdb.set_trace()

        if self.runtime:
            prev_obj = Product.objects.filter(asin=obj.asin, run_at_id=self.runtime)
        else:
            prev_obj = Product.objects.filter(asin=obj.asin, run_at_id__lt=obj.run_at_id).order_by('-run_at_id')

        if prev_obj:
            return prev_obj[0].bb_price
        else:
            return '-'

    bb_price_prev.short_description = 'Prev BB Price'


class ProductHistoryAdmin(admin.ModelAdmin):
    list_display = ['sku', 'asin', 'title', 'bb_status', 'our_min_price', 
                    'bb_price', 'appeagle_strategy', 'num_orders', 'updated_at']
    search_fields = ['sku', 'asin']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductHistory, ProductHistoryAdmin)
admin.site.register(Interval)
