# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .firewall_param import FirewallParam

__all__ = ["FirewallCreateParams", "Body"]


class FirewallCreateParams(TypedDict, total=False):
    body: Body


class Body(FirewallParam, total=False):
    pass
