from enum import StrEnum, auto


class RouterTagEnum(StrEnum):
    DEFAULT = auto()
    SERVER = auto()
    REDIS = auto()
    RABBIT = auto()
    CHAT = auto()
