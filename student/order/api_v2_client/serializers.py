from rest_framework import serializers
from account.models import accountUserCartModel,accountUserCartProduct,accountUserModel
from product.models import productPMainModel
from order.models import orderOMainModel

class orderAddingSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(read_only=True)
    class Meta:
        fields="__all__"

    def validate(self,data):
        user = self.context['request'].user

        product=data.get("products")
        try:
            cart_instance = accountUserCartModel.objects.get(products=product)
        except:
            return data
        cart_product = cart_instance.products.all()
        if not cart_product.exists():
            print(cart_product)
            raise serializers.ValidationError("Cart is Empty")

    def create(self, validated_data):
        product=validated_data.get("product")
        try:
            product_instance = accountUserCartModel.objects.get(product=product)
        except:
            return validated_data
        cart_product = product_instance.products.all()
        total=0
        for product in cart_product:
            total += product.product.price
        print(total,'--------total price')
        cart_product.final_price=total
        cart_product.save()
        order=orderOMainModel.objects.create(product=product)
        order_instance = accountUserCartModel.objects.get(product=product)
        order = order_instance.products.all()
        user_cart=cart_product.clear()
        user_cart.save()


        # <editor-fold desc="Notes">
        """
                1.request user get and user cart in there or not else raise error
                2.user cart instance inside products.all exists or not else raise your cart is empty.
        """

        """
        1.request user get and user cart get from request user
        2.user cart object from product all get and using for loop  every product having price is total
        3.new order is create
        4.order instance using product set using cart.product.all
        5.user cart .clear
        6.user cart save
        """
        # </editor-fold>



