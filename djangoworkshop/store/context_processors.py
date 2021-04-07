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

def counterPoint(request):
    item_count=0
    point=900
    total=0
    totalBefore=0
    total_after_point=0
    counter=0 
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
                totalBefore += (item.product.price * item.quantity)
                counter += item.quantity

            total_after_point = totalBefore-point # ex (-200) = 700-900 / 1090 = 1990-900
            #total = total_after_point
            if total_after_point <= 0:
                point = int(point-totalBefore)
                total_after_point=0
                total=total_after_point
            else:
                total=totalBefore-point
                point = 0
        except Cart.DoesNotExist:
            point = 0
    return dict(item_count=item_count,total=total,point=point,total_after_point=total_after_point,totalBefore=totalBefore)
