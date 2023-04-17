from django.db import models
import uuid

CATEGORY_FIELD =(
    ('clothes','clothes'),
    ('accessories', 'accessories'),
    ('electronic items', 'electronic items')
)

class BaseModel(models.Model):
    order_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    is_created=models.DateTimeField(auto_now_add=True)
    is_updated=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Order(BaseModel):
    order_category=models.CharField(choices=CATEGORY_FIELD, max_length=100)
    order_name=models.CharField(max_length=50)
    order_quantity=models.IntegerField()
    def __str__(self) -> str:
        return self.order_name
    

class OrderDetails(BaseModel):
    amount=models.IntegerField()
    order_detail=models.ForeignKey(Order,on_delete=models.CASCADE)

    def __str__(self):
        return self.order_detail.order_name 
