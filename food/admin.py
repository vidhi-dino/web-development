from django.contrib import admin
from .models import FoodItemsModel
from .models import LogHistoryModel

# Register your models here.
#------------------------------------------
admin.site.register(FoodItemsModel)
admin.site.register(LogHistoryModel)


