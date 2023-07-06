"""Compatibility layer to make this package usable with Pydantic 1 or 2"""

from typing import TYPE_CHECKING

from pydantic.version import VERSION as PYDANTIC_VERSION

PYDANTIC_MAJOR_VERSION = int(PYDANTIC_VERSION.split(".", 1)[0])

if int(PYDANTIC_MAJOR_VERSION) >= 2:
    PYDANTIC_V2 = True
else:
    PYDANTIC_V2 = False

if TYPE_CHECKING:
    # Provide stubs for either version of Pydantic

    from enum import Enum
    from typing import Any, Literal, Type, TypedDict

    from pydantic import BaseModel
    from pydantic import ConfigDict as PydanticConfigDict

    def ConfigDict(
        extra: Literal["allow", "ignore", "forbid"] = "allow",
        json_schema_extra: dict[str, Any] | None = None,
        populate_by_name: bool = True,
    ) -> PydanticConfigDict:
        ...

    class Extra(Enum):
        allow = "allow"
        ignore = "ignore"
        forbid = "forbid"

    class RootModel(BaseModel):
        ...

    JsonSchemaMode = Literal["validation", "serialization"]

    def models_json_schema(
        models: list[tuple[Type[BaseModel], JsonSchemaMode]],
        *,
        by_alias: bool = True,
        ref_template: str = "#/$defs/{model}",
    ) -> tuple[dict, dict[str, Any]]:
        ...

    def v1_schema(
        models: list[Type[BaseModel]],
        *,
        by_alias: bool = True,
        ref_prefix: str = "#/$defs",
    ) -> dict[str, Any]:
        ...

    DEFS_KEY = "$defs"

    class MinLengthArg(TypedDict):
        pass

    def min_length_arg(min_length: int) -> MinLengthArg:
        ...

elif PYDANTIC_V2:
    from typing import Literal, TypedDict

    from pydantic import ConfigDict, RootModel
    from pydantic.json_schema import JsonSchemaMode, models_json_schema

    # Pydantic 2 renders JSON schemas using the keyword "$defs"
    DEFS_KEY = "$defs"

    class MinLengthArg(TypedDict):
        min_length: int

    def min_length_arg(min_length: int) -> MinLengthArg:
        return {"min_length": min_length}

    # Create V1 stubs
    Extra = None
    v1_schema = None


else:
    from typing import TypedDict

    from pydantic import Extra
    from pydantic.schema import schema as v1_schema

    # Pydantic 1 renders JSON schemas using the keyword "definitions"
    DEFS_KEY = "definitions"

    class MinLengthArg(TypedDict):
        min_items: int

    def min_length_arg(min_length: int) -> MinLengthArg:
        return {"min_items": min_length}

    # Create V2 stubs
    ConfigDict = None
    Literal = None
    models_json_schema = None
    JsonSchemaMode = None
    RootModel = None


__all__ = [
    "Literal",
    "ConfigDict",
    "JsonSchemaMode",
    "models_json_schema",
    "RootModel",
    "Extra",
    "v1_schema",
    "DEFS_KEY",
    "min_length_arg",
]