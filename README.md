🎯 AI Learning Path Recommendation System

A Content-Based Recommendation System that recommends the most relevant learning resources based on user interests and skills using TF-IDF Vectorization and Cosine Similarity.

The project demonstrates the core concepts behind modern recommendation systems used by platforms such as Netflix, Amazon, Coursera, and Spotify.

🚀 Features
Personalized course recommendations
Content-Based Filtering
TF-IDF feature extraction
Cosine Similarity matching
Top-N recommendation generation
Fast and lightweight implementation
Easily extendable to books, jobs, research papers, and scholarships
📌 Problem Statement

With thousands of online learning resources available, finding relevant content can be challenging.

This project solves that problem by:

Understanding user interests.
Converting text into numerical vectors.
Measuring similarity between user preferences and course descriptions.
Ranking and recommending the most relevant courses.
🏗️ Project Architecture
User Interests
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Cosine Similarity
      │
      ▼
Ranking Engine
      │
      ▼
Top Recommendations
📂 Project Structure

AI-Recommendation-System/
├── data/
│   └── courses.csv
├── recommendation.py
├── app.py
├── README.md

🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-Learn
TF-IDF Vectorizer
Cosine Similarity
⚙️ Installation

Clone the repository:

git clone : https://github.com/Priyalparmar03/Task3_Priyal-Parmar-AI-Recommendation-System

Move to the project directory:

cd AI-Learning-Path-Recommender

Create a virtual environment:

python -m venv venv

Activate the environment:

Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
📊 Dataset

The dataset contains:

Column	Description
course_id	Unique course identifier
title	Course name
skills	Skills covered in the course

Example:

course_id,title,skills
1,Python for Beginners,"python programming"
2,Machine Learning Fundamentals,"python machine learning"
3,Deep Learning Masterclass,"deep learning neural networks"
▶️ Usage

Run the application:

python app.py

Enter your interests:

python machine learning deep learning

Example output:

Top Recommendations

1. Machine Learning Fundamentals
2. Deep Learning Masterclass
3. NLP with Python
4. Computer Vision
5. Data Science Bootcamp
🧠 How It Works
1. Text Vectorization

Course skills and user interests are converted into numerical vectors using TF-IDF.

2. Similarity Calculation

Cosine Similarity measures how closely user interests align with course features.

3. Recommendation Ranking

Courses are ranked based on similarity scores.

4. Top-N Selection

The highest-scoring courses are returned as recommendations.

📈 Example Workflow
User Input:
Python, Machine Learning

        │
        ▼

TF-IDF Vectorization

        │
        ▼

Cosine Similarity

        │
        ▼

Recommendations:

1. Machine Learning Fundamentals
2. Data Science Bootcamp
3. NLP with Python
🎯 Learning Outcomes

This project demonstrates:

Recommendation Systems
Natural Language Processing
Information Retrieval
Feature Engineering
TF-IDF Vectorization
Cosine Similarity
Machine Learning Fundamentals
Python Development
🔮 Future Improvements
Streamlit Web Application
User Authentication
Recommendation History
Course Rating System
Hybrid Recommendation Engine
BERT-Based Recommendations
FAISS Vector Search
Research Paper Recommendations
Scholarship Recommendations
Job Recommendation Engine
🌟 Applications

This recommendation engine can be adapted for:

E-Learning Platforms
Research Paper Recommendations
Job Portals
Scholarship Discovery Platforms
Book Recommendation Systems
Product Recommendation Systems
Personalized Content Platforms

Authour 

Priyal Parmar 
