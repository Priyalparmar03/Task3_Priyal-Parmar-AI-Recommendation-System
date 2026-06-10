import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class RecommendationEngine:

    def __init__(self, csv_file):

        self.df = pd.read_csv(csv_file)

        self.vectorizer = TfidfVectorizer()

        self.course_vectors = self.vectorizer.fit_transform(
            self.df["skills"]
        )

    def recommend(self, user_interest, top_n=5):

        user_vector = self.vectorizer.transform(
            [user_interest]
        )

        similarity_scores = cosine_similarity(
            user_vector,
            self.course_vectors
        )

        scores = similarity_scores.flatten()

        self.df["score"] = scores

        recommendations = self.df.sort_values(
            by="score",
            ascending=False
        )

        return recommendations[
            ["title", "score"]
        ].head(top_n)