from enum import Enum


class genderEnumType(Enum):

    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"

    @classmethod
    def choices(cls):
        # print(tuple((i.name, i.value) for i in cls))
        return [(x.value , x.name) for x in cls]

class GradeEnumType(Enum):

    A = "A"
    B = "B"
    C = "C"
    D = "D"

    @classmethod
    def choices(cls):
        # print(tuple((i.name, i.value) for i in cls))
        return [(i.value, i.name) for i in cls]

class SemEnumType(Enum):

    First = "First"
    Second = "Second"
    Third = "Third"
    Fourth = "Fourth"

    @classmethod
    def choices(cls):
        # print(tuple((i.name, i.value) for i in cls))
        return [(i.value, i.name) for i in cls]

class BranchEnumType(Enum):

    CSE = "CSE"
    MECH = "MECH"
    ECE = "ECE"
    CIVIL = "CIVIL"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]