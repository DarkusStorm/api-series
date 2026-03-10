from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.serie import SerieModel
from app.schema.serie import SerieSchema, UpdateSerie
from typing import cast

serie = APIRouter()

@serie.post("/")
async def criar_serie(dados: SerieSchema, db: Session = Depends(get_db)):
    nova_serie = SerieModel(**dados.model_dump()) ## "**" significa que diversos argumentos serão repassados sequencialmente;
    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)
    return nova_serie

@serie.get("/series")
async def listar_series(db: Session = Depends(get_db)):
    return db.query(SerieModel).all()

@serie.delete("/series/delete/{id}")
async def deletar_series(id: int, db: Session = Depends(get_db)):
    db.query(SerieModel).filter(SerieModel.id == id).delete()
    db.commit()
    return db.query(SerieModel).all()

@serie.put("/series/update/{id}")
async def atualizar_serie(id: int, dados: UpdateSerie, db: Session = Depends(get_db)):
    serie = cast(SerieModel, db.query(SerieModel).filter(SerieModel.id == id).first()) # "First" garante que apenas o primeiro resultado será retornado, não toda a lista (all());

    if not serie:
        return {"erro": "Série não encontrada."}
    
    # Verifica se, no request, foi fornecido algum título. Se sim, substitui o atual. O mesmo se aplica para descrição e ano de lançamento.
    if dados.titulo is not None:
        serie.titulo = dados.titulo

    if dados.descricao is not None:
        serie.descricao = dados.descricao

    if dados.ano_lancamento is not None:
        serie.ano_lancamento = dados.ano_lancamento

    db.commit()
    db.refresh(serie)

    return serie