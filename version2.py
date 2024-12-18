from PyPDF2 import PdfReader
from transformers import pipeline, GPT2LMHeadModel, GPT2Tokenizer

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


# Function to summarize the extracted text
def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    # Set the maximum chunk size for the model
    max_chunk_size = 1024  # Max input length for Bart
    chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]

    summaries = []
    for chunk in chunks:
        # Summarize each chunk with proper max_length
        summary = summarizer(chunk, max_length=200, min_length=50, do_sample=False)
        summaries.append(summary[0]['summary_text'])

    # Combine all summaries
    return " ".join(summaries)


# Function to generate questions from text using Hugging Face's GPT-2 or GPT-Neo model
def generate_questions(text, num_questions=5):
    model_name = "gpt2"  # You can change to "EleutherAI/gpt-neo-2.7B" for a larger model
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Encode input text to generate prompts
    input_text = f"Please generate {num_questions} questions based on the following content:\n\n{text}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate the questions
    # Generate the questions
    output = model.generate(
        input_ids,
        max_new_tokens=150,  # Generate up to 150 tokens for the output
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        pad_token_id=tokenizer.eos_token_id,  # Ensure proper padding
    )

    # Decode the generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # Extract the questions from the generated text
    questions = generated_text.split("\n")[1:num_questions + 1]  # Assuming questions are line-by-line
    return "\n".join(questions)


# Function to answer a user-provided question based on the summarized text
def answer_question(context, question):
    qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    answer = qa_pipeline(question=question, context=context)
    return answer['answer']


# Main function to process the PDF, summarize, generate questions, and answer a specific question
def process_pdf_and_handle_questions(pdf_path, num_questions=5):
    # Step 1: Extract text from the PDF
    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)

    # Step 2: Summarize the extracted text
    print("Summarizing text...")
    summary = summarize_text(text)

    # Step 3: Generate questions based on the summary
    print("Generating questions...")
    questions = generate_questions(summary, num_questions=num_questions)

    return summary, questions


# Example usage
if __name__ == "__main__":
    pdf_path = r"example.pdf"  # Replace with the path to your PDF file
    num_questions = 5

    # Process the PDF and generate questions
    summary, questions = process_pdf_and_handle_questions(pdf_path, num_questions)

    print("\n--- Summary ---\n")
    print(summary)

    print("\n--- Generated Questions ---\n")
    print(questions)

    # Input a question and get an answer
    print("\n--- Ask a Question ---")
    user_question = input("Enter your question: ")
    answer = answer_question(summary, user_question)

    print("\n--- Answer ---\n")
    print(answer)
