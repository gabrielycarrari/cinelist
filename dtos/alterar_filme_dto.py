from pydantic import BaseModel, field_validator
from datetime import date, datetime, timedelta

from util.validators import *


class AlterarFilmeDTO(BaseModel):
    id: int
    nome: str
    sinopse: str
    id_genero: int
    avaliacao: str

    @field_validator("nome")
    def validar_nome(cls, v):
        msg = is_not_none(v, "Nome")
        if not msg:
            msg = is_not_empty(v, "Nome")
        if msg:
            raise ValueError(msg)
        return v

    @field_validator("sinopse")
    def validar_sinopse(cls, v):
        msg = is_max_size(v, "Sinopse", 255)
        if msg:
            raise ValueError(msg)
        return v

    @field_validator("id_genero")
    def validar_genero(cls, v):
        msg = is_selected_id_valid(v, "Gênero")
        if msg:
            raise ValueError(msg)
        return v