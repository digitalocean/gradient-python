# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["DropletAddParams"]


class DropletAddParams(TypedDict, total=False):
    droplet_ids: Required[Iterable[int]]
    """An array containing the IDs of the Droplets to be assigned to the firewall."""
