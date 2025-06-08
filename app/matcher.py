from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class NameMatcher:
    def __init__(self, names):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.names = names
        self.embeddings = self.model.encode(names, convert_to_numpy=True)

        # Build FAISS index
        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(self.embeddings)

    def get_matches(self, input_name, top_k=5):
        input_vector = self.model.encode([input_name], convert_to_numpy=True)
        distances, indices = self.index.search(input_vector, top_k)
        results = []
        for idx, dist in zip(indices[0], distances[0]):
            score = 1 / (1 + dist)  # Convert distance to similarity score
            results.append((self.names[idx], round(score, 4)))
        return results

    def get_best_match(self, input_name):
        return self.get_matches(input_name, top_k=1)[0]
