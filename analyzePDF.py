import PyPDF2
import openai
import re
from transformers import pipeline
import textwrap

# Set up your OpenAI API credentials
openai.api_key = "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"

keywords = ['prerequisite', 'antirequisite', 'book', 'assignment', 'test', 'quiz', 'lab','exam','important']


def analyze_pdf(filename):
    # Open the PDF file in read binary mode
    with open(filename, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        # Extract text from each page and combine into a single string
        pdf_text = ""
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            pdf_text += page.extract_text()

        # Convert the text to lower case for case-insensitive search
        pdf_text = pdf_text.lower()

        # Look for keywords in the text
        keyword_contexts = []
        for keyword in keywords:
            # Convert the keyword to lower case for case-insensitive search
            keyword = keyword.lower()

            start_index = 0
            while start_index < len(pdf_text):
                start_index = pdf_text.find(keyword, start_index)
                if start_index == -1:
                    break
                start_context = max(0, start_index - 100)
                end_context = min(len(pdf_text), start_index + len(keyword) + 100)
                context = pdf_text[start_context:end_context]

                # Merge with previous context if they overlap or are adjacent
                if keyword_contexts and start_context - 100 <= keyword_contexts[-1][1]:
                    keyword_contexts[-1][1] = end_context
                else:
                    keyword_contexts.append([start_context, end_context])

                start_index += len(keyword)  # Move past the current keyword occurrence

        # Print the number of characters in the PDF and the contexts
        print(f"The number of characters in the PDF: {len(pdf_text)}")
        for context in keyword_contexts:
            context_text = pdf_text[context[0]:context[1]]
            print(f"Context: {context_text}")
            print(f"The number of characters in this context: {len(context_text)}")

        prompt = f"PDF Text: {relevant_text}\n\nFind the answers to the following questions and answer in the provided format:\n{questions}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response.choices[0].message.content.strip()

        # Print the generated answer
        print(answer)
