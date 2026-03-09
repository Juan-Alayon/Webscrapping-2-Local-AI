# Webscrapping-2-Local-AI 🤖

Sistema de web scraping inteligente que extrae datos de productos de e-commerce y genera análisis automáticos usando IA local. Combina **Playwright** para scraping con **LMStudio** para análisis de datos obtenidos con posibilidad de comparación de modelos.

---

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Cómo Usar](#cómo-usar)
- [Categorías Disponibles](#categorías-disponibles)
- [Configuración de LMStudio](#configuración-de-lmstudio)
- [Archivos de Salida](#archivos-de-salida)
- [Solución de Problemas](#solución-de-problemas)
- [Dependencias Principales](#dependencias-principales)

---

<a name="descripción"></a>
## 📖 Descripción

Este proyecto automatiza el proceso de:
1. **Web Scraping**: Extrae datos de productos de un sitio de prueba de e-commerce con paginación AJAX
2. **Procesamiento**: Organiza los datos en un archivo CSV
3. **Análisis IA**: Genera dos análisis automáticos:
   - Resumen conciso de los datos
   - Análisis detallado de tendencias y anomalías

**Fuente de datos**: [webscraper.io - E-commerce de Prueba](https://webscraper.io/test-sites/e-commerce/ajax)

---

<a name="requisitos"></a>

## ✅ Requisitos

### Software Obligatorio
- **Python**: 3.8 o superior
- **LMStudio**: Versión reciente (descarga desde [lmstudio.ai](https://lmstudio.ai))
- **Git** (opcional, para clonar el repositorio)


### Configuración de LMStudio
- ✅ LMStudio debe estar ejecutándose y accesible en `http://localhost:8000`
- ✅ Tener descargado mínimo un modelo LLM (ej: Deepseek, Llama, Mistral)
- ⚠️ Para muchas páginas (>5), aumentar `context-length` del modelo (recomendado: 8K-32K tokens)

---

<a name="instalación"></a>

## 🚀 Instalación

### Paso 1: Preparar el Repositorio
```bash
git clone <url-del-repositorio>
cd Webscrapping-2-Local-AI
```

### Paso 2: Crear Ambiente Virtual
```bash
# En Windows (PowerShell)
python -m venv Webscrapping-2-Local-AI

# Activar ambiente
.\Webscrapping-2-Local-AI\Scripts\Activate.ps1
```

```bash
# En macOS/Linux
python3 -m venv Webscrapping-2-Local-AI
source Webscrapping-2-Local-AI/bin/activate
```

### Paso 3: Instalar Dependencias
```bash
pip install -r requirements.txt
```

### Paso 4: Verificar Instalación
```bash
python -c "import playwright; import pandas; import lmstudio; print('✅ Instalación correcta')"
```

---

<a name="estructura-del-proyecto"></a>

## 📁 Estructura del Proyecto

```
Webscrapping-2-Local-AI/
├── README.md                          # Este archivo
├── requirements.txt                   # Dependencias Python
├── src/
│   ├── main.py                       # Script principal (interfaz de usuario)
│   ├── scrapper.py                   # Lógica de web scraping
│   └── summarizer.py                 # Lógica de análisis con IA
└── output/                            # 📤 Archivos generados
    ├── results.csv                   # Datos extraídos
    └── ai_summary.md                 # Análisis del modelo IA

```

---

<a name="cómo-usar"></a>

## 💻 Cómo Usar

### Inicio Rápido
1. **Asegurate que LMStudio esté ejecutándose** ⚠️
2. Ejecuta el script principal:
```bash
python src/main.py
```

### Flujo Interactivo
El programa te guiará con un menú paso a paso:

**Paso 1**: Selecciona categoría
```
Bienvenido al scraper de productos. Por favor, elija una categoría:
1. Computadores
2. Teléfonos
Ingrese el número: 1
```

**Paso 2**: Selecciona subcategoría
```
Elija la subcategoría de computadores:
1. Laptops
2. Tablets
Ingrese el número: 1
```

**Paso 3**: Define cantidad de páginas
```
Ingrese el numero de páginas que desea scrapear: 3
```

**Paso 4**: Selecciona modelo IA
```
Seleccione un modelo LLM para generar el resumen:
0. deepseek-r1-0528-qwen3-8b
1. llama-2-7b
Ingrese el número: 0
```

**Resultado**: Se generan archivos en la carpeta `output/`

---

<a name="categorías-disponibles"></a>

## 🏪 Categorías Disponibles

| Categoría | Subcategorías | URL |
|-----------|--------------|-----|
| **Computadores** | Laptops, Tablets | `/computers/laptops`, `/computers/tablets` |
| **Teléfonos** | Touch Phones | `/phones/touch` |

### Ejemplos de URLs
- Laptops: `https://webscraper.io/test-sites/e-commerce/ajax/computers/laptops`
- Tablets: `https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets`
- Teléfonos: `https://webscraper.io/test-sites/e-commerce/ajax/phones/touch`

---

<a name="configuración-de-lmstudio"></a>

## ⚙️ Configuración de LMStudio

### Paso 1: Descargar e Instalar
1. Visita [lmstudio.ai](https://lmstudio.ai) descarga la versión para tu SO
2. Instala y abre LMStudio

### Paso 2: Descargar un Modelo
1. En la pestaña "Models" busca un modelo (recomendados: deepseek, llama, mistral)
2. Haz clic en "Download"
3. Espera a que se descargue completamente

### Paso 3: Iniciar el Servidor
1. Ve a la pestaña "Local Server"
2. Selecciona el modelo descargado
3. Haz clic en "Start Server"
4. Deberías ver: `Server listening at http://localhost:8000`

### Paso 4: Aumentar Context Length (Opcional)
Para scrapear muchas páginas sin errores:
1. Haz clic en ⚙️ (configuración) del modelo
2. Busca `context_length`
3. Aumenta a 8192-32768 según tu RAM disponible
4. Reinicia el servidor

---

<a name="archivos-de-salida"></a>

## 📤 Archivos de Salida

La carpeta `output/` contiene dos archivos:

### 1️⃣ `results.csv`
Datos brutos del scraping en formato tabular:

| Columna | Descripción | Ejemplo |
|---------|------------|---------|
| **Title** | Nombre del producto | "Dell Latitude 5520" |
| **Description** | Especificaciones técnicas | "15.6 inch, Intel Core i7" |
| **Storage** | Espacio de almacenamiento (si aplica) | "512GB SSD" |
| **Price** | Precio del producto | "$899.99" |
| **Review** | Calificación de usuarios | "4.5/5" |

**Uso**: Importa a Excel, Pandas, Power BI, etc.

### 2️⃣ `ai_summary.md`
Análisis inteligente generado por el modelo IA con:

#### 📊 Resumen Ejecutivo
- Síntesis concisa de los datos
- Origen de los datos
- Información clave

#### 🔍 Análisis Detallado
- **Relaciones precio-características**: Qué atributos influyen en el precio
- **Relaciones calificación-características**: Qué hace que un producto tenga buenas reseñas
- **Tendencias identificadas**: Patrones en los datos (ej: más almacenamiento = mejor precio)
- **Outliers y anomalías**: Productos extraños o con precios sospechosos
- **Errores en datos**: Inconsistencias o duplicados
- **Recomendaciones**: Insights adicionales útiles

---

<a name="solución-de-problemas"></a>

## 🐛 Solución de Problemas

### ❌ "ConnectionError: Cannot connect to LMStudio"
**Causa**: LMStudio no está ejecutándose o no escucha en `localhost:8000`

**Solución**:
1. Abre LMStudio
2. Selecciona un modelo
3. Haz clic en "Local Server" → "Start Server"
4. Verifica que aparezca `Server listening at http://localhost:8000`
5. Reinicia el script

---

### ❌ "Context length exceeded"
**Causa**: El modelo no tiene contexto suficiente para procesar tantas páginas

**Solución**:
1. Abre LMStudio
2. Haz clic en ⚙️ del modelo
3. Aumenta `context_length` a 16384 o 32768
4. Reinicia el servidor
5. O scrappea menos páginas (máximo 3-5)

---

### ❌ "No module named 'playwright'"
**Causa**: Las dependencias no se instalaron correctamente

**Solución**:
```bash
# Activa el ambiente virtual (si no está activo)
.\Webscrapping-2-Local-AI\Scripts\Activate.ps1

# Reinstala dependencias
pip install --upgrade -r requirements.txt

# Instala drivers de Playwright
playwright install
```

---

### ⏱️ "El scraping es muy lento"
**Causa**: Normal, especialmente en páginas grandes

**Soluciones**:
- Checkea tu conexión a internet
- Reduce el número de páginas
- Usa un modelo IA más pequeño en LMStudio
- Aumenta RAM disponible

---

<a name="dependencias-principales"></a>

## 📦 Dependencias Principales

| Librería | Versión | Propósito |
|----------|---------|----------|
| `playwright` | 1.58.0+ | Automatización del navegador para scraping |
| `pandas` | 3.0.1+ | Procesamiento y exportación de datos |
| `lmstudio` | 1.5.0+ | Conexión con servidor IA local |
| `tqdm` | 4.67.3+ | Barra de progreso visual |

**Instalación completa**: `pip install -r requirements.txt`

---

## 📝 Notas de Rendimiento

- **Tiempo estimado**: 30-120 segundos por página (varía según hardware)
- **Uso de RAM**: ~2-4 GB durante scraping + modelo IA (~6-12 GB)
- **Contexto recomendado**: 8K-32K tokens para análisis óptimo
- **Modelo recomendado**: Deepseek-R1, Llama-2, Mistral (8B-13B parámetros)

---

## 🎯 Ejemplos de Uso

### Analizar Laptops (3 páginas)
```
1. Categoría → 1 (Computadores)
2. Subcategoría → 1 (Laptops)
3. Páginas → 3
4. Modelo → deepseek-r1-0528-qwen3-8b
```

### Analizar Teléfonos (2 páginas)
```
1. Categoría → 2 (Teléfonos)
2. Páginas → 2
3. Modelo → Tu modelo preferido
```

---

## 📄 Licencia

Este proyecto utiliza datos de prueba de [webscraper.io](https://webscraper.io) únicamente con propósitos educativos.


    

