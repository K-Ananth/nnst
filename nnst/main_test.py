import streamlit as st
import pandas as pd


data = {
    'User': ['Cibe', 'u2', 'u3'],
    'company': ['c1', 'c2', 'c3']
}

df = pd.DataFrame(data)
df6 = df.copy()

options_Users = df6['User'].unique().tolist()
selected_Users = st.sidebar.multiselect('Search By User',options_Users)

options_company = df6['company'].unique().tolist()
selected_company = st.sidebar.multiselect('Search By company',options_company)


if selected_Users:
    df6 = df6[df6["User"].isin(selected_Users)]
    st.markdown(
               f'<p class="header_title"> {str(df6.shape[0])} </p>',
               unsafe_allow_html=True,
               )

elif selected_company:
    df6 = df6[df6["company"].isin(selected_company)]
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

if selected_Users or selected_company:
    st.dataframe(df6.reset_index(drop = True))
else:
    st.dataframe(df)
