from django.shortcuts import redirect, render
from django.views import View
from . models import Product,CartItem
from django.http import HttpResponse

# Create your views here.



def total_cart_item():
    total_count = 0
    try:
        card_item=CartItem.objects.all()
        for item in card_item:
            total_count = item.item_count+total_count

    except:
            pass
    return total_count


def addItem(id):
    try:
        item = CartItem.objects.get(item_product_id = id)
        item.item_count = item.item_count+1
        item.save()
        
    except:
        item=CartItem.objects.create(item_product_id =id,item_count=1)
    
    return 1

class ProductListView(View):
    def get(self,request):
        product = Product.objects .all()
        total_count=total_cart_item()
        context = {"product":product,"total_count":total_count}


        return render(request,"user/productlist.html",context)

class ProductAddView(View):
    def get(self,request,id):
        try:
            item = CartItem.objects.get(item_product_id = self.kwargs["id"])
            item.item_count = item.item_count+1
            item.save()        
        except:
            item=CartItem.objects.create(item_product_id =self.kwargs["id"],item_count=1)        
        request.session["cart_item"] = item.id
        return redirect("product_list")


class CartItemDisplayView(View):
    def get(self,request):
        product = CartItem.objects.all()
        total_count=total_cart_item()
        context = {"product":product,"total_count":total_count}
        return render(request,"user/cart.html",context)

class EditCartProductView(View):
    def get(self,request,id):
        context = {}
        total_count=total_cart_item()
        try:
            item = CartItem.objects.get(item_product_id = self.kwargs["id"])        
        except:
            pass
        if item:
            context["cart_data"] = True
            context["item"] = item
        else:
            context["cart_data"] =False
        context["total_count"] = total_count
        return render(request,"user/itemdetail.html",context)



class CartItemAdded(View):
    def get(self,request,id):
        addItem(self.kwargs["id"])
        return redirect("product_edit",id=self.kwargs["id"])

class CartItemRemove(View):
    def get(self,request,id):
        try:
            item = CartItem.objects.get(item_product_id = id)
            if item.item_count > 0:
                item.item_count = item.item_count-1
                item.save()
            else:
                return redirect("product_list")
        except:
            pass
        return redirect("product_edit",id=self.kwargs["id"])


class EmptyCartView(View):
    def get(self,request):
        CartItem.objects.all().delete()
        del request.session["cart_item"]
        return redirect("product_list")

