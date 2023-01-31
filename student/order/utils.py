from enum import Enum

class statusEnumType(Enum):

    PENDING = "PENDING"
    COMPLETED = "COMPLETED"

    @classmethod
    def choices(cls):
        # print(tuple((i.name, i.value) for i in cls))
        return [(i.value, i.name) for i in cls]