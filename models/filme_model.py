from dataclasses import dataclass
from typing import Optional

from models.genero_model import Genero


@dataclass
class Filme():
    id: Optional[int] = None
    nome: Optional[str] = None
    sinopse: Optional[str] = None
    genero: Optional[Genero] = None
    avaliacao: Optional[str] = None
  