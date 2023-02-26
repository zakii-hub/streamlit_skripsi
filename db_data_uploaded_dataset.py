import streamlit as st
import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()


def create_table_data_uploaded_dataset():
	c.execute('''CREATE TABLE IF NOT EXISTS uploaded_dataset
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              data BLOB NOT NULL)''')

def save_data_uploaded_dataset(file_name, file_data):
	c.execute('INSERT INTO uploaded_dataset (name, data) VALUES (?, ?)',(file_name, file_data))
	conn.commit()
	st.success('File saved successfully!')


# def add_data_uploaded_dataset(id_depot,nama_depot,status_depot,longitude_depot,latitude_depot,alamat_depot):
# 	c.execute('INSERT INTO data_uploaded_dataset(id_depot,nama_depot,status_depot,longitude_depot,latitude_depot,alamat_depot) VALUES (?,?,?,?,?,?)',(id_depot,nama_depot,status_depot,longitude_depot,latitude_depot,alamat_depot))
# 	conn.commit()


def view_all_data_uploaded_dataset():
	c.execute('SELECT * FROM uploaded_dataset')
	data = c.fetchall()
	return data

# def view_all_nama_depot():
# 	c.execute('SELECT DISTINCT nama_depot FROM data_uploaded_dataset')
# 	data = c.fetchall()
# 	return data

# def get_nama_depot(nama_depot):
# 	c.execute('SELECT * FROM data_uploaded_dataset WHERE nama_depot="{}"'.format(nama_depot))
# 	data = c.fetchall()
# 	return data

# def get_depot_by_status(status_depot):
# 	c.execute('SELECT * FROM data_uploaded_dataset WHERE status_depot="{}"'.format(status_depot))
# 	data = c.fetchall()


# def edit_data_uploaded_dataset(new_id_depot,new_nama_depot,new_status_depot,new_longitude_depot,new_latitude_depot,new_alamat,id_depot,nama_depot,status_depot,longitude_depot,latitude_depot,alamat_depot):
# 	c.execute("UPDATE data_uploaded_dataset SET id_depot =?,nama_depot=?,status_depot=?,longitude_depot=?,latitude_depot=?,alamat_depot=? WHERE id_depot =? and nama_depot=? and status_depot=? and longitude_depot=? and latitude_depot=? and alamat_depot=? ",(new_id_depot,new_nama_depot,new_status_depot,new_longitude_depot,new_latitude_depot,new_alamat,id_depot,nama_depot,status_depot,longitude_depot,latitude_depot,alamat_depot))
# 	conn.commit()
# 	data = c.fetchall()
# 	return data

# def delete_data(nama_depot):
# 	c.execute('DELETE FROM data_uploaded_dataset WHERE nama_depot="{}"'.format(nama_depot))
# 	conn.commit()