import re
from rest_framework import serializers
from account.models import accountUserModel,accountUserCartModel,accountUserProfileModel,accountUserLoginOtpModel
from django.core.exceptions import ValidationError
from datetime import date, datetime
date.today()
import datetime
from django.core.mail import send_mail
import random
from rest_framework_simplejwt.tokens import RefreshToken



class accountUserCreateSerializer(serializers.Serializer):
    phonenumber = serializers.IntegerField(required=True)
    email = serializers.EmailField(required=True)
    name=serializers.CharField(max_length=100)
    date_of_birth=serializers.DateField()
    image=serializers.ImageField()

    def validate(self, data):
        email=data.get('email')
        email_user=accountUserModel.objects.filter(email=email)
        if email_user.exists():
            raise serializers.ValidationError("email already exist")

        phonenumber = data.get('phonenumber')
        print(type(phonenumber))
        phnstr = str(phonenumber)
        if len(phnstr) == 10:
            pass
        else:
            raise serializers.ValidationError("phone number less than 10 digits")
        phone_user = accountUserModel.objects.filter(phonenumber=phonenumber)
        if phone_user.exists():
            raise serializers.ValidationError("phonenumber already exist")


        date_of_birth=data.get("date_of_birth")
        # date_of_birth_user=accountUserProfileModel.objects.create(date_of_birth=date_of_birth)
        date_of_birth = (datetime.date.today() - date_of_birth).days / 365
        # print(date_of_birth,'--------------')
        if date_of_birth < 18:
            raise serializers.ValidationError("age is less than 18")
        return data



    class Meta:
        fields= "__all__"

    def create(self, validated_data):
        print(validated_data)
        try:
            user = accountUserModel.objects.create(
                phonenumber=validated_data["phonenumber"],
                email=validated_data["email"],
                is_customer=True
            )
        except Exception as e:
            print(e)
            raise serializers.ValidationError(f"User not created {e}")
        try:

            user_profile_details=accountUserProfileModel.objects.create(

                owner=user,
                name=validated_data["name"],
                date_of_birth=validated_data["date_of_birth"],
                image=validated_data["image"]
            )

        except Exception as e:
            user.delete()
            raise serializers.ValidationError(f"User details not created {e}")

        try:
            user_cart=accountUserCartModel.objects.create(
                owner=user
            )
        except Exception as e:
            user.delete()
            user_profile_details.delete()
            raise serializers.ValidationError(f"User cart account not created")

        return validated_data


class accountGetAllASerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField()
    # email=serializers.SerializerMethodField()

    def get_details(self, obj):
        # print(obj.owner.phonenumber)
        details = {}
        details["phone"] = obj.owner.phonenumber
        details["email"] = obj.owner.email
        return details

    class Meta:
        model=accountUserProfileModel
        fields="__all__"


class accountGenarateOtpSerializer(serializers.Serializer):
    email=serializers.EmailField()
    def validate(self, data):
        email = data.get('email')
        # user = self.context['request'].user
        email_user = accountUserModel.objects.filter(email=email)
        if not email_user.exists():
            raise serializers.ValidationError("Invalid Email Address")
        return data

    class Meta:
        fields="__all__"

    def create(self, validated_data):
        email=validated_data.get("email")
        otp = random.randint(1000, 9999)
        send_mail("Your OTP",
                  f"Your otp is {otp} ",
                  "ivishnu.ms@gmail.com",
                  [email],
                )
        user = accountUserModel.objects.get(email=email)
        user=accountUserLoginOtpModel.objects.create(otp=otp,owner=user,active=True)
        return validated_data


class accountLoginSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True)
    otp=serializers.IntegerField(required=True)
    access=serializers.CharField(read_only=True)
    refresh=serializers.CharField(read_only=True)
    name=serializers.SerializerMethodField()

    # def get_details(self, obj):
    #     print(obj)

    # def get_name(self, obj):
    #     print(obj)
    #     # try:
    #     #     instance = accountUserProfileModel.objects.get(owner=obj)
    #     #     return instance.name
    #     # except:
    #     #
    #     #         return None
    #     details = {}
    #     details["name"] = obj.owner.name
    #     details["email"] = obj.owner.email
    #     return details

    def validate(self, data):
        email = data.get('email')
        user_otp = data.get('otp')

        try:
            user_check = accountUserModel.objects.get(email=email)
        except:
            raise serializers.ValidationError("Invalid Email")
        try:
            user_check_otp=accountUserLoginOtpModel.objects.get(owner=user_check,otp=user_otp)
        except:
            raise serializers.ValidationError("Invalid Email or  OTP")
        return data

    class Meta:
        fields = "__all__"


    def create(self, validated_data):
        email=validated_data.get('email')
        user_otp=validated_data.get('otp')

        try:
            user_check=accountUserModel.objects.get(email=email)
        except:
            raise serializers.ValidationError("Invalid Email")

        try:
            login_otp_check = accountUserLoginOtpModel.objects.filter(owner=user_check, otp=user_otp, active=True)
            if login_otp_check.exists():
                refresh = RefreshToken.for_user(user_check)
                print(refresh)
                return {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }
        except:
            raise serializers.ValidationError("Login Failed")
        return validated_data





































