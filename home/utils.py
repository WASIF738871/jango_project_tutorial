from .models import Product
import time

def create_product():
    print("fuction excuted")
    time.sleep(2)

    product = Product.objects.create(
        name='Darsan bhai',
        price= 456,
        description= 'Darsan Bhai ,Product is very good Product'
    )
    print(product)
    print("fuction successfully excuted")