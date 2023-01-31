from rest_framework import serializers
from product.models import productPImageModel, productPMainModel
from account.models import accountUserModel,accountUserCartModel,accountUserCartProduct


# <editor-fold desc="Product Creation Serializer">
class productPCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    # unique_code = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    image = serializers.ListField(child=serializers.FileField(max_length=300, allow_empty_file=False), write_only=True)


    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        try:
            product = productPMainModel.objects.create(
                    title=validated_data.get("title"),
                    description=validated_data.get("description"),
                    # unique_code=validated_data.get("unique_code"),
                    price=validated_data.get("price"))
        except Exception as e:
            print(e)
            raise serializers.ValidationError(f"Product not created {e}")

        images = validated_data.get("image")
        print(images)
        try:
            if images is not None:
                for image in images:
                    try:
                        product_image = productPImageModel.objects.create(product=product, image=image)
                    except Exception as e:
                        product.delete()
                        raise serializers.ValidationError(f"Product Image not created {e}")
        except:
            product.delete()
            raise serializers.ValidationError(f"Product Image not passes")

        return validated_data
# </editor-fold>

class productImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=productPImageModel
        fields= ["image"]


# <editor-fold desc="Product Get All Details Serializer">
class productGetAllPSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    def get_image(self, obj):

        product_images = obj.productPImageModel_product.all()
        try:
            images = productImageSerializer(product_images,many=True).data
        except:
            images = []
        return images

    class Meta:
        model = productPMainModel
        fields = "__all__"
# </editor-fold>

# <editor-fold desc="Product Adding To Cart Serializer">
class productAddingCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    user_id = serializers.IntegerField()

    class Meta:
        model=accountUserCartModel
        fields = "__all__"

    def validate(self,data):
        user_id=data.get("user_id")
        product_id=data.get("product_id")
        try:
            user = accountUserModel.objects.get(id=user_id)
        except:
            raise serializers.ValidationError("User not exit")
        try:
            product=productPMainModel.objects.get(id=product_id)
        except:
            raise serializers.ValidationError("product not exist")

        user_cart = accountUserCartModel.objects.filter(owner=user)
        if user_cart.exists():
            cart_product = accountUserCartProduct.objects.filter(owner=user, product=product, status="PENDING")
            if cart_product.exists():
                product = cart_product.last()
                # user_cart.product.filter(product)
                if cart_product.exists():
                    raise serializers.ValidationError("Product is already in cart")
                else:
                    user_cart.product.add(product)
            else:
                product_user = accountUserCartProduct.objects.create(owner=user,product=product,status="PENDING")
            try:
                user_carts = accountUserCartModel.objects.get(owner=user)
            except:
                accountUserCartModel.objects.create(owner=user)
            user_carts.products.add(product_user.id)
            instance_products = user_cart.products.all()
            print(instance_products)
            total = 0
            for product in instance_products:
                total += product.product.price
            print(total)
            user_cart.final_price = total
            user_cart.save()
            return data


    def create(self, validated_data):
        user_id=validated_data.get("user_id")
        product_id=validated_data.get("product_id")
        try:
            user = accountUserModel.objects.get(id=user_id)
        except:
            raise serializers.ValidationError({"message":"account user Does Not Exist"})
        try:
            product=productPMainModel.objects.get(id=product_id)
        except:
            raise serializers.ValidationError({"message":"Product Does Not Exist"})

    #     user_cart_line=accountUserCartProduct.objects.create(owner=user,product=product,status="PENDING")
    #
    #     print(user_cart_line,'----------------')
    #     try:
    #         user_cart=accountUserCartModel.objects.get(owner=user)
    #     except:
    #         user_cart = accountUserCartModel.objects.create(owner=user)
    #     user_cart.products.add(user_cart_line.id)
    #     instance_products = user_cart.products.all()
    #     print(instance_products,'-------------instance prodct')
    #     total = 0
    #     for product in instance_products:
    #         total += product.product.price
    #     print(total,'--------total price')
    #     user_cart.final_price=total
    #     user_cart.save()
    #     return validated_data

# </editor-fold>

# <editor-fold desc="Product Cart Details Serializer">
class productGetCartDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=accountUserCartModel
        fields="__all__"
# </editor-fold>


# <editor-fold desc="==========================================">
# class productPCreateSerializer(serializers.ModelSerializer):
#     image = serializers.ImageField(read_only=True)
#     uploaded_images=serializers.ListField(child=serializers.ImageField(max_length=1000,allow_empty_file=False,write_only=True))
#
#     class Meta:
#         model=productPMainModel
#         fields="__all__"
#
#     def create(self, validated_data):
#         uploaded_images=validated_data.pop("uploaded_images")
#         product=productPMainModel.objects.create(**validated_data)
#         for image in uploaded_images:
#             product_image = productPImageModel.objects.create(product=product, image=image)
#         return product
# </editor-fold>

# product_user=accountUserCartProduct.objects.get(owner=user,product=product)
#         if product_user.exists():
#             cart_product=accountUserCartProduct.objects.get(owner=user,product=product)
#             if cart_product.exists():
#                 cart_product_user=accountUserCartProduct.ojects.get(owner=user,product=product)
#                 raise serializers.ValidationError("Products in Cart")
#             else:
#                 add_to_cart=accountUserCartProduct.objects.create(owner=user, product=product, status="PENDING")
#         else:
#             product_user=accountUserCartProduct.objects.create(owner=user,product=product)
#             add_to_cart = accountUserCartProduct.objects.create(owner=user, product=product, status="PENDING")
#
#         # else:
#         #     accountUserCartProduct.objects.create(owner=user)
#         #     add_to_cart = accountUserCartProduct.objects.create(owner=user, product=product, status="PENDING")
#         #
#
#         # except:
#         #     accountUserCartModel.objects.create(owner=user)
#         #     if user_cart.exists():
#         #         accountUserCartProduct.objects.create(owner=user, product=product, status="PENDING")
#         #     else:
#         #         raise serializers.ValidationError("Cart is not exists")
#
#             # raise  serializers.ValidationError("Cart is not created")
#
#         cart_product = user_cart.products.filter(product=product,owner=user,status="COMPLETED")
#         if cart_product.exists():
#             raise serializers.ValidationError("product is already in the cart")

# user_cart.product.filter(product)

# user_cart.products.add(product_user)
