from store.models import Category,CartItem,Cart
from store.views import _cart_id

def menu_links(request):
    links=Category.objects.all()
    return dict(links=links)

def counter(request):
    item_count=0
    if 'admin' in request.path: # เช็คผ่าน path
        return {}
    else:
        try:    
            # query cart
            cart=Cart.objects.filter(cart_id=_cart_id(request)) 
            # query cartitem
            cart_Item=CartItem.objects.all().filter(cart=cart[:1]) # เก็บผลลัพที่ได้จากการดึงฐานข้อมูลรายการสินค้าในตะกร้า  / :1 โยน รหัสสินค้าเข้าไป
            for item in cart_Item:
                item_count+=item.quantity
        except Cart.DoesNotExist:
            item_count=0
    return dict(item_count=item_count)