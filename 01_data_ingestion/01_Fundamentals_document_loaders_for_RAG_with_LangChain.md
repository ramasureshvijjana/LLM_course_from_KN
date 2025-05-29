# Document Loaders for RAG Applications with LangChain

LangChain provides a variety of document loaders to ingest data from different sources. Here are some of the most commonly used loaders, along with code examples:

---

## 1. Text File Loader (`TextLoader`)

**Purpose:** Load plain text files (`.txt`).

```python
from langchain.document_loaders import TextLoader

loader = TextLoader("path/to/your/file.txt")
documents = loader.load()
```

---

## 2. PDF Loader (`PyPDFLoader`)

**Purpose:** Load PDF documents.

```python
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("path/to/your/file.pdf")
documents = loader.load()
```

---

## 3. CSV Loader (`CSVLoader`)

**Purpose:** Load CSV files as documents.

```python
from langchain.document_loaders import CSVLoader

loader = CSVLoader("path/to/your/file.csv")
documents = loader.load()
```

---

## 4. Web Page Loader (`WebBaseLoader`)

**Purpose:** Load web pages via URL.

```python
from langchain.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://example.com")
documents = loader.load()
```

---

## 5. Wikipedia Loader (`WikipediaLoader`)

**Purpose:** Load content from Wikipedia.

```python
from langchain.document_loaders import WikipediaLoader

loader = WikipediaLoader(query="LangChain", lang="en")
documents = loader.load()
```

---

## 6. Docx Loader (`UnstructuredWordDocumentLoader`)

**Purpose:** Load Microsoft Word `.docx` files.

```python
from langchain.document_loaders import UnstructuredWordDocumentLoader

loader = UnstructuredWordDocumentLoader("path/to/your/file.docx")
documents = loader.load()
```

---

## 7. Notion Loader (`NotionDBLoader`)

**Purpose:** Load data from Notion databases.

```python
from langchain.document_loaders import NotionDBLoader

notion_token = "your_integration_token"
database_id = "your_database_id"
loader = NotionDBLoader(integration_token=notion_token, database_id=database_id)
documents = loader.load()
```

---

## 8. Google Drive Loader (`GoogleDriveLoader`)

**Purpose:** Load documents from Google Drive.

```python
from langchain.document_loaders import GoogleDriveLoader

loader = GoogleDriveLoader(document_ids=["your_doc_id_1", "your_doc_id_2"])
documents = loader.load()
```

---

## 9. Email Loader (`UnstructuredEmailLoader`)

**Purpose:** Load emails from `.eml` or `.msg` files.

```python
from langchain.document_loaders import UnstructuredEmailLoader

loader = UnstructuredEmailLoader("path/to/your/email.eml")
documents = loader.load()
```

---

## 10. Directory Loader (`DirectoryLoader`)

**Purpose:** Load all documents from a directory (with optional file type filters).

```python
from langchain.document_loaders import DirectoryLoader

loader = DirectoryLoader("path/to/your/directory", glob="**/*.txt")
documents = loader.load()
```

---

## 11. Unstructured Loader for Many Formats

**Purpose:** Use [Unstructured](https://unstructured-io.github.io/unstructured/) to load PDFs, images, HTML, and more.

```python
from langchain.document_loaders import UnstructuredFileLoader

loader = UnstructuredFileLoader("path/to/your/file.pdf")  # or .html, .jpg, etc.
documents = loader.load()
```

---

## 12. Custom Loader

You can also create your own loader by subclassing `BaseLoader`.

```python
from langchain.document_loaders.base import BaseLoader
from langchain.schema import Document

class MyCustomLoader(BaseLoader):
    def load(self):
        # Your custom loading logic here
        return [Document(page_content="Hello from my loader", metadata={"source": "custom"})]

loader = MyCustomLoader()
documents = loader.load()
```

---

# Notes

- After loading documents, you’ll typically split them into chunks (using `RecursiveCharacterTextSplitter`, etc.) before embeddings and retrieval.
- Each loader returns a list of `Document` objects, which can then be passed to text splitters, embedding models, and retrievers in your RAG pipeline.
- For more up-to-date options or new loaders, see the [LangChain documentation on document loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/).

---

**Example: Loading a PDF and preparing for RAG**

```python
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)
```

---

Feel free to ask for code samples for a specific data format or integration!