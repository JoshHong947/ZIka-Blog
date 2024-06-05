import pandas as pd
from googletrans import Translator

# 读取表格
df = pd.read_csv('your_file.csv')  # 替换为你的文件路径
translator = Translator()

# 定义目标语言列表
languages = ['es', 'fr', 'de', 'it', 'ja', 'ko', 'pt', 'ru', 'zh-cn', 'ar', 'hi', 'bn', 'vi']

# 创建一个新的DataFrame来存储翻译结果
translated_df = pd.DataFrame(columns=df.columns.tolist() + ['language'])

# 遍历每一行和每一种语言进行翻译
for index, row in df.iterrows():
    for lang in languages:
        translated_row = row.apply(lambda x: translator.translate(x, dest=lang).text)
        translated_row['language'] = lang
        translated_df = translated_df.append(translated_row, ignore_index=True)

# 保存翻译结果
translated_df.to_csv('translated_file.csv', index=False)  # 替换为你想保存的文件路径
