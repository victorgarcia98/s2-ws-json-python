from typing import Callable, Generic, Protocol, Type, TypeVar

from pydantic import BaseModel
from pydantic import Protocol as PydanticProtocol
from pydantic import StrBytes, ValidationError

from s2wsjson.s2_validation_error import S2ValidationError

B = TypeVar("B", bound=BaseModel, covariant=True)


class SupportsValidation(Protocol[B]):
    # ValidateValuesMixin methods
    def to_json(self) -> str:
        ...

    def to_dict(self) -> dict:
        ...

    @classmethod
    def from_json(cls, json_str: str) -> B:
        ...

    # Pydantic methods
    def json(self) -> str:
        ...

    def dict(self) -> dict:
        ...

    @classmethod
    def parse_raw(
        cls,
        b: StrBytes,
        *,
        content_type: str = ...,
        encoding: str = ...,
        proto: PydanticProtocol = ...,
        allow_pickle: bool = ...
    ) -> B:
        ...


C = TypeVar("C", bound="SupportsValidation")


class ValidateValuesMixin(Generic[C]):
    def to_json(self: C) -> str:
        return self.json()

    def to_dict(self: C) -> dict:
        return self.dict()

    @classmethod
    def from_json(cls: Type[C], json_str: str) -> C:
        gen_model: C = cls.parse_raw(json_str)
        return gen_model


def convert_to_s2exception(f: Callable):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except (ValidationError, TypeError) as e:
            raise S2ValidationError(
                args[0],
                "Pydantic raised a format validation error.",
                pydantic_validation_error=e,
            )

    inner.__doc__ = f.__doc__
    inner.__annotations__ = f.__annotations__

    return inner


def patch(input_class):
    input_class.__init__ = convert_to_s2exception(input_class.__init__)
    input_class.__setattr__ = convert_to_s2exception(input_class.__setattr__)

    input_class.json = convert_to_s2exception(input_class.json)
    input_class.dict = convert_to_s2exception(input_class.dict)
    input_class.parse_raw = convert_to_s2exception(input_class.parse_raw)

    return input_class
