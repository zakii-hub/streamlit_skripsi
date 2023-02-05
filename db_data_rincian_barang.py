import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()


def create_table_data_rincian_barang():
	c.execute('CREATE TABLE IF NOT EXISTS data_rincian_barang(id_rincian_barang TEXT UNIQUE PRIMARY KEY,nama_rincian_barang TEXT, status_rincian_barang TEXT, longitude_rincian_barang INTEGER, latitude_rincian_barang INTEGER,alamat_rincian_barang TEXT)')


def add_data_rincian_barang(id_rincian_barang,nama_rincian_barang,status_rincian_barang,longitude_rincian_barang,latitude_rincian_barang,alamat_rincian_barang):
	c.execute('INSERT INTO data_rincian_barang(id_rincian_barang,nama_rincian_barang,status_rincian_barang,longitude_rincian_barang,latitude_rincian_barang,alamat_rincian_barang) VALUES (?,?,?,?,?,?)',(id_rincian_barang,nama_rincian_barang,status_rincian_barang,longitude_rincian_barang,latitude_rincian_barang,alamat_rincian_barang))
	conn.commit()


def view_all_data_rincian_barang():
	c.execute('SELECT * FROM data_rincian_barang')
	data = c.fetchall()
	return data

def view_all_nama_rincian_barang():
	c.execute('SELECT DISTINCT nama_rincian_barang FROM data_rincian_barang')
	data = c.fetchall()
	return data

def get_nama_rincian_barang(nama_rincian_barang):
	c.execute('SELECT * FROM data_rincian_barang WHERE nama_rincian_barang="{}"'.format(nama_rincian_barang))
	data = c.fetchall()
	return data

def get_rincian_barang_by_status(status_rincian_barang):
	c.execute('SELECT * FROM data_rincian_barang WHERE status_rincian_barang="{}"'.format(status_rincian_barang))
	data = c.fetchall()


def edit_data_rincian_barang(new_id_rincian_barang,new_nama_rincian_barang,new_status_rincian_barang,new_longitude_rincian_barang,new_latitude_rincian_barang,new_alamat,id_rincian_barang,nama_rincian_barang,status_rincian_barang,longitude_rincian_barang,latitude_rincian_barang,alamat_rincian_barang):
	c.execute("UPDATE data_rincian_barang SET id_rincian_barang =?,nama_rincian_barang=?,status_rincian_barang=?,longitude_rincian_barang=?,latitude_rincian_barang=?,alamat_rincian_barang=? WHERE id_rincian_barang =? and nama_rincian_barang=? and status_rincian_barang=? and longitude_rincian_barang=? and latitude_rincian_barang=? and alamat_rincian_barang=? ",(new_id_rincian_barang,new_nama_rincian_barang,new_status_rincian_barang,new_longitude_rincian_barang,new_latitude_rincian_barang,new_alamat,id_rincian_barang,nama_rincian_barang,status_rincian_barang,longitude_rincian_barang,latitude_rincian_barang,alamat_rincian_barang))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(nama_rincian_barang):
	c.execute('DELETE FROM data_rincian_barang WHERE nama_rincian_barang="{}"'.format(nama_rincian_barang))
	conn.commit()