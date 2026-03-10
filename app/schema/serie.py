# Modelo ed validação de dados com Pydantic
from pydantic import BaseModel
from typing import Optional

class SerieSchema(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    ano_lancamento: int

    class Config:
        from_attributes = True

class UpdateSerie(BaseModel):
    titulo: Optional[str]
    descricao: Optional[str]
    ano_lancamento: Optional[int]

    # Classe para atualizar Séries, onde todos os valores são opcionais pois não é obrigatório atualizar todos eles ao executar serie.put