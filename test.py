from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicjalizacja przeglądarki
driver = webdriver.Chrome()  # Możesz zmienić na inną przeglądarkę, jeśli chcesz

# Otwarcie strony do testowania
url = "https://www.example.com"  # Zastąp adresem URL stroną, którą chcesz przetestować
driver.get(url)

# Znalezienie elementów o kolorze niebieskim
elements = driver.find_elements(By.CSS_SELECTOR, '[style*="color: blue"]')

# Wyświetlenie wyników
if elements:
    print("Znaleziono elementy o kolorze niebieskim:")
    for element in elements:
        print(f"- {element.text}")
else:
    print("Nie znaleziono elementów o kolorze niebieskim.")

# Zamknięcie przeglądarki
driver.quit()
