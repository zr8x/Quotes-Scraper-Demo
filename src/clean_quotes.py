import json
import pandas as pd

content = ''
with open("quotes.json", "r") as file:
    content = file.read()

data = json.loads(content)

df = pd.DataFrame(data)

duplicate_dicts = df[df.duplicated(subset=["text","author"])].to_dict(orient='records')

print("Duplicated datasets: ")
print(duplicate_dicts)

print("\nPurging...")

df_cleaned = df[~df.duplicated(subset=["text","author"])]

cleaned_dicts = df_cleaned.to_dict(orient='records')

print("Done purging, writing to file...")

with open("quotes.json", "w", encoding="utf-8") as file:
    json.dump(cleaned_dicts, file, indent=4, ensure_ascii=False)
    print("Finished writing to file.")

print("\nDone.")