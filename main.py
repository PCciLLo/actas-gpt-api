from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from generar_acta import generar_acta
import tempfile
import os

app = FastAPI() 

class ActaInput(BaseModel):
    datos: dict

@app.post("/generar-acta")
def generar_acta_endpoint(input: ActaInput):
    try:
        print("📥 Datos recibidos:")
        print(input.datos)
        # Crear archivo temporal
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp:
            salida_path = temp.name

        # Ruta a tu plantilla
        plantilla_path = "plantilla_acta_con_marcadores_v4.1.docx"

        # Generar acta
        generar_acta(plantilla_path, salida_path, input.datos)

        # Leer el archivo generado
        with open(salida_path, "rb") as f:
            contenido = f.read()

        # Borrar el temporal
        os.remove(salida_path)

        return {
            "filename": os.path.basename(salida_path),
            "content": contenido.hex()  # lo devuelves como hexadecimal para transporte seguro
        }

    except Exception as e:
        print("❌ Error generado:")
        print(e)  # Log al terminal
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")