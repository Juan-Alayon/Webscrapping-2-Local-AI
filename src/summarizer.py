import lmstudio as lms

prompt1 = "Resume el siguiente documento de manera concisa y legible. Explica de donde se pudo haber obtenido y que información relevante deberia saber:\n\n"
prompt2 = """\n\n\n Eres un analista de datos experto en e-commerce. Analiza el siguiente documento y proporciona un análisis detallado de los productos listados, incluyendo pero no limitado a:
- Relación entre caracteristicas de los productos y su precio
- Relación entre caracteristicas de los productos y su calificación
- Identificación de tendencias en los productos (por ejemplo, si los productos con más almacenamiento tienden a tener mejores calificaciones)
- Identificación de posibles outliers o productos atípicos en términos de precio o calificación
- Error en los datos (por ejemplo, productos con precios extremadamente bajos o altos que podrían ser errores de entrada de datos, productos cuya descripción no coincide con sus características o productos repetidos)
- Cualquier otro análisis relevante que pueda proporcionar información útil sobre los productos listados en el documento.
\n\n"""

def generate_summary(document, model):
    llm1 = lms.llm(model.model_key, 
                           config={"contextLength": 32768})
    summary = llm1.respond(prompt1 + document)
    
    llm2 = lms.llm(model.model_key, 
                           config={"contextLength": 32768})
    analysis = llm2.respond(prompt2 + document)
    
    # Combinar en Markdown
    md_content = f"""# Análisis Completo del Documento de Productos

## Resumen Ejecutivo
{summary}

## Análisis Detallado
{analysis}
"""
    return md_content

