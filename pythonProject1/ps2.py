import pandas as pd
# Загрузить данные из файла CSV с указанием кодировки
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
df = pd.read_excel("C:/Users/antip/PycharmProjects/preprocessing/обновленный_файл1.xlsx", engine='openpyxl')print(df.isnull().sum())