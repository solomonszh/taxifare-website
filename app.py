import streamlit as st
import requests
import datetime
'''
# TaxiFareModel front
'''

st.markdown('''
This is my first frontend''')


# with st.form(key='params_for_api'):
pickup_date = st.date_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_time = st.time_input('pickup datetime', value=datetime.datetime(2013, 10, 6, 11, 10, 20))
pickup_datetime = f'{pickup_date} {pickup_time}'
pickup_longitude = st.number_input('pickup longitude', value=40.7614327)
pickup_latitude = st.number_input('pickup latitude', value=40.7614327)
dropoff_longitude = st.number_input('dropoff longitude', value=40.7614327)
dropoff_latitude = st.number_input('dropoff latitude', value=40.7614327)
passenger_count = st.number_input('passenger count', min_value=1, max_value=8, step=1, value=1)

params = dict(
    pickup_datetime=pickup_datetime,
    pickup_longitude=pickup_longitude,
    pickup_latitude=pickup_latitude,
    dropoff_longitude=dropoff_longitude,
    dropoff_latitude=dropoff_latitude,
    passenger_count=passenger_count
)

url = 'https://taxifare-6tmyexoyqq-ew.a.run.app/predict' #https://taxifare.lewagon.ai/predict

response = requests.get(url, params=params)

prediction = response.json()
# print(prediction)
pred = prediction['fare_amount']

st.markdown('''
Returning Results Yehoo!''')
st.header(f'Fare amount: ${round(pred, 2)}')


