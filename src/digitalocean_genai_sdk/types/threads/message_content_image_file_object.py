# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MessageContentImageFileObject", "ImageFile"]


class ImageFile(BaseModel):
    file_id: str
    """The [File](/docs/api-reference/files) ID of the image in the message content.

    Set `purpose="vision"` when uploading the File if you need to later display the
    file content.
    """

    detail: Optional[Literal["auto", "low", "high"]] = None
    """Specifies the detail level of the image if specified by the user.

    `low` uses fewer tokens, you can opt in to high resolution using `high`.
    """


class MessageContentImageFileObject(BaseModel):
    image_file: ImageFile

    type: Literal["image_file"]
    """Always `image_file`."""
