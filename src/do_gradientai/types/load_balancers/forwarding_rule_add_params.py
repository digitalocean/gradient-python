# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..forwarding_rule_param import ForwardingRuleParam

__all__ = ["ForwardingRuleAddParams"]


class ForwardingRuleAddParams(TypedDict, total=False):
    forwarding_rules: Required[Iterable[ForwardingRuleParam]]
