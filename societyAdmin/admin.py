from django.contrib import admin
from societyAdmin.models import Carpenter, Electrician, Painter, Plumber, Ruffer
# Register your models here.
@admin.register(Plumber)
class PlumberAdmin(admin.ModelAdmin):
 list_display=('id','plname','plnemail','plnmobile','plnaddress','plnprice','plnstatus','plnbook','plnusers','plntype')


@admin.register(Painter)
class PainterAdmin(admin.ModelAdmin):
 list_display=('id','painame','paiemail','paimobile','paiaddress','paiprice','paistatus','paibook','paiusers','paitype')
 
@admin.register(Carpenter)
class CarpenterAdmin(admin.ModelAdmin):
     list_display=('id','carname','caremail','carmobile','caraddress','carprice','carstatus','carbook','carusers','cartype')
 
@admin.register(Ruffer)
class CarpenterAdmin(admin.ModelAdmin):
     list_display=('id','rufname','rufemail','rufmobile','rufaddress','rufprice','rufstatus','rufbook','rufusers','ruftype')

@admin.register(Electrician)
class CarpenterAdmin(admin.ModelAdmin):
     list_display=('id','elename','eleemail','elemobile','eleaddress','eleprice','elestatus','elebook','eleusers','eletype')