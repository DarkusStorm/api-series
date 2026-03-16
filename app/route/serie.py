from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.serie import SerieModel
import app.schema.serie

serie = APIRouter()

@serie.post("/")
async def criar_serie(dados: app.schema.serie.SerieSchema, db: Session = Depends(get_db)):
    nova_serie = SerieModel(**dados.model_dump()) ## "**" significa que diversos argumentos serão repassados sequencialmente;
    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)
    return nova_serie

@serie.get("/series")
async def listar_series(db: Session = Depends(get_db)):
    return db.query(SerieModel).all()

@serie.delete("/series/{id}/delete")
async def deletar_series(id: int, db: Session = Depends(get_db)):
    serie = db.query(SerieModel).filter(SerieModel.id == id).first()

    if not serie:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Série com ID {id} não encontrada."
        )
    
    db.delete(serie)
    db.commit()
    return {
        "resposta": f"Serie com ID {id} apagada com sucesso.",
        "series": db.query(SerieModel).all()
    }

@serie.put("/series/{id}/update")
async def atualizar_serie(id: int, dados: app.schema.serie.SerieUpdateSchema, db: Session = Depends(get_db)):
    serie = db.query(SerieModel).filter(SerieModel.id == id).first() # "First" garante que apenas o primeiro resultado será retornado, não toda a lista (all());

    # Verifica se há uma série com o ID fornecido.
    if not serie:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Série com ID {id} não encontrada."
        )
    
    # Verifica se, no request, foi fornecido algum título. Se sim, substitui o atual. O mesmo se aplica para descrição e ano de lançamento.
    for campo, valor in dados.model_dump().items():
        setattr (serie, campo, valor or None)
    
    db.commit()
    db.refresh(serie)

    return serie