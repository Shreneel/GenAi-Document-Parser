# Custom PDF Loader with PyMuPDF and LangChain

This repository contains a custom PDF loader that extracts text and metadata from PDF files and stores them as structured `LangChainDocument` objects. It processes all PDF files in a specified directory and logs the status of the extraction process.

## Features
- Extracts text from PDF files using the `PyMuPDF` (`fitz`) library.
- Cleans and structures the text.
- Extracts metadata from the PDF, including the total number of pages and available metadata fields (e.g., author, title).
- Uses `LangChainDocument` to store the extracted text and metadata for further use in NLP or document processing pipelines.
- Logs success and failure for each PDF file in a CSV file for easy monitoring.

## Requirements

To run this project, you'll need to install the following dependencies:
pip install pymupdf pandas langchain

## How to Use
Clone the repository:

git clone <repo-url>
cd <repo-directory>
Prepare the Directory:

Place all the PDF files you want to process in a directory.
Run the Loader: Create a Python script or use a Jupyter notebook to instantiate and run the Custom_Loader class:


from custom_pdf_loader import Custom_Loader

Provide the path to the directory containing PDF files
loader = Custom_Loader('/path/to/your/pdf/directory')

Load and process the PDF files
documents, status_df = loader.load()

documents will contain the extracted text and metadata
status_df will contain the log of success/failure for each file

## Output Files:

Extracted Documents: The extracted content is stored in documents, a list of LangChainDocument objects.
Logs: Two CSV files are created:
pdf_in_server.csv: A list of all PDFs found in the directory.
file_text_extraction_log.csv: Logs the status of text extraction for each file (success or failure).

## Customization
You can modify the following aspects based on your use case:

Directory Path: Modify the path in the Custom_Loader initialization to point to your specific directory containing PDFs.
Text Processing: Adjust the regular expression used for text cleaning in the load() method to suit your text processing needs.
Metadata: You can extract more metadata by updating the metadata dictionary in the load() method.

## Example
loader = Custom_Loader('/path/to/pdf/directory')
documents, status_df = loader.load()

## Access the content of the first document
first_doc = documents[0]
print(first_doc.page_content)  # Prints the extracted text from the PDF
print(first_doc.metadata)      # Prints the metadata of the PDF

## Error Handling
The loader gracefully handles errors during PDF processing. If an error occurs while extracting text from a file, the error is printed to the console, and the file's status is marked as 'Failure' in the log.

## Dependencies
PyMuPDF (fitz): For PDF file reading and text extraction.
pandas: For managing logs and saving them as CSV files.
LangChain: For creating structured document objects for downstream NLP tasks.

## License
This project is licensed under the MIT License.
