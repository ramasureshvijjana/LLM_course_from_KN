# Text Splitters for RAG Applications with LangChain

LangChain provides several text splitters to break documents into manageable chunks for embedding, retrieval, and generation. Here are commonly used splitters, their use-cases, and example Python code:

---

## 1. RecursiveCharacterTextSplitter

**Splits text recursively by characters, sentences, or paragraphs.**  
*Best for: Flexible splitting with control over chunk size and overlap.*

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_text("A long document string...")
# For Document objects:
docs = splitter.split_documents(documents)
```

---

## 2. CharacterTextSplitter

**Splits by a specified character (default is "\n\n").**  
*Best for: Simple, delimiter-based splitting.*

```python
from langchain.text_splitter import CharacterTextSplitter

splitter = CharacterTextSplitter(separator="\n\n", chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_text("A long document string...")
```

---

## 3. TokenTextSplitter

**Splits based on token count, useful for LLM token limits.**  
*Best for: Keeping chunks within LLM token context windows.*

```python
from langchain.text_splitter import TokenTextSplitter

splitter = TokenTextSplitter(chunk_size=256, chunk_overlap=32)
chunks = splitter.split_text("A long document string...")
```

---

## 4. MarkdownTextSplitter

**Splits Markdown documents at headers, blocks, etc.**  
*Best for: Markdown files with structure.*

```python
from langchain.text_splitter import MarkdownTextSplitter

splitter = MarkdownTextSplitter(chunk_size=600, chunk_overlap=50)
chunks = splitter.split_text("# Header\n\nSome content\n\n## Subheader\nMore content")
```

---

## 5. NLTKTextSplitter

**Uses NLTK to split by sentences.**  
*Best for: Sentence-aware splitting for natural language.*

```python
from langchain.text_splitter import NLTKTextSplitter

splitter = NLTKTextSplitter(chunk_size=1000)
chunks = splitter.split_text("A long document string...")
```
> Requires `nltk` and `punkt` tokenizer:  
> `pip install nltk` and `import nltk; nltk.download('punkt')`

---

## 6. SpacyTextSplitter

**Uses spaCy to split by sentences.**  
*Best for: Sentence-aware splitting with advanced NLP capabilities.*

```python
from langchain.text_splitter import SpacyTextSplitter

splitter = SpacyTextSplitter(chunk_size=1000)
chunks = splitter.split_text("A long document string...")
```
> Requires `spacy` and a language model:  
> `pip install spacy` and `python -m spacy download en_core_web_sm`

---

## 7. LatexTextSplitter

**Splits LaTeX documents at sections, equations, etc.**  
*Best for: Scientific documents in LaTeX format.*

```python
from langchain.text_splitter import LatexTextSplitter

splitter = LatexTextSplitter(chunk_size=800, chunk_overlap=100)
chunks = splitter.split_text(r"\section{Intro}\nSome LaTeX text...")
```

---

## 8. HTMLHeaderTextSplitter

**Splits HTML documents at header tags (h1, h2, h3, ...).**  
*Best for: Web page content with HTML structure.*

```python
from langchain.text_splitter import HTMLHeaderTextSplitter

splitter = HTMLHeaderTextSplitter(headers_to_split_on=["h1", "h2", "h3"])
chunks = splitter.split_text("<h1>Title</h1><p>Paragraph</p>")
```

---

## 9. SentenceTransformersTokenTextSplitter

**Uses sentence-transformers tokenization for splitting.**  
*Best for: When using sentence-transformers embeddings.*

```python
from langchain.text_splitter import SentenceTransformersTokenTextSplitter

splitter = SentenceTransformersTokenTextSplitter(chunk_size=128, chunk_overlap=16)
chunks = splitter.split_text("A long document string...")
```

---

## 10. Custom Splitter Example

**You can implement your own by subclassing `TextSplitter`.**

```python
from langchain.text_splitter import TextSplitter

class MyCustomSplitter(TextSplitter):
    def split_text(self, text):
        return text.split("CUSTOM_DELIMITER")

splitter = MyCustomSplitter()
chunks = splitter.split_text("section1CUSTOM_DELIMITERsection2")
```

---

## Example: Splitting Documents For RAG

```python
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = TextLoader("sample.txt")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)
```

---

**Tip:**  
Choose the splitter best suited to your document format and downstream model constraints.  
For more, see: [LangChain Text Splitters Docs](https://python.langchain.com/docs/modules/data_connection/text_splitters/)