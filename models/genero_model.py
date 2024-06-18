from dataclasses import dataclass
from typing import Optional


@dataclass
class Genero():
    id: Optional[int] = None
    nome: Optional[str] = None