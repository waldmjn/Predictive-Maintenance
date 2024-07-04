
import numpy as np
import pickle
import streamlit as st


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
    
    
    Air_Temperature = st.text_input('Air temperature (Kelvin)')
    Process_Temperature = st.text_input('Process temperature (Kelvin)')
    Rotational_Speed = st.text_input('Rotational speed (Rpm)')
    Torque = st.text_input('Torque (Nm)')
    Tool_Wear = st.text_input('Tool wear (Minutes)')
    Power_Value = st.text_input('Power Value (Watt)')
    Overstrain = st.text_input('Overstrain (Minutes/Nm)')
    Heat_dissipation = st.text_input('Heat dissipation (rpm in Kelvin)')
    ninth = st.text_input("This is the ninth input")
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Machine Test Result'):
        diagnosis = machine_failure([Air_Temperature, Process_Temperature, Rotational_Speed, Torque, Tool_Wear, Power_Value])
          
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()