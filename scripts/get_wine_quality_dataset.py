import requests

# Ссылка для скачивания
url = "https://drive.google.com/uc?export=download&id=1W8CS4Y9tlMn3wF0GnxbedDzAO0kZohDx"

# Имя файла, под которым сохранится скачанный файл
output_file = "wine_quality_dataset.csv"

try:
    # GET-запрос для загрузки файла
    response = requests.get(url)

    # Проверка успешности запроса (код 200 - успешный запрос)
    if response.status_code == 200:
        # Сохранение содержимого файла
        with open(output_file, "wb") as file:
            file.write(response.content)
        print(f"Файл '{output_file}' успешно скачан.")
    else:
        print(f"Ошибка: Не удалось скачать файл. Код состояния: {response.status_code}")
except Exception as e:
    print(f"Произошла ошибка при скачивании файла: {str(e)}")
