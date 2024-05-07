from enum import Enum

class EstrategiasEnum(Enum):
    MARTINGALA = 1
    DALAMBERT = 2
    FIBONACCI = 3

    @classmethod
    def has_value(cls, value:str):
        if not isinstance(value, str):
            return False
        value_upper:str = value.upper()

        return (value_upper in EstrategiasEnum._member_names_)

    @classmethod
    def show_values(cls):
        return EstrategiasEnum._member_names_

