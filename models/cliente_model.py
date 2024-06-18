from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Cliente:
    id: Optional[int] = None
    nome: Optional[str] = None
    email: Optional[str] = None
    senha: Optional[str] = None
    token: Optional[str] = None
