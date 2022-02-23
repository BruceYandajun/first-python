import time

import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber pickups in NYC!!!")

DATE_COLUMN = 'date/time'
DATA_URL = '/Users/yandajun/Downloads/browser/uber-raw-data-sep14.csv'


@st.cache(ttl=600)
def load_data(nrows):
    data_r = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data_r.rename(lowercase, axis='columns', inplace=True)
    data_r[DATE_COLUMN] = pd.to_datetime(data_r[DATE_COLUMN])
    return data_r


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
start = time.perf_counter()
data = load_data(10000)
end = time.perf_counter()
# print(data)
# Notify the reader that the data was successfully loaded.
data_load_state.text(f'Loaded data...done, cost {end - start} seconds.')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)

st.subheader('Map of all pickups')
st.map(data)

hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)
