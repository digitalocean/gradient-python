# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["APIDeploymentVisibility"]

APIDeploymentVisibility: TypeAlias = Literal[
    "VISIBILITY_UNKNOWN", "VISIBILITY_DISABLED", "VISIBILITY_PLAYGROUND", "VISIBILITY_PUBLIC", "VISIBILITY_PRIVATE"
]
