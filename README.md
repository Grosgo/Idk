# MOVIES DATASET

## Description
This dataset contains information about movies, including details such as title, year, genre, rating, one-line description, number of votes, runtime, gross revenue, directors, and actors.

## Dataset Source
The dataset was downloaded from Kaggle: [Movies Dataset](https://www.kaggle.com/datasets/bharatnatrayn/movies-dataset-for-feature-extracion-prediction?select=movies.csv)

- Number of rows: 9999
- Number of columns: 9

## Cleaning Process
- Started with the 'YEAR' column, removed all non-digit characters, and added a " - " if there are more than 4 characters, indicating a range of years.
- Split the 'DIRECTORS' column into separate 'Directors' and 'Actors' columns, as they were mixed.
- Removed extra characters and null (NaN, None) cells.

## New Columns
- 'Directors': Contains the names of the directors.
- 'Actors': Contains the names of the actors.

## Usage
- The cleaned dataset is available in CSV format in this repository.
- Users may use the dataset for practice or exploration. No specific preprocessing steps are required.

## Contact Information
For questions or feedback about the dataset, please contact amdgaham@gmail.com.
