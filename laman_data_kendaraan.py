import streamlit as st
import pandas as pd 
from db_data_kendaraan import * 
import streamlit.components.v1 as stc
from PIL import Image
from st_btn_select import st_btn_select

# Data Viz Pkgs
import plotly.express as px 

def laman_data_kendaraan():
    st.subheader("Semua Data kendaraan")
    result = view_all_data_kendaraan()
    # st.write(result)
    clean_df = pd.DataFrame(result,columns=["id_tipe_kendaraan","nama_kendaraan","kapasitas_kendaraan","jumlah_kendaraan"])
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
        st.subheader("Tambah Data kendaraan")
        col1,col2 = st.columns(2)
        
        with col1:
            id_tipe_kendaraan = st.text_input("Id tipe kendaraan")
            nama_kendaraan = st.text_input("Nama kendaraan")
            
        with col2:
            kapasitas_kendaraan = st.number_input("Kapasitas Kendaraan",step=1)
            jumlah_kendaraan = st.number_input("Jumlah Kendaraan",step=1)
        
       
        if st.button("Tambah Data"):
            add_data_kendaraan(id_tipe_kendaraan,nama_kendaraan,kapasitas_kendaraan,jumlah_kendaraan)
            st.success("Berhasil menambahkan ::{} ::ke data kendaraan".format(nama_kendaraan))

    if option=='Ubah Data':
        st.subheader("Ubah Data kendaraan")
        list_of_nama_kendaraan = [i[0] for i in view_all_nama_kendaraan()]
        selected_nama_kendaraan = st.selectbox("Pilih Nama kendaraan",list_of_nama_kendaraan)
        nama_kendaraan_result = get_nama_kendaraan(selected_nama_kendaraan)
        # st.write(task_result)

        if nama_kendaraan_result:
            id_tipe_kendaraan = nama_kendaraan_result [0][0]
            nama_kendaraan = nama_kendaraan_result[0][1]
            kapasitas_kendaraan = nama_kendaraan_result[0][2]
            jumlah_kendaraan = nama_kendaraan_result[0][3]

            col1,col2 = st.columns(2)
                
            with col1:
                new_id_tipe_kendaraan = st.text_input("Id Kendaraan",id_tipe_kendaraan)
                new_nama_kendaraan = st.text_input("Nama Kendaraan",nama_kendaraan)
                
            with col2:
                new_kapasitas_kendaraan = st.number_input("Kapasitas Kendaraan",kapasitas_kendaraan,step=1)
                new_jumlah_kendaraan = st.number_input("Jumlah Kendaraan",jumlah_kendaraan,step=1)
           
            if st.button("Update Task"):
                edit_data_kendaraan(new_id_tipe_kendaraan,new_nama_kendaraan,new_kapasitas_kendaraan,new_jumlah_kendaraan,id_tipe_kendaraan,nama_kendaraan,kapasitas_kendaraan,jumlah_kendaraan)
                st.success("Updated ::{} ::To {}".format(nama_kendaraan,new_nama_kendaraan))

    if option=='Hapus Data':
        st.subheader("Hapus Data kendaraan")
        unique_list = [i[0] for i in view_all_nama_kendaraan()]
        delete_by_nama_kendaraan =  st.selectbox("Pilih Nama kendaraan",unique_list)
        if st.button("Delete"):
            delete_data(delete_by_nama_kendaraan)
            st.warning("Berhasil menghapus: '{}'".format(delete_by_nama_kendaraan))
    
