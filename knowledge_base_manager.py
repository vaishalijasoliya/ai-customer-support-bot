"""
Knowledge Base Manager for storing and retrieving company information
"""
import os
import json
from typing import List, Dict
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from config import OPENAI_API_KEY, KNOWLEDGE_BASE_DIR, VECTOR_STORE_DIR, TEST_MODE

class KnowledgeBaseManager:
    def __init__(self):
        self.test_mode = TEST_MODE
        if not self.test_mode:
            self.embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        else:
            self.embeddings = None
            print("🧪 Knowledge Base in TEST MODE - Using simple text matching instead of embeddings")
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        self.vector_store = None
        self.simple_storage = []  # For test mode - simple text storage
        self._initialize_directories()
        if not self.test_mode:
            self._load_vector_store()
    
    def _initialize_directories(self):
        """Create necessary directories if they don't exist"""
        os.makedirs(KNOWLEDGE_BASE_DIR, exist_ok=True)
        os.makedirs(VECTOR_STORE_DIR, exist_ok=True)
    
    def _load_vector_store(self):
        """Load or create vector store"""
        if os.path.exists(VECTOR_STORE_DIR) and os.listdir(VECTOR_STORE_DIR):
            try:
                self.vector_store = Chroma(
                    persist_directory=VECTOR_STORE_DIR,
                    embedding_function=self.embeddings
                )
                # Test if it works
                _ = self.vector_store.similarity_search("test", k=1)
            except:
                self.vector_store = None
        
        if self.vector_store is None:
            # Create empty vector store with a dummy document
            dummy_doc = Document(page_content="dummy", metadata={})
            self.vector_store = Chroma.from_documents(
                documents=[dummy_doc],
                embedding=self.embeddings,
                persist_directory=VECTOR_STORE_DIR
            )
    
    def add_document(self, content: str, metadata: Dict = None):
        """Add a document to the knowledge base"""
        if self.test_mode:
            # Simple storage for test mode
            self.simple_storage.append({
                "content": content,
                "metadata": metadata or {}
            })
            return
        
        documents = self.text_splitter.create_documents([content])
        
        if metadata:
            for doc in documents:
                doc.metadata.update(metadata)
        
        if self.vector_store is None:
            self.vector_store = Chroma.from_documents(
                documents=documents,
                embedding=self.embeddings,
                persist_directory=VECTOR_STORE_DIR
            )
        else:
            self.vector_store.add_documents(documents)
            # Chroma persists automatically, but we can force it
            try:
                self.vector_store.persist()
            except:
                pass  # Some versions persist automatically
    
    def add_faq(self, question: str, answer: str):
        """Add a FAQ to the knowledge base"""
        content = f"Q: {question}\nA: {answer}"
        self.add_document(content, metadata={"type": "faq"})
    
    def search(self, query: str, k: int = 3) -> List[Document]:
        """Search the knowledge base for relevant information"""
        if self.test_mode:
            # Simple keyword matching for test mode
            query_lower = query.lower()
            results = []
            for item in self.simple_storage:
                if query_lower in item["content"].lower():
                    results.append(Document(
                        page_content=item["content"],
                        metadata=item["metadata"]
                    ))
            return results[:k]
        
        if self.vector_store is None:
            return []
        
        try:
            results = self.vector_store.similarity_search(query, k=k)
            return results
        except:
            return []
    
    def get_context(self, query: str, k: int = 3) -> str:
        """Get formatted context from knowledge base"""
        results = self.search(query, k)
        if not results:
            return ""
        
        context_parts = []
        for doc in results:
            context_parts.append(doc.page_content)
        
        return "\n\n".join(context_parts)
    
    def clear_knowledge_base(self):
        """Clear the entire knowledge base"""
        if os.path.exists(VECTOR_STORE_DIR):
            import shutil
            shutil.rmtree(VECTOR_STORE_DIR)
        self._load_vector_store()

