from enum import StrEnum, IntEnum


class ChocolateEndpoint(StrEnum):
    GET_CHOCOLATES = "chocolates"
    GET_CHOCOLATE_PRICE = "chocolates/{chocolate_id}/price"
    BUY_CHOCOLATE = "buy/{chocolate_id}"


class StatusCode(IntEnum):
    OK = 200
    CREATED = 201
    NOT_FOUND = 404


class AssertMode(StrEnum):
    FULL = "FULL"
    SOFT = "SOFT"


class ResponseMessage(StrEnum):
    CHOCOLATE_NOT_FOUND = "Chocolate not found"
    INSUFFICIENT_BALANCE = "Insufficient balance"
    PURCHASE_SUCCESSFUL = "Purchase successful"
