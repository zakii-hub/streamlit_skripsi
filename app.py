import streamlit as st
import pandas as pd 
from db_fxns import *
from db_data_depot import *
from db_data_kendaraan import *
from db_data_konsumen import *
from db_data_rincian_barang import *
from laman_data_depot import *
from laman_data_kendaraan import *
from laman_data_konsumen import * 
from laman_data_rincian_barang import * 
import streamlit.components.v1 as stc
from PIL import Image
from st_btn_select import st_btn_select

# Data Viz Pkgs
import plotly.express as px 

#Customized Icon
img = Image.open('icon_pt_allure_alluminio.png')
st.set_page_config(page_title='CVRPTW PT ALLURE ALLUMINIO', page_icon=img)

HTML_BANNER = """
    <div style="background-color:#464e5f;padding:5px;border-radius:5px">
    <h1 style="color:white;text-align:center;font-size:25px;">Optimasi Rute Pengiriman dengan Greedy Search dan Simulated Annealing</h1>
    <p style="color:white;text-align:center;">Dibuat oleh Muhammad Zakii Rofii
	<br>
	Sebagai produk dari penelitian skripsi</p>


    </div>
    """

# hide_st_style = """

#             <style>

#             #MainMenu {visibility: hidden;}

#             footer {visibility: hidden;}

#             header {visibility: hidden;}

#             .css-1rs6os {visibility: hidden;}

#             .css-17ziqus {visibility: hidden;}

#             """

# st.markdown(hide_st_style,unsafe_allow_html=True)

def main():
	stc.html(HTML_BANNER)


	menu = ["Home","Data Depot (Kantor)","Data Kendaraan","Data Konsumen","Data Rincian Barang","Optimasi dengan Data CRUD","Optimasi dengan Dataset","About"]
	choice = st.sidebar.selectbox("Menu",menu)
	create_table()
	create_table_data_depot()
	create_table_data_kendaraan()
	create_table_data_konsumen()
	create_table_data_rincian_barang()

	if choice == "Home":

		# page = st_btn_select(
		# # The different pages
		# ('home', 'about', 'docs', 'playground'),
		# # Enable navbar
		
		# # You can pass a formatting function. Here we capitalize the options
		
		# )

		# # Display the right things according to the page
		# if page == 'home':
		# 	st.write('HOMEPAGE')


		# st.subheader("Semua Data")
		st.subheader("Semua Data")
		result = view_all_data()
		# st.write(result)
		clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
		st.dataframe(clean_df)

		st.subheader("Task Status")
		task_df = clean_df['Status'].value_counts().to_frame()
		# st.dataframe(task_df)
		task_df = task_df.reset_index()
		st.dataframe(task_df)

		p1 = px.pie(task_df,names='index',values='Status')
		st.plotly_chart(p1,use_container_width=True)
		
		option = st_btn_select(('#','Add Data', 'Edit Data', 'Delete Data'),index=0)
		button1 = st.button('Refresh Data')
		if button1=='Refresh Data':
			st.experimental_rerun()
			

		if option=='Add Data':
			st.subheader("Add Items")
			col1,col2 = st.columns(2)
			
			with col1:
				task = st.text_area("Task To Do")

			with col2:
				task_status = st.selectbox("Status",["ToDo","Doing","Done"])
				task_due_date = st.date_input("Due Date")

			if st.button("Add Task"):
				add_data(task,task_status,task_due_date)
				st.success("Added ::{} ::To Task".format(task))

		if option=='Edit Data':
			st.subheader("Edit Items")
			list_of_tasks = [i[0] for i in view_all_task_names()]
			selected_task = st.selectbox("Task",list_of_tasks)
			task_result = get_task(selected_task)
			# st.write(task_result)

			if task_result:
				task = task_result[0][0]
				task_status = task_result[0][1]
				task_due_date = task_result[0][2]

				col1,col2 = st.columns(2)
					
				with col1:
					new_task = st.text_area("Task To Do",task)
				with col2:
					new_task_status = st.selectbox(task_status,["ToDo","Doing","Done"])
					new_task_due_date = st.date_input(task_due_date)

				if st.button("Update Task"):
					edit_task_data(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date)
					st.success("Updated ::{} ::To {}".format(task,new_task))

		if option=='Delete Data':
			st.subheader("Delete Data")
			unique_list = [i[0] for i in view_all_task_names()]
			delete_by_task_name =  st.selectbox("Select Task",unique_list)
			if st.button("Delete"):
				delete_data(delete_by_task_name)
				st.warning("Deleted: '{}'".format(delete_by_task_name))

	if choice == "Data Depot (Kantor)":

		# page = st_btn_select(
		# # The different pages
		# ('home', 'about', 'docs', 'playground'),
		# # Enable navbar
		
		# # You can pass a formatting function. Here we capitalize the options
		
		# )

		# # Display the right things according to the page
		# if page == 'home':
		# 	st.write('HOMEPAGE')


		# st.subheader("Semua Data")
		laman_data_depot()

	if choice =="Data Kendaraan":
		laman_data_kendaraan()

	if choice =="Data Konsumen":
		laman_data_konsumen()
	
	if choice =="Data Rincian Barang":
		laman_data_rincian_barang()

	if choice == "About":
		st.subheader("Optimasi Rute Pengiriman dengan Greedy Search dan Simulated Annealing")
		st.write("Dibuat oleh Muhammad Zakii Rofii")
		st.text("Sebagai hasil produk penelitian dari skripsi")



if __name__ == '__main__':
	main()

