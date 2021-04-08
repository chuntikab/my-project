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
    global point,point2,total_after_point,total_after_point
    item_count=0
    total=0
    totalBefore=0

    counter=0 
    if 'admin' in request.path: # เช็คผ่าน path
        return {}
    elif not 'home' in request.path :
        point=900
        if point>0 :
        #try:    
            #point=900
            point2=1
            total_after_point=0
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
            if total_after_point <= 0 and not 'thankyou' in request.path:
                #nonlocal point
                point = int(point-totalBefore)
                total_after_point=0
                total=total_after_point
                print(1,point)
                #return point
            else :
                #nonlocal point
                total=totalBefore-point
                point = 0
                print(2,point)
                #return point
            # if 'thankyou' in request.path and counter==0:
            #     point2+=point
            #     print(3,point2) 
        else:       
        #except Cart.DoesNotExist:
            if 'thankyou' in request.path and counter==0:
                point2+=point
                print(3,point2)


        # if 'thankyou' in request.path and counter==0:
        #         point2+=point
        #         print(3,point2)

        # if 'thankyou' in request.path:
        #     point=0
            


    return dict(item_count=item_count,total=total,point=point,total_after_point=total_after_point,totalBefore=totalBefore,point2=point2)
