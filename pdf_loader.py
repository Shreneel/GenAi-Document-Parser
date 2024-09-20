import fitz # PyMuPDF
import pandas as pd
import os
import re
from langchain.schema import Document as LangChainDocument

class Custom_Loader:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.documents = []
        self.status_df = pd.DataFrame(columns=['Filename', 'Status'])
        self.file_list = self.get_pdf_files(directory_path)

    def get_pdf_files(self, directory_path):
        pdf_files = []
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.pdf'):
                    pdf_files.append(os.path.join(root, file))
        pdf_in_server = pd.DataFrame(pdf_files)
        pdf_in_server.columns = ['FileName']
        pdf_in_server.to_csv("pdf_in_server.csv")
        return pdf_files

    def load(self):
        for i, file in enumerate(self.file_list, start=1):
            print(f"Status = {i} of {len(self.file_list)}")
            try:
                doc = fitz.open(file)
                page_content = ""
                for page in doc:
                    page_content += page.get_text(sort=True) + "\n"
                page_content = re.sub(r'\n\s*\n', '\n', page_content)
                metadata = {
                    "source": os.path.basename(file),
                    "total_pages": len(doc),
                    **{k: doc.metadata[k] for k in doc.metadata if type(doc.metadata[k]) in [str, int]}
                }
                # Using langchain.schema.Document for storing the extracted text and metadata
                langchain_doc = LangChainDocument(page_content=page_content, metadata=metadata)
                self.documents.append(langchain_doc)
                # Using pd.concat to append a row to the status_df DataFrame
                new_row = pd.DataFrame({'Filename': [os.path.basename(file)], 'Status': ['Success']})
                self.status_df = pd.concat([self.status_df, new_row], ignore_index=True)
            except Exception as e:
                print(f"Error processing file {file}: {e}")
                # Using pd.concat to append a row to the status_df DataFrame
                new_row = pd.DataFrame({'Filename': [os.path.basename(file)], 'Status': ['Failure']})
                self.status_df = pd.concat([self.status_df, new_row], ignore_index=True)
        self.status_df.to_csv("file_text_extraction_log.csv")
        return self.documents, self.status_df

# Example usage
# if __name__ == "__main__":
    # directory_path = 'path/to/your/directory' # Replace with your actual directory path
    # loader = Custom_Loader(directory_path)
    # documents, status_df = loader.load()
    # print(status_df)
