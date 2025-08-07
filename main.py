from fastapi import FastAPI
from pydantic import BaseModel
from generar_acta import generar_acta
import uuid
import os

app = FastAPI()

class ActaInput(BaseModel):
    datos: dict

@app.post("/generar-acta")
def generar(data: ActaInput):
    # Ruta de la plantilla (debe estar en el mismo directorio del proyecto)
    plantilla = "plantilla_acta_con_marcadores_v4.1.docx"
    nombre_salida = f"acta-{uuid.uuid4().hex}.docx"

    generar_acta(plantilla, nombre_salida, data.datos)

    # Devolver archivo en binario como hex para simplicidad
    with open(nombre_salida, "rb") as f:
        contenido = f.read()

    # Opcional: eliminar archivo generado tras devolverlo
    os.remove(nombre_salida)

    return {
        "filename": nombre_salida,
        "content": contenido.hex()
    }