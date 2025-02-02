# Movie Recommendation System

## Overview
This project is a movie recommendation system developed using Python. It utilizes text preprocessing techniques to generate vectors for movie recommendations, calculates cosine distances between these vectors, and recommends the top five movies based on user input.

The system fetches movie data from TMDB datasets (`tmdb_5000_credits.csv` and `tmdb_5000_movies.csv`) and provides an interactive user interface using Streamlit.

## Directory Structure

project_directory/
│
├── data/
│ ├── tmdb_5000_credits.csv
│ └── tmdb_5000_movies.csv
│
├── venv/
├── .gitattributes
├── .gitignore
├── app.py
├── movies_with_id.pkl
├── notebook.ipynb
├── requirements.txt
└── vectors.pkl

## Installation

### Prerequisites
- Python 3.10 or higher
- Git Bash (for command-line interface)
- Virtual environment (venv) with required dependencies

### Installation Steps
1. Clone the repository:

   git clone https://github.com/sagarkasotiya/Movie_Recommendation_Project
   cd <repository-directory>

2. Create and activate the virtual environment:
   python -m venv venv
   source venv/bin/activate  # For Linux/MacOS
   venv\Scripts\activate  # For Window

3. Install the required dependencies:
   pip install -r requirements.txt

## Usage
1.Ensure the virtual environment is activated.

2.Run the Streamlit application:
  streamlit run app.py

3.Open your web browser and navigate to http://localhost:8501 to interact with the application.

## Notebooks
- \`notebook.ipynb\`: Notebook containing exploratory data analysis and model training.

## Files and Descriptions

- \`tmdb_5000_credits.csv\` and \`tmdb_5000_movies.csv\`: Dataset files containing movie credits and details from TMDB.
- \`app.py\`: Main script to run the Streamlit web application.
- \`movies_with_id.pkl\` and \`vectors.pkl\`: Pickle files containing processed movie data and generated vectors.
- \`.gitattributes\` and \`.gitignore\`: Git configuration files.
- \`requirements.txt\`: List of dependencies required for the project.

## Contributing
Contributions are welcome! Please create a pull request or open an issue to discuss any changes.

## Acknowledgements
- TMDB for providing the dataset.


echo "README.md file created successfully."
