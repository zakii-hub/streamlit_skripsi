import streamlit as st
import pandas as pd 
from db_data_rincian_barang import * 
import streamlit.components.v1 as stc
from PIL import Image
from st_btn_select import st_btn_select

# Data Viz Pkgs
import plotly.express as px 

def laman_data_rincian_barang():
    st.subheader("Semua Data Rincian Barang")
    result = view_all_data_rincian_barang()
    # st.write(result)
    clean_df = pd.DataFrame(result,columns=["id_barang","nama_barang","panjang_barang","lebar_barang","tinggi_barang","massa_barang","volumetrik_pengiriman","jumlah_barang"])
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
        st.subheader("Tambah Data Rincian Barang")
        col1,col2 = st.columns(2)
        
        with col1:
            id_barang = st.text_input("Id Barang")
            nama_barang = st.text_input("Nama Barang")
            panjang_barang = st.number_input("Panjang Barang", step=1)
            lebar_barang = st.number_input("Lebar Barang", step=1)
            tinggi_barang = st.number_input("Tinggi Barang", step=1)
        with col2:
            massa_barang = st.number_input("Massa Barang",step=1)
            volumetrik_pengiriman = st.number_input("Volumetrik Barang",step=1)
            jumlah_barang = st.number_input("Jumlah Barang",step=1)
        
        if st.button("Tambah Data"):
            add_data_rincian_barang(id_barang,nama_barang,panjang_barang,lebar_barang,tinggi_barang,massa_barang,volumetrik_pengiriman,jumlah_barang)
            st.success("Berhasil menambahkan ::{} ::ke data rincian_barang".format(nama_barang))

    if option=='Ubah Data':
        st.subheader("Ubah Data rincian_barang")
        list_of_nama_rincian_barang = [i[0] for i in view_all_nama_rincian_barang()]
        selected_nama_rincian_barang = st.selectbox("Pilih Nama rincian_barang",list_of_nama_rincian_barang)
        nama_rincian_barang_result = get_nama_rincian_barang(selected_nama_rincian_barang)
        # st.write(task_result)

        if nama_rincian_barang_result:
            id_barang = nama_rincian_barang_result [0][0]
            nama_barang = nama_rincian_barang_result[0][1]
            panjang_barang = nama_rincian_barang_result[0][2]
            lebar_barang = nama_rincian_barang_result[0][3]
            tinggi_barang = nama_rincian_barang_result[0][4]
            massa_barang = nama_rincian_barang_result[0][5]
            volumetrik_pengiriman = nama_rincian_barang_result[0][6]
            jumlah_barang = nama_rincian_barang_result[0][7]

            col1,col2 = st.columns(2)
                
            with col1:
                new_id_barang = st.text_input("Id Barang",id_barang)
                new_nama_barang = st.text_input("Nama Barang",nama_barang)
                new_panjang_barang = st.number_input("Panjang Barang",panjang_barang,step=1)
                new_lebar_barang = st.number_input("Lebar Barang",lebar_barang,step=1)
                new_tinggi_barang = st.number_input("Tinggi Barang",tinggi_barang,step=1)

            with col2:
                new_massa_barang = st.number_input("Massa Barang",massa_barang,step=1)
                new_volumetrik_pengiriman = st.number_input("Volumetrik Pengiriman",volumetrik_pengiriman,step=1)
                new_jumlah_barang = st.number_input("Jumlah Barang",jumlah_barang,step=1)
            if st.button("Update Task"):
                edit_data_rincian_barang((new_id_barang,new_nama_barang,new_panjang_barang,new_lebar_barang,new_tinggi_barang,new_massa_barang,new_volumetrik_pengiriman,new_jumlah_barang,id_barang,nama_barang,panjang_barang,lebar_barang,tinggi_barang,massa_barang,volumetrik_pengiriman,jumlah_barang))
                st.success("Updated ::{} ::To {}".format(nama_barang,new_nama_barang))

    if option=='Hapus Data':
        st.subheader("Hapus Data rincian_barang")
        unique_list = [i[0] for i in view_all_nama_rincian_barang()]
        delete_by_nama_rincian_barang =  st.selectbox("Pilih Nama rincian_barang",unique_list)
        if st.button("Delete"):
            delete_data(delete_by_nama_rincian_barang)
            st.warning("Berhasil menghapus: '{}'".format(delete_by_nama_rincian_barang))
    
