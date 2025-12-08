# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["APIWebCrawlerDataSource"]


class APIWebCrawlerDataSource(BaseModel):
    """WebCrawlerDataSource"""

    base_url: Optional[str] = None
    """The base url to crawl."""

    crawling_option: Optional[Literal["UNKNOWN", "SCOPED", "PATH", "DOMAIN", "SUBDOMAINS", "SITEMAP"]] = None
    """Options for specifying how URLs found on pages should be handled.

    - UNKNOWN: Default unknown value
    - SCOPED: Only include the base URL.
    - PATH: Crawl the base URL and linked pages within the URL path.
    - DOMAIN: Crawl the base URL and linked pages within the same domain.
    - SUBDOMAINS: Crawl the base URL and linked pages for any subdomain.
    - SITEMAP: Crawl URLs discovered in the sitemap.
    """

    embed_media: Optional[bool] = None
    """Whether to ingest and index media (images, etc.) on web pages."""

    exclude_tags: Optional[List[str]] = None
    """Declaring which tags to exclude in web pages while webcrawling"""
