import datetime
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Params:
    name: str
    label: str


@dataclass
class Price:
    value: float
    # currency: str


@dataclass
class Object:
    url: str
    title: str
    created_time: datetime.datetime
    city: Optional[str] = None
    district: Optional[str] = None
    region: Optional[str] = None
    price: Optional[Price] = None
    params: Optional[List[Params]] = None
    rent: Optional[Price] = None
