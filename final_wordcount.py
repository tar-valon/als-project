import re
import fitz


def count_txt_words():
    # Open the text file for reading
    with open('ALS_Report.txt', 'r') as f:

        # Read the whole text file
        text = f.read()

        # Convert all words to lowercase
        text = text.lower()

        # Remove figure captions from text using regular expressions
        text = re.sub(r"f i g u r e \d{1,}[\s\S]*?(?=\n{2,})\n", '', text)

        # Remove punctuation using regular expressions
        text = re.sub(r"[^\w\s]", '', text)

        # Split the text
        text = text.split()

        end_index = text.index('references')

        # Get the text within the specified range
        text_within_range = text[:end_index]

        word_count = len(text_within_range)

        print("Word Count:", word_count)


def count_pdf_words():
    # Open the pdf file for reading
    pdf = fitz.open("ALS_Report.pdf")
    text = ""

    # Extract text from pdf pages
    for page in pdf:
        text += page.get_text()

    # Convert all words to lowercase
    text = text.lower()

    # Remove figure captions from text using regular expressions
    # only removes the first line of figure caption
    text = re.sub(r"f i g u r e \d{1,}\n{1,}.+", '', text)

    # Remove punctuation using regular expressions
    text = re.sub(r"[^\w\s]", '', text)

    # Split the text
    text = text.split()

    end_index = text.index('references')

    # Get the text within the specified range
    text_within_range = text[:end_index]

    word_count = len(text_within_range)

    print("Word Count:", word_count)


if __name__ == "__main__":
    file = input("Select a file option:\nEnter 1 for Pdf\nEnter 2 for txt\n")
    if file == '1':
        count_pdf_words()
    elif file == '2':
        count_txt_words()
    else:
        print("Invalid option")
