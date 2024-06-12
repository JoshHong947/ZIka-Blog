import pandas as pd
from googletrans import Translator

# Load the Excel file
file_path = 'Tag 3.0.xlsx'
data = pd.read_excel(file_path)

# Initialize the translator
translator = Translator()

# Languages to translate to
languages = ["de", "en", "sa", "fr", "ja", "ko", "pt", "ch", "vi", "nl", "ar", "pl"]

# Function to translate text
def translate_text(text, lang):
    try:
        translated = translator.translate(text, dest=lang)
        return translated.text
    except Exception as e:
        return text

# Including 'tag_name' in the translation process
def translate_columns(row, lang):
    row['tag_name'] = translate_text(row['tag_name'], lang)
    row['tag_title'] = translate_text(row['tag_title'], lang)
    row['tag_description'] = translate_text(row['tag_description'], lang)
    row['lang'] = lang
    return row

# Loop through each language and translate
translated_data = pd.DataFrame()

for lang in languages:
    temp_data = data.copy()
    temp_data = temp_data.apply(lambda row: translate_columns(row, lang), axis=1)
    translated_data = pd.concat([translated_data, temp_data], ignore_index=True)

# Save the translated data to a new Excel file
translated_file_path = '你的文件路径/Tag_Translated.xlsx'
translated_data.to_excel(translated_file_path, index=False)

print(f"Translated file saved to: {translated_file_path}")
