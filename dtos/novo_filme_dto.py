from pydantic import BaseModel, field_validator
from datetime import date, datetime, timedelta

from util.validators import *


class NovoFilmeDTO(BaseModel):
    nome: str
    sinopse: str
    id_genero: int
    avaliacao: str

