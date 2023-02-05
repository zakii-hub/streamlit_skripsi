import streamlit as st
import pandas as pd 
from db_data_rincian_barang import * 
import streamlit.components.v1 as stc
from PIL import Image
from st_btn_select import st_btn_select

# Data Viz Pkgs
import plotly.express as px 

def laman_data_rincian_barang():
    st.subheader("Semua Data rincian_barang (Kantor)")
    result = view_all_data_rincian_barang()
    # st.write(result)
    clean_df = pd.DataFrame(result,columns=["id_rincian_barang","nama_rincian_barang","status_rincian_barang","longitude_rincian_barang","latitude_rincian_barang","alamat_rincian_barang"])
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
        st.subheader("Tambah Data rincian_barang")
        col1,col2 = st.columns(2)
        
        with col1:
            id_rincian_barang = st.text_input("Id rincian_barang")
            nama_rincian_barang = st.text_input("Nama rincian_barang")
            status_rincian_barang = st.selectbox("Status",["Active","In-Active"])

        with col2:
            longitude_rincian_barang = st.number_input("Longitude rincian_barang",step=1e-15,format="%.15f")
            latitude_rincian_barang = st.number_input("Latitude rincian_barang",step=1e-15,format="%.15f")
        
        alamat_rincian_barang = st.text_area("Alamat rincian_barang")

        if st.button("Tambah Data"):
            add_data_rincian_barang(id_rincian_barang,nama_rincian_barang,status_rincian_barang,longitude_rincian_barang,latitude_rincian_barang,alamat_rincian_barang)
            st.success("Berhasil menambahkan ::{} ::ke data rincian_barang".format(nama_rincian_barang))

    if option=='Ubah Data':
        st.subheader("Ubah Data rincian_barang")
        list_of_nama_rincian_barang = [i[0] for i in view_all_nama_rincian_barang()]
        selected_nama_rincian_barang = st.selectbox("Pilih Nama rincian_barang",list_of_nama_rincian_barang)
        nama_rincian_barang_result = get_nama_rincian_barang(selected_nama_rincian_barang)
        # st.write(task_result)

        if nama_rincian_barang_result:
            id_rincian_barang = nama_rincian_barang_result [0][0]
            nama_rincian_barang = nama_rincian_barang_result[0][1]
            status_rincian_barang = nama_rincian_barang_result[0][2]
            longitude_rincian_barang = nama_rincian_barang_result[0][3]
            latitude_rincian_barang = nama_rincian_barang_result[0][4]
            alamat_rincian_barang = nama_rincian_barang_result[0][5]

            col1,col2 = st.columns(2)
                
            with col1:
                new_id_rincian_barang = st.text_input("Id rincian_barang",id_rincian_barang)
                new_nama_rincian_barang = st.text_input("Nama rincian_barang",nama_rincian_barang)
                new_status_rincian_barang = st.selectbox(status_rincian_barang,["Active","In-Active"])
            with col2:
                new_longitude_rincian_barang = st.number_input("Longitude rincian_barang",step=1e-15,format="%.15f")
                new_latitude_rincian_barang = st.number_input("Latitude rincian_barang",step=1e-15,format="%.15f")
            new_alamat_rincian_barang = st.text_area("Alamat rincian_barang",alamat_rincian_barang)
            if st.button("Update Task"):
                edit_data_rincian_barang(new_id_rincian_barang,new_nama_rincian_barang,new_status_rincian_barang,new_longitude_rincian_barang,new_latitude_rincian_barang,new_alamat_rincian_barang,id_rincian_barang,nama_rincian_barang,status_rincian_barang,longitude_rincian_barang,latitude_rincian_barang,alamat_rincian_barang)
                st.success("Updated ::{} ::To {}".format(nama_rincian_barang,new_nama_rincian_barang))

    if option=='Hapus Data':
        st.subheader("Hapus Data rincian_barang")
        unique_list = [i[0] for i in view_all_nama_rincian_barang()]
        delete_by_nama_rincian_barang =  st.selectbox("Pilih Nama rincian_barang",unique_list)
        if st.button("Delete"):
            delete_data(delete_by_nama_rincian_barang)
            st.warning("Berhasil menghapus: '{}'".format(delete_by_nama_rincian_barang))
    
