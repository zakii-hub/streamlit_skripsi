import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()


def create_table_data_kendaraan():
	c.execute('CREATE TABLE IF NOT EXISTS data_kendaraan(id_tipe_kendaraan TEXT UNIQUE PRIMARY KEY, nama_kendaraan TEXT, kapasitas_kendaraan INTEGER, jumlah_kendaraan INTEGER)')


def add_data_kendaraan(id_tipe_kendaraan,nama_kendaraan,kapasitas_kendaraan,jumlah_kendaraan):
	c.execute('INSERT INTO data_kendaraan(id_tipe_kendaraan,nama_kendaraan,kapasitas_kendaraan,jumlah_kendaraan) VALUES (?,?,?,?)',(id_tipe_kendaraan,nama_kendaraan,kapasitas_kendaraan,jumlah_kendaraan))
	conn.commit()


def view_all_data_kendaraan():
	c.execute('SELECT * FROM data_kendaraan')
	data = c.fetchall()
	return data

def view_all_nama_kendaraan():
	c.execute('SELECT DISTINCT nama_kendaraan FROM data_kendaraan')
	data = c.fetchall()
	return data

def get_nama_kendaraan(nama_kendaraan):
	c.execute('SELECT * FROM data_kendaraan WHERE nama_kendaraan="{}"'.format(nama_kendaraan))
	data = c.fetchall()
	return data

def get_kendaraan_by_kapasitas(kapasitas_kendaraan):
	c.execute('SELECT * FROM data_kendaraan WHERE kapasitas_kendaraan="{}"'.format(kapasitas_kendaraan))
	data = c.fetchall()


def edit_data_kendaraan(new_id_tipe_kendaraan,new_nama_kendaraan,new_kapasitas_kendaraan,new_jumlah_kendaraan,id_tipe_kendaraan,nama_kendaraan,kapasitas_kendaraan,jumlah_kendaraan):
	c.execute("UPDATE data_kendaraan SET id_tipe_kendaraan =?,nama_kendaraan=?,kapasitas_kendaraan=?,jumlah_kendaraan=? WHERE id_tipe_kendaraan =? and nama_kendaraan=? and kapasitas_kendaraan=? and jumlah_kendaraan=?",(new_id_tipe_kendaraan,new_nama_kendaraan,new_kapasitas_kendaraan,new_jumlah_kendaraan,id_tipe_kendaraan,nama_kendaraan,kapasitas_kendaraan,jumlah_kendaraan))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(nama_kendaraan):
	c.execute('DELETE FROM data_kendaraan WHERE nama_kendaraan="{}"'.format(nama_kendaraan))
	conn.commit()