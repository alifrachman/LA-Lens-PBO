# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class Frame_Utama
###########################################################################

class Frame_Utama ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1036,982 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebook1.SetFont( wx.Font( 10, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Mongolian Baiti" ) )
		self.m_notebook1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		self.m_notebook1.SetBackgroundColour( wx.Colour( 128, 128, 128 ) )

		self.m_panel4 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4.SetBackgroundColour( wx.Colour( 192, 192, 192 ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )


		bSizer5.Add( ( 0, 50), 0, wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"KATALOG BARANG", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Mongolian Baiti" ) )

		bSizer5.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer5.Add( ( 0, 55), 0, wx.EXPAND, 5 )

		self.m_grid3 = wx.grid.Grid( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid3.CreateGrid( 12, 3 )
		self.m_grid3.EnableEditing( True )
		self.m_grid3.EnableGridLines( True )
		self.m_grid3.EnableDragGridSize( False )
		self.m_grid3.SetMargins( 0, 0 )

		# Columns
		self.m_grid3.SetColSize( 0, 130 )
		self.m_grid3.SetColSize( 1, 175 )
		self.m_grid3.SetColSize( 2, 100 )
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelValue( 0, u"ID Barang" )
		self.m_grid3.SetColLabelValue( 1, u"Nama Barang" )
		self.m_grid3.SetColLabelValue( 2, u"Harga" )
		self.m_grid3.SetColLabelValue( 3, wx.EmptyString )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid3.SetRowSize( 0, 40 )
		self.m_grid3.SetRowSize( 1, 40 )
		self.m_grid3.SetRowSize( 2, 40 )
		self.m_grid3.SetRowSize( 3, 40 )
		self.m_grid3.SetRowSize( 4, 40 )
		self.m_grid3.SetRowSize( 5, 40 )
		self.m_grid3.SetRowSize( 6, 40 )
		self.m_grid3.SetRowSize( 7, 40 )
		self.m_grid3.SetRowSize( 8, 40 )
		self.m_grid3.SetRowSize( 9, 40 )
		self.m_grid3.SetRowSize( 10, 40 )
		self.m_grid3.SetRowSize( 11, 40 )
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 80 )
		self.m_grid3.SetRowLabelValue( 0, wx.EmptyString )
		self.m_grid3.SetRowLabelValue( 1, wx.EmptyString )
		self.m_grid3.SetRowLabelValue( 2, wx.EmptyString )
		self.m_grid3.SetRowLabelValue( 3, wx.EmptyString )
		self.m_grid3.SetRowLabelValue( 4, wx.EmptyString )
		self.m_grid3.SetRowLabelValue( 5, wx.EmptyString )
		self.m_grid3.SetRowLabelValue( 6, wx.EmptyString )
		self.m_grid3.SetRowLabelValue( 7, wx.EmptyString )
		self.m_grid3.SetRowLabelValue( 8, wx.EmptyString )
		self.m_grid3.SetRowLabelValue( 9, wx.EmptyString )
		self.m_grid3.SetRowLabelValue( 10, wx.EmptyString )
		self.m_grid3.SetRowLabelValue( 11, wx.EmptyString )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.m_grid3.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_grid3.SetLabelFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		# Cell Defaults
		self.m_grid3.SetDefaultCellBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_grid3.SetDefaultCellTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		bSizer5.Add( self.m_grid3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel4.SetSizer( bSizer5 )
		self.m_panel4.Layout()
		bSizer5.Fit( self.m_panel4 )
		self.m_notebook1.AddPage( self.m_panel4, u"Katalog", True )
		self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetBackgroundColour( wx.Colour( 192, 192, 192 ) )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )


		bSizer11.Add( ( 0, 50), 0, wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"FORM PEMINJAMAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 14, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Mongolian Baiti" ) )

		bSizer11.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer11.Add( ( 0, 55), 0, wx.EXPAND, 5 )

		fgSizer4 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer4.SetMinSize( wx.Size( 350,250 ) )
		self.m_staticText22 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Nama Pelanggan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( 12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Mongolian Baiti" ) )

		fgSizer4.Add( self.m_staticText22, 0, wx.ALL, 5 )


		fgSizer4.Add( ( 100, 0), 1, wx.EXPAND, 5 )

		self.input_nama = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer4.Add( self.input_nama, 0, wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"No Telepon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		self.m_staticText24.SetFont( wx.Font( 12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Mongolian Baiti" ) )

		fgSizer4.Add( self.m_staticText24, 0, wx.ALL, 5 )


		fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_telp = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer4.Add( self.input_telp, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Alamat Lengkap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		self.m_staticText25.SetFont( wx.Font( 12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Mongolian Baiti" ) )

		fgSizer4.Add( self.m_staticText25, 0, wx.ALL, 5 )


		fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_alamat = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer4.Add( self.input_alamat, 0, wx.ALL, 5 )

		self.m_staticText26 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"ID Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		self.m_staticText26.SetFont( wx.Font( 12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Mongolian Baiti" ) )

		fgSizer4.Add( self.m_staticText26, 0, wx.ALL, 5 )


		fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		c_idbarang_formChoices = [ u"1001", u"1002", u"1003", u"1004", u"1005", u"2001", u"2002", u"2003", u"2004", u"2005", u"2006", u"2007" ]
		self.c_idbarang_form = wx.Choice( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), c_idbarang_formChoices, 0 )
		self.c_idbarang_form.SetSelection( 0 )
		fgSizer4.Add( self.c_idbarang_form, 0, wx.ALL, 5 )

		self.m_staticText27 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Jaminan Peminjam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		self.m_staticText27.SetFont( wx.Font( 12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Mongolian Baiti" ) )

		fgSizer4.Add( self.m_staticText27, 0, wx.ALL, 5 )


		fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		c_jaminan_formChoices = [ u"KTP", u"SIM", u"Kartu Pelajar", u"KTM" ]
		self.c_jaminan_form = wx.Choice( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), c_jaminan_formChoices, 0 )
		self.c_jaminan_form.SetSelection( 0 )
		fgSizer4.Add( self.c_jaminan_form, 0, wx.ALL, 5 )


		bSizer11.Add( fgSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )


		bSizer13.Add( ( 0, 20), 0, wx.EXPAND, 5 )

		self.b_submit_form = wx.Button( self.m_panel3, wx.ID_ANY, u"SUBMIT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.b_submit_form.SetFont( wx.Font( 11, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Mongolian Baiti" ) )
		self.b_submit_form.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.b_submit_form.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer13.Add( self.b_submit_form, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer11.Add( bSizer13, 1, wx.EXPAND, 5 )


		self.m_panel3.SetSizer( bSizer11 )
		self.m_panel3.Layout()
		bSizer11.Fit( self.m_panel3 )
		self.m_notebook1.AddPage( self.m_panel3, u"Form Peminjaman", False )
		self.m_panel41 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel41.SetBackgroundColour( wx.Colour( 192, 192, 192 ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )


		bSizer6.Add( ( 0, 15), 0, wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( self.m_panel41, wx.ID_ANY, u"TABEL DATA PEMINJAMAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 14, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Mongolian Baiti" ) )

		bSizer6.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer6.Add( ( 0, 20), 0, wx.EXPAND, 5 )

		self.m_grid31 = wx.grid.Grid( self.m_panel41, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid31.CreateGrid( 10, 9 )
		self.m_grid31.EnableEditing( True )
		self.m_grid31.EnableGridLines( True )
		self.m_grid31.EnableDragGridSize( False )
		self.m_grid31.SetMargins( 0, 0 )

		# Columns
		self.m_grid31.SetColSize( 0, 100 )
		self.m_grid31.SetColSize( 1, 175 )
		self.m_grid31.SetColSize( 2, 175 )
		self.m_grid31.SetColSize( 3, 125 )
		self.m_grid31.SetColSize( 4, 75 )
		self.m_grid31.SetColSize( 5, 100 )
		self.m_grid31.SetColSize( 6, 100 )
		self.m_grid31.SetColSize( 7, 75 )
		self.m_grid31.SetColSize( 8, 125 )
		self.m_grid31.EnableDragColMove( False )
		self.m_grid31.EnableDragColSize( True )
		self.m_grid31.SetColLabelSize( 30 )
		self.m_grid31.SetColLabelValue( 0, u"ID Barang" )
		self.m_grid31.SetColLabelValue( 1, u"Tanggal Sewa" )
		self.m_grid31.SetColLabelValue( 2, u"Tanggal Kembali" )
		self.m_grid31.SetColLabelValue( 3, u"Nama Pelanggan" )
		self.m_grid31.SetColLabelValue( 4, u"Jaminan" )
		self.m_grid31.SetColLabelValue( 5, u"Alamat" )
		self.m_grid31.SetColLabelValue( 6, u"No. Telp" )
		self.m_grid31.SetColLabelValue( 7, u"Hari" )
		self.m_grid31.SetColLabelValue( 8, u"Biaya Total" )
		self.m_grid31.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid31.SetRowSize( 0, 40 )
		self.m_grid31.SetRowSize( 1, 40 )
		self.m_grid31.SetRowSize( 2, 40 )
		self.m_grid31.SetRowSize( 3, 40 )
		self.m_grid31.SetRowSize( 4, 40 )
		self.m_grid31.SetRowSize( 5, 40 )
		self.m_grid31.SetRowSize( 6, 40 )
		self.m_grid31.SetRowSize( 7, 40 )
		self.m_grid31.SetRowSize( 8, 40 )
		self.m_grid31.SetRowSize( 9, 40 )
		self.m_grid31.EnableDragRowSize( True )
		self.m_grid31.SetRowLabelSize( 80 )
		self.m_grid31.SetRowLabelValue( 0, wx.EmptyString )
		self.m_grid31.SetRowLabelValue( 1, wx.EmptyString )
		self.m_grid31.SetRowLabelValue( 2, wx.EmptyString )
		self.m_grid31.SetRowLabelValue( 3, wx.EmptyString )
		self.m_grid31.SetRowLabelValue( 4, wx.EmptyString )
		self.m_grid31.SetRowLabelValue( 5, wx.EmptyString )
		self.m_grid31.SetRowLabelValue( 6, wx.EmptyString )
		self.m_grid31.SetRowLabelValue( 7, wx.EmptyString )
		self.m_grid31.SetRowLabelValue( 8, wx.EmptyString )
		self.m_grid31.SetRowLabelValue( 9, wx.EmptyString )
		self.m_grid31.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.m_grid31.SetLabelBackgroundColour( wx.Colour( 255, 255, 255 ) )

		# Cell Defaults
		self.m_grid31.SetDefaultCellBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_grid31.SetDefaultCellTextColour( wx.Colour( 255, 255, 255 ) )
		self.m_grid31.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		bSizer6.Add( self.m_grid31, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer6.Add( ( 0, 10), 0, wx.EXPAND, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText8 = wx.StaticText( self.m_panel41, wx.ID_ANY, u"ID Barang Yang Dikembalikan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 11, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Mongolian Baiti" ) )

		gSizer1.Add( self.m_staticText8, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		c_idbarang_dataChoices = []
		self.c_idbarang_data = wx.Choice( self.m_panel41, wx.ID_ANY, wx.DefaultPosition, wx.Size( 175,-1 ), c_idbarang_dataChoices, 0 )
		self.c_idbarang_data.SetSelection( 0 )
		gSizer1.Add( self.c_idbarang_data, 1, wx.ALL, 5 )


		gSizer1.Add( ( 0, 20), 0, wx.EXPAND, 5 )


		bSizer6.Add( gSizer1, 0, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.b_submit_data = wx.Button( self.m_panel41, wx.ID_ANY, u"SUBMIT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.b_submit_data.SetFont( wx.Font( 12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Mongolian Baiti" ) )
		self.b_submit_data.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.b_submit_data.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer10.Add( self.b_submit_data, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer6.Add( bSizer10, 1, wx.EXPAND, 5 )


		self.m_panel41.SetSizer( bSizer6 )
		self.m_panel41.Layout()
		bSizer6.Fit( self.m_panel41 )
		self.m_notebook1.AddPage( self.m_panel41, u"Data Peminjaman", False )

		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.b_submit_form.Bind( wx.EVT_BUTTON, self.submit_form )
		self.b_submit_data.Bind( wx.EVT_BUTTON, self.submit_data )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def submit_form( self, event ):
		event.Skip()

	def submit_data( self, event ):
		event.Skip()


###########################################################################
## Class Frame_Login
###########################################################################

class Frame_Login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 943,636 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 192, 192, 192 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )


		bSizer10.Add( ( 0, 50), 0, wx.EXPAND, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang di LA-Lens", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( 26, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Studio Brush DEMO" ) )

		bSizer10.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer10.Add( ( 0, 50), 0, wx.EXPAND, 5 )

		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		self.m_staticText23.SetFont( wx.Font( 16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Mongolian Baiti" ) )

		bSizer10.Add( self.m_staticText23, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer10.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.username_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer10.Add( self.username_input, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer10.Add( ( 0, 60), 0, wx.EXPAND, 5 )

		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		self.m_staticText24.SetFont( wx.Font( 16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Mongolian Baiti" ) )

		bSizer10.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer10.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.password_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer10.Add( self.password_input, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer10.Add( ( 0, 60), 0, wx.EXPAND, 5 )

		self.b_submit_login = wx.Button( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.b_submit_login.SetFont( wx.Font( 12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Mongolian Baiti" ) )
		self.b_submit_login.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.b_submit_login.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer10.Add( self.b_submit_login, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer9.Add( bSizer10, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.b_submit_login.Bind( wx.EVT_BUTTON, self.submit_login )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def submit_login( self, event ):
		event.Skip()


