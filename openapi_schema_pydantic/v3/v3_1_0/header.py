from pydantic import Extra, Field

from .parameter import Parameter, ParameterLocation


class Header(Parameter):
    """
    The Header Object follows the structure of the [Parameter Object](#parameterObject)
    with the following changes:

    1. `name` MUST NOT be specified, it is given in the corresponding `headers` map.
    2. `in` MUST NOT be specified, it is implicitly in `header`.
    3. All traits that are affected by the location MUST be applicable to a location of
       `header` (for example, [`style`](#parameterStyle)).
    """

    name: str = Field(default="", const=True)
    param_in: ParameterLocation = Field(
        default=ParameterLocation.HEADER, const=True, alias="in"
    )

    class Config:
        extra = Extra.allow
        allow_population_by_field_name = True
        schema_extra = {
            "examples": [
                {
                    "description": "The number of allowed requests in the current "
                    "period",
                    "schema": {"type": "integer"},
                }
            ]
        }
