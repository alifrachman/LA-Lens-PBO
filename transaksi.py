from datetime import date, datetime
import locale

from wx.core import Locale
from conn import Connect

class Transaksi(Connect):
    
    def __init__(self) -> None:
        super().__init__()
    
    def input_transaksi(self, nama_input, c_idbarang_form, c_jaminan_form, alamat_input, telp_input):
        cursor = self.db.cursor()

        tanggal_sewa = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        sql_query = """INSERT INTO transaksi VALUES ("", %s, %s, NULL, %s, %s, %s, %s)"""
        values = (c_idbarang_form, tanggal_sewa, nama_input, c_jaminan_form, alamat_input, telp_input)
        cursor.execute(sql_query, values)

        self.db.commit()
        return True

    def get_harga(self, c_idbarang_form):
        cursor = self.db.cursor()
        sql_query = """SELECT harga FROM katalog_barang where id_barang == %s"""
        value = (c_idbarang_form,)
        cursor.execute(sql_query, value)

        result = cursor

        return result

    def get_hari(self, date_start, date_end):
        locale.setlocale(locale.LC_ALL, 'en_US.utf8')

        if date_end == None:
            date_start = datetime.strptime(date_start, "%d/%m/%Y, %H:%M:%S")
            return abs((datetime.now() - date_start).days)

        else:
            date_start = datetime.strptime(date_start, "%d/%m/%Y, %H:%M:%S")
            date_end = datetime.strptime(date_end, "%d/%m/%Y, %H:%M:%S")
            return abs((date_end - date_start).days)

    

    def get_transaksi(self):
        cursor = self.db.cursor()
        sql_query = """SELECT * FROM transaksi"""
        cursor.execute(sql_query)

        result = cursor.fetchall()

        id_pinjam = []
        value_pinjam = []

        for i in result:
            temp = []
            for idx, j in enumerate(i):
                if idx == 0:
                    id_pinjam.append(i[0])
                else:
                    temp.append(j)
            value_pinjam.append(temp)


        for i in value_pinjam:
            for idx, j in enumerate(i):
                if idx == 0:
                    harga = self.get_harga(i[0])

                elif idx == 1:
                    hari = self.get_hari(i[1], i[2])

            i.append(hari)
            i.append(hari * harga)


        return id_pinjam, value_pinjam

    def get_transaksi_berlangsung(self):
        cursor = self.db.cursor()
        sql_query = """SELECT * FROM transaksi WHERE tanggal_kembali IS NULL"""
        cursor.execute(sql_query)

        result = cursor.fetchall()

        id_pinjam = []
        value_pinjam = []

        for i in result:
            temp = []
            for idx, j in enumerate(i):
                if idx == 0:
                    id_pinjam.append(i[0])
                else:
                    temp.append(j)
            value_pinjam.append(temp)

        for i in value_pinjam:
            for idx, j in enumerate(i):
                if idx == 0:
                    harga = self.get_harga(i[0])

                elif idx == 1:
                    hari = self.get_hari(i[1], i[2])

            i.append(hari)
            i.append(hari * harga)

        return id_pinjam, value_pinjam


    def pengembalian_barang(self, c_idbarang_data):
        cursor = self.db.cursor()

        tanggal_kembali = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        sql_query = """UPDATE transaksi SET tanggal_kembali = %s WHERE id_transaksi = %s"""
        values = (tanggal_kembali, c_idbarang_data)
        cursor.execute(sql_query, values)

        self.db.commit()

    def katalog_barang(self, m_grid3):
        cursor = self.db.cursor()
        sql_query = """SELECT * FROM katalog_barang"""
        cursor.execute(sql_query)

        result = cursor.fetchall()

        id_pinjam = []
        value_pinjam = []

        for i in result:
            temp = []
            for idx, j in enumerate(i):
                if idx == 0:
                    id_pinjam.append(i[0])
                else:
                    temp.append(j)
            value_pinjam.append(temp)


        for i in value_pinjam:
            for idx, j in enumerate(i):
                if idx == 0:
                    harga = self.get_harga(i[0])

                elif idx == 1:
                    hari = self.get_hari(i[1], i[2])

            i.append(hari)
            i.append(hari * harga)


        return id_pinjam, value_pinjam



