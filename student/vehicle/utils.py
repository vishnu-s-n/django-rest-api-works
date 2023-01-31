from enum import Enum

class statusEnumType(Enum):

    RUNNING = "RUNNING"
    BREAKDOWN = "BREAKDOWN"

    @classmethod
    def choices(cls):
        # print(tuple((i.name, i.value) for i in cls))
        return [(i.value, i.name) for i in cls]

class statusVehicleEnumType(Enum):

    BREAKDOWN = "BREAKDOWN"
    INSPECTION = "INSPECTION"

    @classmethod
    def choices(cls):
        # print(tuple((i.name, i.value) for i in cls))
        return [(i.value, i.name) for i in cls]

class statusVehicleAssignEnumType(Enum):

    assign = "assign"
    deassign = "deassign"

    @classmethod
    def choices(cls):
        # print(tuple((i.name, i.value) for i in cls))
        return [(i.value, i.name) for i in cls]




