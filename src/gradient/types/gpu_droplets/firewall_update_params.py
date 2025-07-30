# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .firewall_param import FirewallParam

__all__ = ["FirewallUpdateParams"]


class FirewallUpdateParams(TypedDict, total=False):
    firewall: Required[FirewallParam]
