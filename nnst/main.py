import streamlit as st
import pandas as pd

data=pd.read_excel("data.xlsx",sheet_name="HL LAP")

df = pd.DataFrame(data)
df6 = df.copy()

options_Name = df6['NAME'].unique().tolist()
selected_Name = st.sidebar.multiselect('Search By Name',options_Name)

options_phone = df6['Phone Number'].unique().tolist()
selected_phone = st.sidebar.multiselect('Search By Phone Number',options_phone)

options_district = df6['District'].unique().tolist()
selected_district = st.sidebar.multiselect('Search By District',options_district)

options_location = df6['Location'].unique().tolist()
selected_location = st.sidebar.multiselect('Search By Location',options_location)

if selected_Name:
    df6 = df6[df6["NAME"].isin(selected_Name)]
    st.markdown(
               f'<p class="header_title"> {str(df6.shape[0])} </p>',
               unsafe_allow_html=True,
               )

elif selected_phone:
    df6 = df6[df6["Phone Number"].isin(selected_phone)]
    st.markdown(
               f'<p class="header_title"> {str(df6.shape[0])} </p>',
               unsafe_allow_html=True,
               )

elif selected_district:
    df6 = df6[df6["District"].isin(selected_district)]
    st.markdown(
               f'<p class="header_title"> {str(df6.shape[0])} </p>',
               unsafe_allow_html=True,
               )
    
elif selected_location:
    df6 = df6[df6["Location"].isin(selected_location)]
    st.markdown(
               f'<p class="header_title"> {str(df6.shape[0])} </p>',
               unsafe_allow_html=True,
               )

else:
    st.markdown(
               f'<p class="header_title"> {str(df6.shape[0])} </p>',
               unsafe_allow_html=True,
               )
# st.dataframe(df6.reset_index(drop = True).style.apply(highlight_rows, axis=1))

if selected_Name or selected_phone or selected_district or selected_location:
    st.dataframe(df6.reset_index(drop = True))
else:
    st.dataframe(df)
