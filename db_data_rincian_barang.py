import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()


def create_table_data_rincian_barang():
	c.execute('CREATE TABLE IF NOT EXISTS data_rincian_barang(id_barang TEXT UNIQUE PRIMARY KEY,nama_barang TEXT, panjang_barang INTEGER, lebar_barang INTEGER, tinggi_barang INTEGER, massa_barang INTEGER, volumetrik_pengiriman INTEGER, jumlah_barang INTEGER)')


def add_data_rincian_barang(id_barang,nama_barang,panjang_barang,lebar_barang,tinggi_barang,massa_barang,volumetrik_pengiriman,jumlah_barang):
	c.execute('INSERT INTO data_rincian_barang(id_barang,nama_barang,panjang_barang,lebar_barang,tinggi_barang,massa_barang,volumetrik_pengiriman,jumlah_barang) VALUES (?,?,?,?,?,?,?,?)',(id_barang,nama_barang,panjang_barang,lebar_barang,tinggi_barang,massa_barang,volumetrik_pengiriman,jumlah_barang))
	conn.commit()


def view_all_data_rincian_barang():
	c.execute('SELECT * FROM data_rincian_barang')
	data = c.fetchall()
	return data

def view_all_nama_rincian_barang():
	c.execute('SELECT DISTINCT nama_barang FROM data_rincian_barang')
	data = c.fetchall()
	return data

def get_nama_rincian_barang(nama_barang):
	c.execute('SELECT * FROM data_rincian_barang WHERE nama_barang="{}"'.format(nama_barang))
	data = c.fetchall()
	return data

# def get_rincian_barang_by_status(status_rincian_barang):
# 	c.execute('SELECT * FROM data_rincian_barang WHERE status_rincian_barang="{}"'.format(status_rincian_barang))
# 	data = c.fetchall()


def edit_data_rincian_barang(new_id_barang,new_nama_barang,new_panjang_barang,new_lebar_barang,new_tinggi_barang,new_massa_barang,new_volumetrik_pengiriman,new_jumlah_barang,id_barang,nama_barang,panjang_barang,lebar_barang,tinggi_barang,massa_barang,volumetrik_pengiriman,jumlah_barang):
	c.execute("UPDATE data_rincian_barang SET id_barang =?,nama_barang=?,panjang_barang=?,lebar_barang=?,tinggi_barang=?,massa_barang=?,volumetrik_pengiriman=?,jumlah_barang=? WHERE id_barang =? and nama_barang=? and panjang_barang=? and lebar_barang=? and tinggi_barang=? and volumetrik_pengiriman=? and jumlah_barang=? ",(new_id_barang,new_nama_barang,new_panjang_barang,new_lebar_barang,new_tinggi_barang,new_massa_barang,new_volumetrik_pengiriman,new_jumlah_barang,id_barang,nama_barang,panjang_barang,lebar_barang,tinggi_barang,massa_barang,volumetrik_pengiriman,jumlah_barang))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(nama_barang):
	c.execute('DELETE FROM data_rincian_barang WHERE nama_barang="{}"'.format(nama_barang))
	conn.commit()
