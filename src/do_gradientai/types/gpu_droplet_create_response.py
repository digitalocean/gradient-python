# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .shared.droplet import Droplet
from .shared.action_link import ActionLink

__all__ = [
    "GPUDropletCreateResponse",
    "SingleDropletResponse",
    "SingleDropletResponseLinks",
    "MultipleDropletResponse",
    "MultipleDropletResponseLinks",
]


class SingleDropletResponseLinks(BaseModel):
    actions: Optional[List[ActionLink]] = None


class SingleDropletResponse(BaseModel):
    droplet: Droplet

    links: SingleDropletResponseLinks


class MultipleDropletResponseLinks(BaseModel):
    actions: Optional[List[ActionLink]] = None


class MultipleDropletResponse(BaseModel):
    droplets: List[Droplet]

    links: MultipleDropletResponseLinks


GPUDropletCreateResponse: TypeAlias = Union[SingleDropletResponse, MultipleDropletResponse]
