from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#-----------------------------------------

class FoodItemsModel(models.Model):

    prod_code = models.IntegerField(default=100)
    restaurant_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1
    )
    admin = models.CharField(max_length=50, null=True)
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(
        max_length=500,
        default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea, ut. Fugiat excepturi sit, perferendis debitis deserunt quaerat earum optio, voluptatum officia voluptatibus possimus placeat eligendi, consequuntur blanditiis deleniti modi praesentium."
    )
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://cdn.dribbble.com/userupload/22570626/file/original-379b4978ee41eeb352e0ddacbaa6df96.jpg"
    )


    def __str__(self):
        return str((self.item_name, self.item_price))

# Log history model
#-----------------------------------------

class LogHistoryModel(models.Model):
    log_username = models.CharField(max_length=50)
    log_prod_code = models.IntegerField(default=100)
    log_item_name = models.CharField(max_length=100)
    log_opration_type = models.CharField(max_length=50)

    def __str__(self):
        return str(
            (
                self.log_username,
                self.log_prod_code,
                self.log_item_name,
                self.log_opration_type
            )
        )
    
    
