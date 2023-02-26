import streamlit as st
import pandas as pd 
import streamlit.components.v1 as stc
from db_data_uploaded_dataset import * 
from PIL import Image
from st_btn_select import st_btn_select

def laman_optimasi_dengan_dataset():
    st.subheader("Semua Data Depot (Kantor)")
    result = view_all_data_uploaded_dataset()
    # st.write(result)
    clean_df = pd.DataFrame(result,columns=["id","name","data"])
    st.dataframe(clean_df)
    datafile = st.file_uploader("Upload Dokumen", type=['csv','xlsx','xls'])
    if datafile is not None:
        file_details = {"File Name":datafile.name,"File Type":datafile.type}
        df = pd.read_excel(datafile)
        st.dataframe(df)
        # Get the file name
        file_name = datafile.name
        
        # Read the file data as bytes
        file_data = datafile.read()
        option = st_btn_select(('#','Tambah Dataset', 'Hapus Dataset'),index=0)
        if option == 'Tambah Dataset':
            save_data_uploaded_dataset(file_name, file_data)

    