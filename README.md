# Predictive-Maintenance

## How it works

### DataAnalysis
This Notebook is used to inspect, clean and analyse our Dataset. This will be achieved by 3 steps:
- Loading and inspecting the dataset.
- Identifying and dealing with inconsistent or missing data
- Using visualizations to understand the data further

### DataModells
After anylsing our data we can now move on to develope and evaluate ML models.
This is used to use the chosen modells and find out which one performs the best on our Dataset.
We achieve this by using resampling techniques and hyperparameter tuning.
In the end we extract the best performing modell using pickle which we will be using for the Webapp.

The last step is the Webapp.
We simply load our modell onto our website and use user inputs to give out predictions on whether machines can or cant be used in that way.

## Installation / Packages

The requirements to run the files are the installation of the following packages:

- NumPy: pip install numpy
- Pandas: pip install pandas
- Matplotlib: pip install matplotlib
- Scikit-learn: pip install scikit-learn
- Imbalanced-learn: pip install imbalanced-learn
- Seaborn: pip install seaborn
- Streamlit: pip install streamlit

Command: pip install pandas numpy seaborn matplotlib scikit-learn streamlit

Validate installation:

Command: streamlit hello 

## How to start the code
The Dataset can be found in the "Data" folder where the path has to be swapped to your own in the Jupyter Notebooks.The same has to be done with the path in the Web-App.
To start the Webapp type the following into your comand line: streamlit run "Prediction_Web_App.py"

Members of the Group: Finn Münstermann(3071508), Jan Waldmann (7952189), Lars Lönnen (1412338)
