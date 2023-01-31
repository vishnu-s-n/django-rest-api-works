from rest_framework import serializers
from vehicle.models import vehicleVMainModel,vehicleBreakDownModel,vehicleBreakDownImageModel,vehicleAssignModel,vehicleInspectionModel
from accounts.models import accountsUserModel

class vehicleCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model=vehicleVMainModel
        fields="__all__"

class vehicleAssignSerializer(serializers.Serializer):
    vehicle_id = serializers.IntegerField()
    user_id = serializers.IntegerField()

    def validate(self, data):
        vehicle_id = data.get("vehicle_id")
        user_id = data.get("user_id")

        try:
            vehicle = vehicleVMainModel.objects.get(id=vehicle_id)
        except:
            raise serializers.ValidationError("Vehicle not exit")

        try:
            user=accountsUserModel.objects.get(id=user_id)
        except:
            raise serializers.ValidationError("USer not exists")
        return data

        # vehicle_user=accountsUserModel.objects.filter(owner=user)
        # if vehicle_user.exists():
        #     vehicle_assign=vehicleAssignModel.objects.filter(owner=user,vehicle=vehicle,status="assign")
        #     assign=vehicle_assign.last()
        #     if vehicle_assign.exists():
        #         raise serializers.ValidationError("Already assigned")

    class Meta:
        fields="__all__"

    def create(self, validated_data):
        user_id = validated_data.get("user_id")
        vehicle_id = validated_data.get("vehicle_id")
        try:
            user = accountsUserModel.objects.get(id=user_id)
        except:
            raise serializers.ValidationError({"message": "account user Does Not Exist"})
        try:
            vehicle = vehicleVMainModel.objects.get(id=vehicle_id)
        except:
            raise serializers.ValidationError({"message": "vehicle Does Not Exist"})

        vehicle_assign=vehicleAssignModel.objects.create(owner=user,vehicle=vehicle,status="assign")

        # try:
        #     assign=vehicleAssignModel.objects.get(owner=user)
        # except:
        #     assign = vehicleAssignModel.objects.create(owner=user)
        vehicle_assign.status = "deassign"
        vehicle_assign.save()
        return validated_data


class vehicleBreakDownSerializer(serializers.Serializer):
    vehicle_id = serializers.IntegerField()
    reason = serializers.CharField(max_length=100)
    image = serializers.ListField(child=serializers.FileField(max_length=300, allow_empty_file=False), write_only=True)

    def validate(self, data):
        vehicle_id = data.get("vehicle_id")
        try:
            vehicle = vehicleVMainModel.objects.get(id=vehicle_id)
        except:
            raise serializers.ValidationError("vehicle not exists")

        if vehicle.status == "RUNNING":
            pass
        elif vehicle.status == "BREAKDOWN":
            raise serializers.ValidationError("vehicle is in breakdown condition")
        else:
            pass

        return data

    class Meta:
        fields= "__all__"

    def create(self, validated_data):
        print(validated_data)
        vehicle_id=validated_data.get("vehicle_id")
        vehicle = vehicleVMainModel.objects.get(id=vehicle_id)
        try:
            break_down = vehicleBreakDownModel.objects.create(reason=validated_data.get("reason"),vehicle=vehicle)
        except Exception as e:
            raise serializers.ValidationError(f"BreakDown Reason not added {e}")

        images = validated_data.get("image")
        try:
            if images is not None:
                for images in images:
                    try:
                        vehicle_images = vehicleBreakDownImageModel.objects.create(break_down=break_down, image=images,status="BREAKDOWN")
                        vehicle.status = "BREAKDOWN"
                        vehicle.save()
                    except Exception as e:
                        break_down.delete()
                        raise serializers.ValidationError(f"BreakDown image not created {e}")
        except Exception as e:
            break_down.delete()
            raise serializers.ValidationError(f"Image not passes {e}")
        return validated_data

class vehicleInspectionSerializer(serializers.Serializer):
    break_down_id=serializers.IntegerField()
    reason=serializers.CharField(max_length=50)

    def validate(self,data):
        break_down_id = data.get("break_down_id")
        try:
            break_down = vehicleBreakDownModel.objects.get(id=break_down_id)
        except:
            raise serializers.ValidationError("break down not exists")

        return data

    class Meta:
        fields="__all__"

    def create(self, validated_data):
        break_down_id = validated_data.get("break_down_id")
        break_down=vehicleBreakDownModel.objects.get(id=break_down_id)
        try:
            vehicle_inspection = vehicleInspectionModel.objects.create(reason=validated_data.get("reason"),break_down=break_down)
            # queryset = break_down.vehicleBreakDownImageModel_break_down.filter(break_down=break_down).update(status="INSPECTION")
        except Exception as e:
            raise serializers.ValidationError(f"Reason down not added {e}")
        return validated_data








