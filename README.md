# Predictive-Maintenance

## Goal of this Project
The Goal of this project is to create a ML model. This model is then used to classify whether machines can be used in that way or if it would lead to damage.
Companies can take advantage of this and reduce the wear they have on their machines.

## How it works

### DataAnalysis
This Notebook is used to inspect, clean and analyse our Dataset. This will be achieved by 3 steps:
- Loading and inspecting the dataset.
- Identifying and dealing with inconsistent or missing data
- Using visualizations to understand the data further

### DataModells
After the data has been cleaned we can move on to out ML models. We proceeded in these steps:
- Preprocessing the data
- Implementing and compairing classification algorithms
- Addressing class imbalances
- Performing hyperparameter tuning
- Evaluating model performance
- Saving best performing model

### Web Application

In this last step we deploy our best performing model into our web application. This includes:
- loading the saved model onto the website
- creating a UI that allows user input
- Using the model to ensure its functions

### Use-Case

Outside of our technical work we put a heavy focus on our use case to make sure our product bring value. 

## Installation / Packages

The requirements to run the files are the installation of the following packages:

- NumPy: pip install numpy
- Pandas: pip install pandas
- Matplotlib: pip install matplotlib
- Scikit-learn: pip install scikit-learn
- Imbalanced-learn: pip install imbalanced-learn
- Seaborn: pip install seaborn

Command: pip install pandas numpy seaborn matplotlib scikit-learn 

And a Streamlit installation for the Web App: https://docs.streamlit.io/get-started/installation 

## How to start the code
The Dataset can be found in the "Data" folder where the path has to be swapped to your own in the Jupyter Notebooks.The same has to be done with the path in the Web-App.
To start the Webapp type the following into your comand line: streamlit run "Prediction_Web_App.py"

Members of the Group: Finn Münstermann(3071508), Jan Waldmann (7952189), Lars Lönnen (1412338)
