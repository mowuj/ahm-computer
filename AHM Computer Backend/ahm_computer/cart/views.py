from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
# Create your views here.
from . models import Cart,CartProduct,Order
from product.models import Product
from .serializers import CartSerializer,CartProductSerializer,OrderSerializer


class AddToCartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartProductSerializer

    def create(self, request, *args, **kwargs):
        product_id = self.kwargs['id']
        cart_id = self.request.session.get("cart_id", None)

        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'detail': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        if cart_id:
            try:
                cart_obj = Cart.objects.get(id=cart_id)
                product_in_cart = cart_obj.cartproduct_set.filter(
                    product=product_obj)

                # item already exists in cart
                if product_in_cart.exists():
                    cartproduct = product_in_cart.last()
                    cartproduct.quantity += 1
                    cartproduct.subtotal += product_obj.sell_price
                    cartproduct.save()
                    cart_obj.total += product_obj.sell_price
                    cart_obj.save()
                else:
                    # new items added to cart
                    cartproduct = CartProduct.objects.create(
                        cart=cart_obj,
                        product=product_obj,
                        rate=product_obj.sell_price,
                        quantity=1,
                        subtotal=product_obj.sell_price
                    )
                    cart_obj.total += product_obj.sell_price
                    cart_obj.save()

            except Cart.DoesNotExist:
                return Response({'detail': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

        else:
            # create a new cart
            cart_obj = Cart.objects.create(total=0)
            self.request.session['cart_id'] = cart_obj.id
            cartproduct = CartProduct.objects.create(
                cart=cart_obj,
                product=product_obj,
                rate=product_obj.sell_price,
                quantity=1,
                subtotal=product_obj.sell_price
            )
            cart_obj.total += product_obj.sell_price
            cart_obj.save()

        serializer = CartProductSerializer(cartproduct)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
