from playwright.sync_api import sync_playwright
import pandas as pd
from tqdm import trange
import time

def scrape_website(url, num_pages=1):

    base_url = "https://webscraper.io"
    df = pd.DataFrame(columns=["Title", "Description", "Storage", "Price", "Review"])

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True, slow_mo=0) # Cambia a True al finalizar pruebas
        page = browser.new_page()
        page.goto(url)
        page.click("button.acceptCookies")
        
        for _ in trange(num_pages, desc="Scraping pages", unit="page", leave=False):
            
            for article in page.query_selector_all("div.thumbnail"):
                article_url = article.query_selector("a").get_attribute("href")

                if article_url is not None:
                    p = browser.new_page(base_url=base_url)
                    p.goto(article_url)
                    p.click("button.acceptCookies")

                    if p.query_selector("button.btn.swatch") is None:
                        # En caso de no haber opciones de almacenamiento, se asigna un valor por defecto
                        # Caso especifico para la categoria de telefonos
                        title = p.query_selector("h4.title.card-title").inner_text()
                        description = p.query_selector("p.description.card-text").inner_text()
                        price = p.query_selector("h4.price.float-end.pull-right").inner_text()
                        rating = len(p.query_selector_all("span.ws-icon.ws-icon-star"))
                        df = pd.concat([df, pd.DataFrame([{"Title": title, "Description": description, "Storage": "N/A", "Price": price, "Review": rating}])], ignore_index=True)

                    for swatch in p.query_selector_all("button.btn.swatch"):

                        if swatch.is_disabled():
                            continue

                        swatch.click()
                        title = p.query_selector("h4.title.card-title").inner_text()
                        description = p.query_selector("p.description.card-text").inner_text()
                        storage = p.query_selector("button.btn.swatch.btn-primary.active").get_attribute("value")
                        price = p.query_selector("h4.price.float-end.pull-right").inner_text()
                        rating = len(p.query_selector_all("span.ws-icon.ws-icon-star"))
                        df = pd.concat([df, pd.DataFrame([{"Title": title, "Description": description, "Storage": storage, "Price": price, "Review": rating}])], ignore_index=True)

                    p.close()
         
            next_button = page.query_selector("button.btn.btn-default.next")

            if next_button is not None and not next_button.is_disabled():
                next_button.click()
                # Espera a que el contenido se cargue antes de continuar
                page.wait_for_selector('div[data-type="ajax"]', state="visible", timeout=10000)
                time.sleep(0.5)  # Espera adicional para asegurar que el contenido se haya cargado completamente
            else:
                print("Se revisaron todas las paginas disponibles.")
                break    
        browser.close()

    return df
