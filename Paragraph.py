import requests
from transformers import T5Tokenizer, T5ForConditionalGeneration
import pandas as pd

def summarize_website(url):
    try:
        # Fetch website content
        response = requests.get(url)
        response.raise_for_status()
        content = response.text

        # Initialize tokenizer and model
        tokenizer = T5Tokenizer.from_pretrained("t5-base", model_max_length=512)
        model = T5ForConditionalGeneration.from_pretrained("t5-base")

        # Tokenize and encode the input text
        inputs = tokenizer.encode("summarize: " + content, return_tensors="pt", truncation=True)

        # Generate the summary
        summary_ids = model.generate(inputs, max_length=100, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return summary

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Read the Excel file
df = pd.read_excel(r"C:\Users\deepa\Desktop\Project\Company URL data.xlsx", engine='openpyxl')

# Access the 'Website' column
column_data = df['Company URL']

# Create a new column for summaries
df['Summary'] = ""

# Generate summaries for each URL
for index, url in enumerate(column_data):
    summary = summarize_website(url)
    df.at[index, 'Summary'] = summary 

# Save the updated dataframe to a new Excel file
df.to_excel(r"C:\Users\deepa\Desktop\Project\Company URL data with summary.xlsx", index=False)
