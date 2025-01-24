import streamlit as st

st.markdown('# Welcome to Taxifare predictor Website 🚖')

st.markdown('''
Enter your ride details to get the fare prediction 🔮
''')


#Here we would like to add some controllers in order to ask the user to select the parameters of the ride
#
#1. Let's ask for:
#- date and time
#- pickup longitude
#- pickup latitude
#- dropoff longitude
#- dropoff latitude
#- passenger count

#date and time

from datetime import datetime

d = st.date_input(
    "When do you want to take your ride?",
    datetime.today().strftime('%Y-%m-%d'))
st.write('Pickup Date:', d)


t = st.time_input('What time ?', datetime.today().strftime('%H:%M:%S'))

st.write('Pickup Time', t)

#- pickup longitude

pickup_longitude = st.number_input('Insert a pickup longitude')

st.write('pickup longitude ', pickup_longitude)

# pickup latitude

pickup_latitude = st.number_input('Insert a pickup latitude')

st.write('pickup latitude ', pickup_latitude)

#- dropoff longitude

dropoff_longitude = st.number_input('Insert a dropoff longitude')

st.write('dropoff longitude ', dropoff_longitude)

# dropoff latitude

dropoff_latitude = st.number_input('Insert a dropoff latitude')

st.write('dropoff latitude ', dropoff_latitude)

#- passenger count

passenger_count = st.slider('How many passaeger?', 1, 8)

st.write('passengers:',passenger_count)

#'''
### Once we have these, let's call our API in order to retrieve a prediction
#
#See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...
#
#🤔 How could we call our API ? Off course... The `requests` package 💡
#'''

if st.button('Forecast my fare 💰!'):
    # print is visible in the server output, not in the page
    st.write('Here you go! 👇')

    import requests

    url = 'https://apitaxifare-39170945173.europe-west1.run.app/predict'

    params = {
        "pickup_datetime": f"{d} {t}",
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    # Make the GET request
    response = requests.get(url, params=params)

    # Check the response status
    if response.status_code == 200:
        # Parse JSON response
        st.write(f"Tadaaa! Your fare should be around : {round(response.json()['fare'],2)} $ 🎉")
    else:
        st.write(f"Error: {response.status_code}, {response.text}")


#'''
#2. Let's build a dictionary containing the parameters for our API...
#
#3. Let's call our API using the `requests` package...
#
#4. Let's retrieve the prediction from the **JSON** returned by the API...
#
### Finally, we can display the prediction to the user
#'''
