from recommendation import RecommendationEngine

engine = RecommendationEngine(
    "data/courses.csv"
)

user_input = input(
    "Enter your interests: "
)

results = engine.recommend(user_input)

print("\nRecommended Courses:\n")

for index, row in results.iterrows():

    print(
        f"{row['title']} "
        f"({row['score']:.2f})"
    )