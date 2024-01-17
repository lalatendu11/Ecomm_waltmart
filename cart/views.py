from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponse

@login_required
def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals})


def cart_add(request):
    # Get the cart
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # lookup product in DB
        product = get_object_or_404(Product, id=product_id)

        # Save to session
        cart.add(product=product, quantity=product_qty)

        # Get Cart Quantity
        cart_quantity = cart.__len__()

        # Return resonse
        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty': cart_quantity})
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        # Call delete Function in Cart
        cart.delete(product=product_id)

        response = JsonResponse({'product':product_id})
        #return redirect('cart_summary')
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty':product_qty})
        #return redirect('cart_summary')
        return response


def success(request):
    return render(request, template_name="success.html")


def address(request):
    return render(request, template_name="address.html")



def checkout(request):
    cart = Cart(request)
    totals = cart.cart_total()
    return render(request, 'checkout.html', {"totals": totals})



# class address1(View):
#     def get(self,request):
#         name = request.POST["name"]
#         mob = int(request.POST["cont"])
#         gmail = request.POST["gmail"]
#         house_no = request.POST["Add1"]
#         pin = int(request.POST["pin"])
#         city = request.POST["Add2"]
#         state = request.POST["Add4"]
#
#         add1 =address1(gmail=gmail,name=name,house_no=house_no,city=city,pin=pin,mob=mob,state=state)
#         add1.save()
#         return HttpResponse("ok done")