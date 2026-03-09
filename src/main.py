import scrapper
import summarizer
from pathlib import Path

def main():

    # Interfaz de usuario para seleccionar categoría y subcategoría
    print("Bienvenido al scraper de productos de laptops y teléfonos. Por favor, elija una categoría:")
    print("1. Computadores")
    print("2. Teléfonos")
    categoria = input("Ingrese el número de la categoría que desea scrapear: ")

    if categoria == "1":
        print("Elija la subcategoría de computadores:")
        print("1. Laptops")
        print("2. Tablets")
        subcategoria = input("Ingrese el número de la subcategoría que desea scrapear: ")
        
        if subcategoria == "1":
            url = "https://webscraper.io/test-sites/e-commerce/ajax/computers/laptops"
        elif subcategoria == "2":            
            url = "https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets"
        else:
            print("Opción no válida. Saliendo del programa.")
            return
    elif categoria == "2":
        url = "https://webscraper.io/test-sites/e-commerce/ajax/phones/touch"
    else:
        print("Opción no válida. Saliendo del programa.")
        return
    
    num_pages = int(input("Ingrese el numero de páginas que desea scrapear: "))

    if num_pages < 1:
        print("Número de páginas no válido. Saliendo del programa.")
        return
    
    if num_pages > 5:
        print("Número de páginas demasiado alto. El proceso podra tardar demasiado tiempo y cosumira muchos recursos.")
        quiery = input("¿Desea continuar? (s/n): ")
        
        if quiery.lower() != "s":
            print("Saliendo del programa.")
            return
        else:
            print("Continuando con el proceso de scraping...")

    # Scraping de datos
    print("Iniciando el proceso de scraping...")
    df = scrapper.scrape_website(url, num_pages=num_pages)

    # Guardado de datos en CSV
    project_root = Path(__file__).parent.parent 
    output_dir = project_root / "output"
    output_dir.mkdir(exist_ok=True)  # crea si no existe
    output_file = output_dir / "results.csv"
    df.to_csv(output_file, index=False)
    print("Scraping completado. Los datos se han guardado en: ", output_file)

    # Lectura del archivo CSV para mostrar un resumen
    with open(output_file, "r", encoding='utf-8') as file:
        document = file.read()

    # Interfaz de usuario para seleccionar modelo LLM para generar el resumen
    list_of_llms = summarizer.lms.list_downloaded_models("llm")
    print("Seleccione un modelo LLM para generar el resumen:")

    for index, model in enumerate(list_of_llms):
        print(f"{index}. {model.model_key}")

    model_index = int(input("Ingrese el número del modelo que desea usar: "))
    selected_model = list_of_llms[model_index]
    print(f"Generando resumen con el modelo: {selected_model.model_key}")

    # Generación del resumen
    summary = summarizer.generate_summary(document, selected_model)
    print("Resumen generado")

    # Guardado del resumen en un archivo Markdown
    output_file = output_dir / "ai_summary.md"
    with open(output_file, "w", encoding='utf-8') as file:
        file.write(summary)
    print("El resumen se ha guardado en: ", output_file)

if __name__ == "__main__":
    main()