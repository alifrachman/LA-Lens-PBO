import wx
from wx.core import NOT_FOUND
import wx.xrc
import gui as frame

import user
import transaksi

class ClassFrame_Utama(frame.Frame_Utama):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.user = user.user()
        self.transaksi = transaksi.Transaksi()

        self.c_idbarang_form.GetSelection()
        self.c_jaminan_form.GetSelection()

        self.id_pinjam, self.value_pinjam = self.transaksi.get_transaksi_berlangsung()

        for num in range(len(self.id_pinjam)):
            self.m_grid31.SetRowLabelValue(num, str(self.id_pinjam[num]))
            
        for i in range(len(self.value_pinjam)):
            for j in range(len(self.value_pinjam[0])):
                if self.value_pinjam[i][j] is None:
                    self.m_grid31.SetCellValue(i, j, "-Belum Kembali-")
                else:
                    self.m_grid31.SetCellValue(i, j, str(self.value_pinjam[i][j]))

        self.c_idbarang_data.SetItems([str(i) for i in self.id_pinjam])

        


    def refresh_table(self):

        self.id_pinjam, self.value_pinjam = self.transaksi.get_transaksi()

        for num in range(len(self.id_pinjam)):
            self.m_grid31.SetRowLabelValue(num, str(self.id_pinjam[num]))
            
        for i in range(len(self.value_pinjam)):
            for j in range(len(self.value_pinjam[0])):
                if self.value_pinjam[i][j] is None:
                    self.m_grid31.SetCellValue(i, j, "-Belum Kembali-")
                else:
                    self.m_grid31.SetCellValue(i, j, str(self.value_pinjam[i][j]))

        self.choice_pengembalian.SetItems([str(i) for i in self.id_pinjam])


    def submit_data( self, event ):
        nama_input = self.input_nama.GetValue()
        telp_input = self.input_telp.GetValue()
        alamat_input = self.input_alamat.GetValue()
        c_idbarang_form = self.c_idbarang_form.GetString(self.c_idbarang_form.GetSelection())
        c_jaminan_form = self.c_jaminan_form.GetString(self.c_jaminan_form.GetSelection())


        self.transaksi.input_transaksi(nama_input, c_idbarang_form, c_jaminan_form, alamat_input, telp_input)
        self.transaksi.get_harga(c_idbarang_form)

        self.input_nama.SetValue(str())
        self.input_telp.SetValue(str())
        self.input_alamat.SetValue(str())
        self.c_idbarang_form.SetSelection(NOT_FOUND) 
        self.c_jaminan_form.SetSelection(NOT_FOUND)

        self.refresh_table()


    def submit_data_pengembalian( self, event ):
        c_idbarang_data = self.c_idbarang_data.GetString(self.c_idbarang_data.GetSelection())
        
        self.transaksi.pengembalian_barang(c_idbarang_data)
        
        self.refresh_table()


class ClassFrame_Login(frame.Frame_Login):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.user = user.user()

    def submit_login(self, event):
        username = self.username_input.GetValue()
        password = self.password_input.GetValue()

        auth_login = self.user.auth_login(username, password)
        print(auth_login)
        if auth_login == True:
            frame_new = ClassFrame_Utama()
            frame_new.Show()
            self.Close()

        self.username_input.SetValue(str())
        self.password_input.SetValue(str())

class Main():

    def __init__(self):
        app = wx.App()
        frame = ClassFrame_Login()
        frame.Show()
        app.MainLoop()
    

if __name__ == "__main__":
	login = Main()
