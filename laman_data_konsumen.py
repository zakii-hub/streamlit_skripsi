import streamlit as st
import pandas as pd 
from db_data_konsumen import * 
import streamlit.components.v1 as stc
from PIL import Image
from st_btn_select import st_btn_select

# Data Viz Pkgs
import plotly.express as px 

def laman_data_konsumen():
    st.subheader("Semua Data konsumen")
    result = view_all_data_konsumen()
    # st.write(result)
    clean_df = pd.DataFrame(result,columns=["id_konsumen","nama_konsumen","status_konsumen","longitude_konsumen","latitude_konsumen","alamat_konsumen"])
    st.dataframe(clean_df)

    # st.subheader("Task Status")
    # task_df = clean_df['Status'].value_counts().to_frame()
    # # st.dataframe(task_df)
    # task_df = task_df.reset_index()
    # st.dataframe(task_df)

    # p1 = px.pie(task_df,names='index',values='Status')
    # st.plotly_chart(p1,use_container_width=True)
    
    option = st_btn_select(('#','Tambah Data', 'Ubah Data', 'Hapus Data'),index=0)
    button1 = st.button('Refresh Data')
    if button1=='Refresh Data':
        st.experimental_rerun()
        

    if option=='Tambah Data':
        st.subheader("Tambah Data konsumen")
        col1,col2 = st.columns(2)
        
        with col1:
            id_konsumen = st.text_input("Id konsumen")
            nama_konsumen = st.text_input("Nama konsumen")
            status_konsumen = st.selectbox("Status",["Active","In-Active"])

        with col2:
            longitude_konsumen = st.number_input("Longitude konsumen",step=1e-15,format="%.15f")
            latitude_konsumen = st.number_input("Latitude konsumen",step=1e-15,format="%.15f")
        
        alamat_konsumen = st.text_area("Alamat konsumen")

        if st.button("Tambah Data"):
            add_data_konsumen(id_konsumen,nama_konsumen,status_konsumen,longitude_konsumen,latitude_konsumen,alamat_konsumen)
            st.success("Berhasil menambahkan ::{} ::ke data konsumen".format(nama_konsumen))

    if option=='Ubah Data':
        st.subheader("Ubah Data konsumen")
        list_of_nama_konsumen = [i[0] for i in view_all_nama_konsumen()]
        selected_nama_konsumen = st.selectbox("Pilih Nama konsumen",list_of_nama_konsumen)
        nama_konsumen_result = get_nama_konsumen(selected_nama_konsumen)
        # st.write(task_result)

        if nama_konsumen_result:
            id_konsumen = nama_konsumen_result [0][0]
            nama_konsumen = nama_konsumen_result[0][1]
            status_konsumen = nama_konsumen_result[0][2]
            longitude_konsumen = nama_konsumen_result[0][3]
            latitude_konsumen = nama_konsumen_result[0][4]
            alamat_konsumen = nama_konsumen_result[0][5]

            col1,col2 = st.columns(2)
                
            with col1:
                new_id_konsumen = st.text_input("Id konsumen",id_konsumen)
                new_nama_konsumen = st.text_input("Nama konsumen",nama_konsumen)
                new_status_konsumen = st.selectbox(status_konsumen,["Active","In-Active"])
            with col2:
                new_longitude_konsumen = st.number_input("Longitude konsumen",longitude_konsumen,step=1e-15,format="%.15f")
                new_latitude_konsumen = st.number_input("Latitude konsumen",latitude_konsumen,step=1e-15,format="%.15f")
            new_alamat_konsumen = st.text_area("Alamat konsumen",alamat_konsumen)
            if st.button("Update Task"):
                edit_data_konsumen(new_id_konsumen,new_nama_konsumen,new_status_konsumen,new_longitude_konsumen,new_latitude_konsumen,new_alamat_konsumen,id_konsumen,nama_konsumen,status_konsumen,longitude_konsumen,latitude_konsumen,alamat_konsumen)
                st.success("Updated ::{} ::To {}".format(nama_konsumen,new_nama_konsumen))

    if option=='Hapus Data':
        st.subheader("Hapus Data konsumen")
        unique_list = [i[0] for i in view_all_nama_konsumen()]
        delete_by_nama_konsumen =  st.selectbox("Pilih Nama konsumen",unique_list)
        if st.button("Delete"):
            delete_data(delete_by_nama_konsumen)
            st.warning("Berhasil menghapus: '{}'".format(delete_by_nama_konsumen))
    
