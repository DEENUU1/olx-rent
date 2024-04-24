from dataclasses import dataclass
from typing import Optional


@dataclass
class Offer:
    title: str
    url: str
    map_url: Optional[str]
    district: Optional[str]
    price: Optional[str]
