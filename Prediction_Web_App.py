
import numpy as np
import pickle
import streamlit as st

# Vorher Streamlit installieren https://docs.streamlit.io/get-started/installation
# loading the saved model
loaded_model = pickle.load(open('C:/Uni/Semester 4/Projekt in Machine Learning/Projekt-Git/Predictive-Maintenance/best_model_1', 'rb'))


# creating a function for Prediction

def machine_failure(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Die Maschine läuft so weiter'
    else:
      return 'Die Maschine geht so Kaputt'
  
    
  
def main():
    
    
    # giving a title
    st.title('Predictive Maintenance Web App')
    
    
    # getting the input data from the user
    
    # Diese Sachen? Type, Rotational speed [rpm],Torque [Nm],Power, Overstrain, Heat Dissipation

    Type = st.text_input('Type (Low = 0, Medium = 1, High = 2)')
    Rotational_Speed = st.text_input('Rotational speed (Rpm)')
    Torque = st.text_input('Torque (Nm)')
    Power = st.text_input('Power Value (Watt)')
    Overstrain = st.text_input('Overstrain (Min/Nm)')
    Heat_Dissipation = st.text_input('Heat Dissipation (Rounds per Minute in Kelvin)')

    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Machine Test Result'):
        diagnosis = machine_failure([Type, Rotational_Speed, Torque, Power,Overstrain, Heat_Dissipation])
          
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
