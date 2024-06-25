import PyPDF2
import cohere
import re
import tkinter as tk

# Initialize Cohere client
co = cohere.Client('your-cohere-api-key')

keywords = ['prerequisite', 'antirequisite', 'book', 'assignment', 'test', 'quiz', 'lab', 'exam', 'important']

def analyze_pdf(filename):
    # Open the PDF file in read binary mode
    with open(filename, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        pdf_text = ""
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            pdf_text += page.extract_text()

        pdf_text = pdf_text.lower()

        keyword_contexts = []
        for keyword in keywords:
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

        # Using Cohere's chat to analyze context
        response = co.chat(
            model="large",
            messages=[
                {"role": "user", "text": f"Summarize this content: {context_text}"}
            ]
        )
        answer = response.generations[0].text.strip()

        window = tk.Tk()
        window.title("Course Compass")
        window.geometry("800x800")
        window.configure(bg="#f0f0f0")

        answer_label = tk.Label(window, text=answer, wraplength=400, justify="center", bg="#f0f0f0", fg="#333333", font=("Arial", 12))
        answer_label.pack(padx=20, pady=20)

        def close_window():
            window.destroy()

        close_button = tk.Button(window, text="Close", command=close_window, width=10, height=2, bg="#ff5757", fg="white", font=("Arial", 12))
        close_button.pack(pady=10)

        window.mainloop()

# Example usage
analyze_pdf('path_to_your_pdf_file.pdf')
