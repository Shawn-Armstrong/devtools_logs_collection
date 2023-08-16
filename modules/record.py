from typing import Optional
from dataclasses import dataclass

@dataclass
class Record:
    endpoint: str
    testing_url: Optional[str] = None
    production_url: Optional[str] = None
    testing_logs: Optional[dict] = None
    production_logs: Optional[dict] = None
