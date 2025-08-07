# 📝 ActasGPT API

**ActasGPT** es una API construida con FastAPI que genera actas de reuniones en formato `.docx` a partir de una plantilla de Word y un conjunto de datos estructurados en JSON.

Esta API está diseñada para integrarse con un GPT personalizado, permitiendo automatizar la redacción de actas directamente desde una conversación con IA.

---

## 🚀 Funcionalidades

- Recibe los datos de una reunión (asunto, fecha, participantes, agenda, etc.)
- Rellena una plantilla `.docx` (`plantilla_acta_con_marcadores_v4.1.docx`)
- Devuelve el archivo generado como documento Word
- Integra vía OpenAPI con GPTs personalizados

---

## 📁 Estructura del proyecto

```
actas-gpt-api/
├── __init__.py                         # Marca el directorio como módulo Python
├── docs/
│   └── openapi.json                    # Esquema OpenAPI para conectar con GPT
├── generar_acta.py                    # Lógica para generar el acta a partir de datos y plantilla
├── main.py                            # Punto de entrada FastAPI y definición de endpoints
├── plantilla_acta_con_marcadores_v4.1.docx  # Plantilla base para el acta
├── README.md                          # Este archivo
├── requirements.txt                   # Dependencias necesarias
└── test/
    └── response_1754560663406.json    # Respuesta de prueba local
```

---

## ⚙️ Requisitos

- Python 3.9+
- pip (`pip3` en macOS)

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## 🧪 Ejecutar localmente

Desde la raíz del proyecto:

```bash
uvicorn main:app --reload
```

Abre en navegador:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🤖 Integración con GPT personalizado

El archivo [`docs/openapi.json`](docs/openapi.json) contiene el esquema necesario para conectar esta API con tu GPT.

Desde el GPT Builder:

1. Añadir una acción
2. Seleccionar "Escribir el esquema OpenAPI"
3. Pegar el contenido de `openapi.json`

---

## 📥 Ejemplo de payload

```json
{
  "datos": {
    "ASUNTO": "Reunión de kickoff",
    "FECHA": "08/08/2025",
    "CLIENTE": "Infokode",
    "HORA_INICIO": "10:00",
    "HORA_FIN": "11:30",
    "PROYECTO": "Automatización de actas",
    "TIPO_REUNION": "Videollamada",
    "ID_PROYECTO": "ACTAS-IA-2025",
    "OBJETIVO": "Definir plan inicial del proyecto",
    "AGENDA": "- Presentación\n- Planificación\n- Entregables",
    "TEMAS": [
      "Se presentó el objetivo del proyecto.",
      "Se debatieron las herramientas a utilizar."
    ],
    "ACUERDOS": [
      "Primera demo el 16/08.",
      "Uso de FastAPI + GPT para generación automática."
    ],
    "PARTICIPANTES": [
      {"id": "1", "asistente": "Daniel Ramos", "iniciales": "DR", "compania": "Infokode"},
      {"id": "2", "asistente": "Laura Martín", "iniciales": "LM", "compania": "Consultora UX"}
    ],
    "PROXIMOS_PASOS": [
      {
        "responsable": "Daniel",
        "titulo": "Subir versión inicial",
        "descripcion": "Montar lógica básica y desplegar",
        "fecha": "10/08/2025",
        "estado": "En curso"
      }
    ]
  }
}
```

---

## 📄 Licencia

MIT © 2025 [Daniel Ramos / Infokode]
