import streamlit as st

st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place:", key="place")
slider = st.slider(label="Forecast Days", min_value=1, max_value=5, key="forecast", help="select the number of "
                                                                                         "forecasted days")
select_box = st.selectbox(label="Select Data to view", options=["Temperature", "Sky"], key="view_data")
st.subheader(f"{select_box} for the next {slider} Days in {place}")

