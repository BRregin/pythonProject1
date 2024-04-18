import nltk
import pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
# Загрузить данные из базы данных
data = pd.read_excel("C:/Users/Lenovo/PycharmProjects/pythonProject1/обновленный_файл.xlsx")
# Предварительная обработка текста(для запроса пользователя)
def preprocess_text(text):
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word not in stopwords.words('russian')]
    return ' '.join(filtered_words)
# Привязка ключевых слов к категориям ноутбуков
categories = {
    'Большой экран': ['большой экран', 'широкий экран'],
    'Яркий дисплей': ['яркий дисплей', 'яркий экран'],
    'Домашняя версия': ['домашняя версия', 'home edition'],
    'Шустрый': ['шустрый', 'быстрый', 'производительный'],
    'Хорошая память': ['хорошая память', 'память больше 256 гб'],
    'Видеокарта': ['видеокарта']
}
# Поиск соответствующих категорий для запроса пользователя
def find_matching_categories(query):
    preprocessed_query = preprocess_text(query)
    matching_categories = []
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in preprocessed_query:
                matching_categories.append(category)
                break
    return matching_categories
# Функция для поиска ноутбуков по признакам
def find_matching_notebooks(user_query, data):
    matching_notebooks = []
    for index, notebook in data.iterrows():
        try:
            if 'легкий' in user_query.lower() and 'игровой' in user_query.lower():
                if 1 <= notebook['Weight'] <= 2 and notebook['Category'] == 'gaming':
                    matching_notebooks.append(notebook)
            elif 'небольшой' in user_query.lower() and 'недорогой' in user_query.lower():
                if notebook['Screen Size'] <= 15.4 and notebook['Weight'] <= 3 and notebook['Price (Euros)'] <= 1000:
                    matching_notebooks.append(notebook)
            elif 'небольшой' in user_query.lower() and 'игровой' in user_query.lower():
                if notebook['Screen Size'] <= 15.4 and notebook['Category'] == 'gaming':
                    matching_notebooks.append(notebook)
            elif 'хорошая память' in user_query.lower() and 'видеокарта' in user_query.lower():
                if notebook['Storage'] >= 256 and notebook['GPU'] != 'None':
                    matching_notebooks.append(notebook)
            elif 'игровой' in user_query.lower() and 'видеокарта' in user_query.lower():
                if notebook['Category'] == 'gaming' and notebook['GPU'] != 'None':
                    matching_notebooks.append(notebook)
            else:
                # Если не заданы конкретные комбинации критериев, то ищем ноутбуки по каждому критерию отдельно
                if 'легкий' in user_query.lower():
                    if 1 <= notebook['Weight'] <= 2:
                        matching_notebooks.append(notebook)
                if 'небольшой' in user_query.lower():
                    if notebook['Screen Size'] <= 15.4 and notebook['Weight'] <= 3:
                        matching_notebooks.append(notebook)
                if 'недорогой' in user_query.lower():
                    if notebook['Price (Euros)'] <= 1000:
                        matching_notebooks.append(notebook)
                if 'классика' in user_query.lower():
                    if notebook['Category'] == 'notebook':
                        matching_notebooks.append(notebook)
                if 'ультрабук' in user_query.lower():
                    if notebook['Category'] == 'ultrabook':
                        matching_notebooks.append(notebook)
        except ValueError:
            print(f"Не удалось преобразовать вес в числовой формат: {notebook['Weight']}")
    return matching_notebooks
# Пример запроса пользователя
user_query = "Небольшой игровой ноутбук с видеокартой"
# Рекомендация ноутбуков для пользователя
recommended_notebooks = find_matching_notebooks(user_query, data)
if recommended_notebooks:
    print("Рекомендуемые ноутбуки:")
    for notebook in recommended_notebooks:
        print(notebook['Manufacturer'],notebook['Model Name'],notebook['Category'],'#Screen Size=',notebook['Screen Size'],'#Weight=', notebook['Weight'], notebook['GPU'], '#Price (Euros)=', notebook['Price (Euros)'])
        #print(notebook['Manufacturer'], '     ', notebook['Model Name'], '       ', notebook['Category'], '       ', '#Screen Size=', notebook['Screen Size'], '                      ', '#Weight=', notebook['Weight'])
else:
    print("Извините, не удалось найти подходящие ноутбуки.")
    #data = pd.read_csv("C:/Users/antip/PycharmProjects/TEAMwork/обновленный_файл999.xlsx", encoding='cp1251')
df = pd.read_csv("C:/Users/Lenovo/PycharmProjects/pythonProject1/laptops.csv", encoding='latin1')
df['Operating System Version'] = df['Operating System Version'].fillna('no')
# Привести все значения к нижнему регистру и удалить пробелы
df = df.apply(lambda x: x.astype(str).str.lower().str.strip())
df['Screen Size'] = df['Screen Size'].str.replace('"', '').str.replace("'", '')
df['RAM'] = df['RAM'].str.replace(r'\D', '', regex=True)
df['Weight'] = df['Weight'].str.replace(r'[^\d.,]+', '', regex=True)
# Сохранить обновленную таблицу без пробелов в файл Excel
df.to_excel('обновленный_файл1.xlsx', index=False, columns=df.columns, engine='openpyxl')
# Проверка наличия пропущенных значений
df = pd.read_excel("C:/Users/Lenovo/PycharmProjects/pythonProject1/обновленный_файл.xlsx", engine='openpyxl')
print(df.isnull().sum())