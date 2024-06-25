from dataclasses import dataclass
from typing import Optional

from models.genero_model import Genero
from models.cliente_model import Cliente


@dataclass
class Filme():
    id: Optional[int] = None
    nome: Optional[str] = None
    sinopse: Optional[str] = None
    genero: Optional[Genero] = None
    cliente: Optional[Cliente] = None
    avaliacao: Optional[str] = None
  