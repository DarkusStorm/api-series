# Modelo para o banco de dados

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class SerieModel(Base):
    __tablename__ = "serie"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str] = mapped_column(String(255))
    ano_lancamento: Mapped[int] = mapped_column(Integer)
    # "Mapped" indica ao SQL Alchemy que o atributo é mapeado/ligado a um banco de dados ou relacionamento. "mapped_column" indica a coluna que será mapeada.