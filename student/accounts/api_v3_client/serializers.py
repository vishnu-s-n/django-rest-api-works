from rest_framework import serializers
from accounts.models import accountsUserModel,accountsUserProfileModel
from datetime import date, datetime
import datetime
date.today()

class accountsUserCreateSerializer(serializers.Serializer):
    phonenumber = serializers.IntegerField(required=True)
    email = serializers.EmailField(required=True)
    name=serializers.CharField(max_length=100)
    date_of_birth=serializers.DateField()
    image=serializers.ImageField()
    gender=serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        email_user = accountsUserModel.objects.filter(email=email)
        if email_user.exists():
            raise serializers.ValidationError("email already exist")
        phonenumber = data.get('phonenumber')
        print(type(phonenumber))
        phnstr = str(phonenumber)
        if len(phnstr) == 10:
            pass
        else:
            raise serializers.ValidationError("Enter a Valid Phone Number")
        phone_user = accountsUserModel.objects.filter(phonenumber=phonenumber)
        if phone_user.exists():
            raise serializers.ValidationError("phonenumber already exist")

        date_of_birth = data.get("date_of_birth")
        # date_of_birth_user=accountUserProfileModel.objects.create(date_of_birth=date_of_birth)
        date_of_birth = (datetime.date.today() - date_of_birth).days / 365
        # print(date_of_birth,'--------------')
        if date_of_birth < 18:
            raise serializers.ValidationError("age is less than 18")
        return data


    class Meta:
        fields="__all__"

    def create(self, validated_data):
        try:
            user = accountsUserModel.objects.create(
                phonenumber=validated_data["phonenumber"],
                email=validated_data["email"],
                is_customer=True
            )
        except Exception as e:
            print(e)
            raise serializers.ValidationError(f"User not created {e}")

        try:

            user_profile_details=accountsUserProfileModel.objects.create(

                owner=user,
                name=validated_data["name"],
                date_of_birth=validated_data["date_of_birth"],
                image=validated_data["image"],
                gender=validated_data["gender"]
            )

        except Exception as e:
            user.delete()
            raise serializers.ValidationError(f"User details not created {e}")
        return validated_data



