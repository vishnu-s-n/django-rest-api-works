from rest_framework import serializers

from student.models import studentSModel,studentMainModel,studentMarkModel

class studentGetAllSSerializer(serializers.ModelSerializer):
    branch=serializers.SerializerMethodField()

    def get_branch(self, obj):
        try:
            instance=studentMainModel.objects.get(owner=obj)
            print(instance)
            return instance.branch
        except:
            return None

    # branch=serializers.SerializerMethodField(read_only=True)

    # def get_branch(self, obj):

        # branch=studentMainModel.objects.filter(owner=obj)
        # serializer=studentMainSerializer(branch)
        # return serializer.data


    class Meta:
        model=studentSModel
        fields = "__all__"




class studentMainSerializer(serializers.ModelSerializer):

    class Meta:
        model=studentMainModel
        fields= "__all__"

class studentMarkSerializer(serializers.ModelSerializer):

    class Meta:
        model=studentMarkModel
        fields= "__all__"


class studentDetailSerializer(serializers.ModelSerializer):
    marks = serializers.SerializerMethodField()
    grade=serializers.SerializerMethodField()

    def get_grade(self, obj):

        try:
            instance=studentMainModel.objects.get(owner=obj)
            return instance.grade
        except:
            return None

    def get_marks(self,obj):
        try:
            instance = studentMainModel.objects.get(owner=obj)
            marks = studentMarkSerializer(instance.marks, many=True)
            return marks.data

        except:
            return None



    # def get_final_grade(self,obj):
    #     try:
    #         instance=studentMarkModel.objects.values("grade").filter(owner=obj)
    #         len(instance.grade)
    #         grade = ["A","B","C","D"]
    #
    #
    #     except:
    #         return None

    # def get_final_grade(self,obj):


    # def get_marks(self,obj):
    #     instance = studentMainModel.objects.get(owner=obj)
    #     print(instance)
    #     return instance.marks

    # def get_final_grade(self,obj):
    #     dict={"A":10, "B":20, "c":30,"D":40}
    #     marks=studentMarkModel.objects.values("grade").filter(owner=obj)
    #     s=0
    #     for i in marks:
    #         s+=dict[i["grade"]]
    #     average=s//len(marks)
    #     m=[k for k, v in dict.items() if v == average]
    #     return m[0]

    class Meta:
        model=studentSModel
        fields= "__all__"


class studentAdminCreateSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=150,required=True)
    date_of_birth=serializers.DateField()
    gender=serializers.CharField(max_length=150,required=True)
    image=serializers.ImageField()
    branch=serializers.CharField(max_length=150,required=True)

    class Meta:
        field="__all__"

    def create(self, validated_data):
        try:

            student=studentSModel.objects.create(name=validated_data["name"],
                                             date_of_birth=validated_data["date_of_birth"],
                                             gender=validated_data["gender"],
                                             image=validated_data["image"])
        except Exception as e:
            raise serializers.ValidationError(f"Student not created {e}")
        try:

            student_details=studentMainModel.objects.create(owner=student,branch=validated_data["branch"])
        except Exception as e:
            student.delete()
            raise serializers.ValidationError(f"student details not created {e}")

        return validated_data


class studentPostGradeSSerializer(serializers.ModelSerializer):
    class Meta:
        model=studentMarkModel
        fields= "__all__"