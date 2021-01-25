from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd


class Recommender:
    def __init__(self):
        self.df = None
        self.model = None
        self.summary_tokenised = None
        self.documents = None
        self.vecs = None
        self.cosine_similarity_matrix = None

    def get_recommendations(self, title: str, results: int):
        # Get the index of the books that matches the title
        indices = pd.Series(self.df.index, index=self.df['Title']).drop_duplicates()
        idx = indices[title]
        if type(idx) != np.int64:
            idx = idx[0]

        # Get the pairwsie similarity scores of all books with that book
        sim_scores = list(enumerate(self.cosine_similarity_matrix[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 10 most similar books
        sim_scores = sim_scores[1:results+1]

        # Get the books indices
        book_indices = [i[0] for i in sim_scores]

        # Return the top 10 most similar books
        return self.df['Title'].iloc[book_indices]

    def _cosine_similarity_matrix(self):
        cosine_sim = cosine_similarity(self.vecs, self.vecs)
        return cosine_sim

    def load_df(self, path):
        self.df = pd.read_csv(path)

    def similarity_matrix(self):
        pass

    def _create_vecs(self):
        pass

    def load_model(self, path):
        pass

    def save_model(self, filename):
        pass
