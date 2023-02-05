import streamlit as st
import pandas as pd 
from db_data_depot import * 
import streamlit.components.v1 as stc
from PIL import Image
from st_btn_select import st_btn_select

# Data Viz Pkgs
import plotly.express as px 

def laman_data_depot():
    st.subheader("Semua Data Depot (Kantor)")
    result = view_all_data_depot()
    # st.write(result)
    clean_df = pd.DataFrame(result,columns=["id_depot","nama_depot","status_depot","longitude_depot","latitude_depot","alamat_depot"])
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
        st.subheader("Tambah Data Depot")
        col1,col2 = st.columns(2)
        
        with col1:
            id_depot = st.text_input("Id Depot")
            nama_depot = st.text_input("Nama Depot")
            status_depot = st.selectbox("Status",["Active","In-Active"])

        with col2:
            longitude_depot = st.number_input("Longitude Depot",step=1e-15,format="%.15f")
            latitude_depot = st.number_input("Latitude Depot",step=1e-15,format="%.15f")
        
        alamat_depot = st.text_area("Alamat Depot")

        if st.button("Tambah Data"):
            add_data_depot(id_depot,nama_depot,status_depot,longitude_depot,latitude_depot,alamat_depot)
            st.success("Berhasil menambahkan ::{} ::ke data depot".format(nama_depot))

    if option=='Ubah Data':
        st.subheader("Ubah Data Depot")
        list_of_nama_depot = [i[0] for i in view_all_nama_depot()]
        selected_nama_depot = st.selectbox("Pilih Nama depot",list_of_nama_depot)
        nama_depot_result = get_nama_depot(selected_nama_depot)
        # st.write(task_result)

        if nama_depot_result:
            id_depot = nama_depot_result [0][0]
            nama_depot = nama_depot_result[0][1]
            status_depot = nama_depot_result[0][2]
            longitude_depot = nama_depot_result[0][3]
            latitude_depot = nama_depot_result[0][4]
            alamat_depot = nama_depot_result[0][5]

            col1,col2 = st.columns(2)
                
            with col1:
                new_id_depot = st.text_input("Id Depot",id_depot)
                new_nama_depot = st.text_input("Nama Depot",nama_depot)
                new_status_depot = st.selectbox(status_depot,["Active","In-Active"])
            with col2:
                new_longitude_depot = st.number_input("Longitude Depot",longitude_depot,step=1e-15,format="%.15f")
                new_latitude_depot = st.number_input("Latitude Depot",latitude_depot,step=1e-15,format="%.15f")
            new_alamat_depot = st.text_area("Alamat Depot",alamat_depot)
            if st.button("Update Task"):
                edit_data_depot(new_id_depot,new_nama_depot,new_status_depot,new_longitude_depot,new_latitude_depot,new_alamat_depot,id_depot,nama_depot,status_depot,longitude_depot,latitude_depot,alamat_depot)
                st.success("Updated ::{} ::To {}".format(nama_depot,new_nama_depot))

    if option=='Hapus Data':
        st.subheader("Hapus Data Depot")
        unique_list = [i[0] for i in view_all_nama_depot()]
        delete_by_nama_depot =  st.selectbox("Pilih Nama Depot",unique_list)
        if st.button("Delete"):
            delete_data(delete_by_nama_depot)
            st.warning("Berhasil menghapus: '{}'".format(delete_by_nama_depot))
    
