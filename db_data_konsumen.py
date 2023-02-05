import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()


def create_table_data_konsumen():
	c.execute('CREATE TABLE IF NOT EXISTS data_konsumen(id_konsumen TEXT UNIQUE PRIMARY KEY,nama_konsumen TEXT, status_konsumen TEXT, longitude_konsumen INTEGER, latitude_konsumen INTEGER,alamat_konsumen TEXT)')


def add_data_konsumen(id_konsumen,nama_konsumen,status_konsumen,longitude_konsumen,latitude_konsumen,alamat_konsumen):
	c.execute('INSERT INTO data_konsumen(id_konsumen,nama_konsumen,status_konsumen,longitude_konsumen,latitude_konsumen,alamat_konsumen) VALUES (?,?,?,?,?,?)',(id_konsumen,nama_konsumen,status_konsumen,longitude_konsumen,latitude_konsumen,alamat_konsumen))
	conn.commit()


def view_all_data_konsumen():
	c.execute('SELECT * FROM data_konsumen')
	data = c.fetchall()
	return data

def view_all_nama_konsumen():
	c.execute('SELECT DISTINCT nama_konsumen FROM data_konsumen')
	data = c.fetchall()
	return data

def get_nama_konsumen(nama_konsumen):
	c.execute('SELECT * FROM data_konsumen WHERE nama_konsumen="{}"'.format(nama_konsumen))
	data = c.fetchall()
	return data

def get_konsumen_by_status(status_konsumen):
	c.execute('SELECT * FROM data_konsumen WHERE status_konsumen="{}"'.format(status_konsumen))
	data = c.fetchall()


def edit_data_konsumen(new_id_konsumen,new_nama_konsumen,new_status_konsumen,new_longitude_konsumen,new_latitude_konsumen,new_alamat,id_konsumen,nama_konsumen,status_konsumen,longitude_konsumen,latitude_konsumen,alamat_konsumen):
	c.execute("UPDATE data_konsumen SET id_konsumen =?,nama_konsumen=?,status_konsumen=?,longitude_konsumen=?,latitude_konsumen=?,alamat_konsumen=? WHERE id_konsumen =? and nama_konsumen=? and status_konsumen=? and longitude_konsumen=? and latitude_konsumen=? and alamat_konsumen=? ",(new_id_konsumen,new_nama_konsumen,new_status_konsumen,new_longitude_konsumen,new_latitude_konsumen,new_alamat,id_konsumen,nama_konsumen,status_konsumen,longitude_konsumen,latitude_konsumen,alamat_konsumen))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(nama_konsumen):
	c.execute('DELETE FROM data_konsumen WHERE nama_konsumen="{}"'.format(nama_konsumen))
	conn.commit()