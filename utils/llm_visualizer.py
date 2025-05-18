import openai
import re

openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"

import time

def get_visualization_code(prompt, retries=3):
    for attempt in range(retries):
        try:
            response = openai.ChatCompletion.create(
                model="deepseek/deepseek-v3-base:free",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that writes pandas/seaborn/matplotlib Python code for data visualization. The DataFrame is already loaded and named df. Return only valid Python code, nothing else."},
                    {"role": "user", "content": prompt},
                ]
            )

            raw_code = response['choices'][0]['message']['content']

            # Clean the raw code
            lines = raw_code.splitlines()
            cleaned_lines = [line for line in lines if not line.strip().lower().startswith("click to see")]
            cleaned_code = "\n".join(cleaned_lines)

            if "```" in cleaned_code:
                cleaned_code = cleaned_code.split("```python")[-1].split("```")[0]

            return cleaned_code.strip()

        except Exception as e:
            if attempt < retries - 1:
                print(f"⚠️ Attempt {attempt+1} failed. Retrying...")
                time.sleep(2)
            else:
                raise e



