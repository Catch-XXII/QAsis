from pydantic import BaseModel


class BaseResponse(BaseModel):
    """
    All API response models should inherit from this class.
    Provides validation, parsing, and serialization out of the box.
    """

    pass
