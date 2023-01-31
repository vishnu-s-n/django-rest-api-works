from enum import Enum


class genderEnumType(Enum):

    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"

    @classmethod
    def choices(cls):
        # print(tuple((i.name, i.value) for i in cls))
        return [(x.value , x.name) for x in cls]