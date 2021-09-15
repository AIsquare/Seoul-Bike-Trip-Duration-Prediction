import streamlit as st
from model import predict_duration

st.set_page_config(page_title="Seoul Biker Trip Duration Prediction App",page_icon='@___/-',layout='wide')

with st.form("prediction_form"):

    st.header("Enter the deciding factors:")

    distance = st.number_input("Distance: ",value=0,format="%d")
    haversine = st.number_input("Haversine: ")
    phour = st.slider("Pickup Hour: ",0, 23, value=0, format="%d")
    pmin = st.slider("Pickup Hour: ",0, 59, value=0, format="%d")
    dhour = st.slider("Dropoff Hour: ", 0, 23, value=0, format="%d")
    dmin = st.slider("Dropff Hour: ",0, 59, value=0, format="%d")
    temp = st.number_input("Temp: ")
    humid = st.number_input("Humid: ")
    solar = st.number_input("Solar: ")
    dust = st.number_input("Dust: ")

    submit_val = st.form_submit_button("Prediction duration")

if submit_val:
    #if submit is pressed == True
    attribute = np.array([distance, haversine, phour,
                        pmin, dhour,
                        dmin, temp,
                        humid, solar, dust]).reshape(1,-1)

    if attribute.shape == (1,10):
        print("attributes valid")

        value = predict_duration(attributes=attribute)
        st.header("Here are the results:")
        st.success(f"The Duration predicted is {value} mins")


