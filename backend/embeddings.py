from sentence_transformers import SentenceTransformer
from typing import List
import torch


class EmbeddingModel:
    """
    Handles text embeddings for the RAG system.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):

        device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model = SentenceTransformer(model_name, device=device)

    def create_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of texts.
        """

        embeddings = self.model.encode(
            texts,
            batch_size=32,
            show_progress_bar=False,
            convert_to_numpy=True
        )

        return embeddings.tolist()


# global instance
embedding_model = EmbeddingModel()


def create_embeddings(texts: List[str]) -> List[List[float]]:

    return embedding_model.create_embeddings(texts)