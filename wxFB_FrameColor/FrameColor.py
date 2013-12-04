# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2013)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Hyena Quality Guard", pos = wx.DefaultPosition, size = wx.Size( 800,450 ), style = wx.DEFAULT_FRAME_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 12, 74, 90, 92, False, "Verdana" ) )
		self.SetForegroundColour( wx.Colour( 219, 238, 244 ) )
		self.SetBackgroundColour( wx.Colour( 219, 238, 244 ) )
		
		m_Sizer_MainFrame = wx.BoxSizer( wx.VERTICAL )
		
		self.m_NoteBook_MainFrame = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_NoteBook_MainFrame.SetFont( wx.Font( 12, 71, 90, 92, False, "Verdana" ) )
		self.m_NoteBook_MainFrame.SetForegroundColour( wx.Colour( 219, 238, 244 ) )
		self.m_NoteBook_MainFrame.SetBackgroundColour( wx.Colour( 219, 238, 244 ) )
		
		self.m_panel_SWUpgrade = wx.Panel( self.m_NoteBook_MainFrame, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_SWUpgrade.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel8 = wx.Panel( self.m_panel_SWUpgrade, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel10 = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 4, 2, 0, 0 )
		
		self.m_st_Customer = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Customer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_st_Customer.Wrap( -1 )
		self.m_st_Customer.SetFont( wx.Font( 12, 74, 90, 90, True, wx.EmptyString ) )
		self.m_st_Customer.SetForegroundColour( wx.Colour( 47, 133, 158 ) )
		
		gSizer1.Add( self.m_st_Customer, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_tc_Customer = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_tc_Customer.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gSizer1.Add( self.m_tc_Customer, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_st_Date = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_st_Date.Wrap( -1 )
		self.m_st_Date.SetFont( wx.Font( 12, 74, 90, 90, True, wx.EmptyString ) )
		self.m_st_Date.SetForegroundColour( wx.Colour( 47, 133, 158 ) )
		
		gSizer1.Add( self.m_st_Date, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_tc_Date = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_tc_Date.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gSizer1.Add( self.m_tc_Date, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_st_LastChange = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Last Change", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_st_LastChange.Wrap( -1 )
		self.m_st_LastChange.SetFont( wx.Font( 12, 74, 90, 90, True, wx.EmptyString ) )
		self.m_st_LastChange.SetForegroundColour( wx.Colour( 47, 133, 158 ) )
		
		gSizer1.Add( self.m_st_LastChange, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_tc_LastChange = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_tc_LastChange.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gSizer1.Add( self.m_tc_LastChange, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_st_SystemModel = wx.StaticText( self.m_panel10, wx.ID_ANY, u"System Model", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_st_SystemModel.Wrap( -1 )
		self.m_st_SystemModel.SetFont( wx.Font( 12, 74, 90, 90, True, wx.EmptyString ) )
		self.m_st_SystemModel.SetForegroundColour( wx.Colour( 47, 133, 158 ) )
		
		gSizer1.Add( self.m_st_SystemModel, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_tc_SystemModel = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_tc_SystemModel.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gSizer1.Add( self.m_tc_SystemModel, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel10.SetSizer( gSizer1 )
		self.m_panel10.Layout()
		gSizer1.Fit( self.m_panel10 )
		bSizer6.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel11 = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel8.SetSizer( bSizer6 )
		self.m_panel8.Layout()
		bSizer6.Fit( self.m_panel8 )
		bSizer2.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel9 = wx.Panel( self.m_panel_SWUpgrade, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel_SWUpgrade.SetSizer( bSizer2 )
		self.m_panel_SWUpgrade.Layout()
		bSizer2.Fit( self.m_panel_SWUpgrade )
		self.m_NoteBook_MainFrame.AddPage( self.m_panel_SWUpgrade, u"SW Upgrade", False )
		self.m_panel_Customize = wx.Panel( self.m_NoteBook_MainFrame, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_NoteBook_MainFrame.AddPage( self.m_panel_Customize, u"Customize", False )
		self.m_panel_Diagnosis = wx.Panel( self.m_NoteBook_MainFrame, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_NoteBook_MainFrame.AddPage( self.m_panel_Diagnosis, u"Diagnosis", False )
		self.m_panel_FAQ = wx.Panel( self.m_NoteBook_MainFrame, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_NoteBook_MainFrame.AddPage( self.m_panel_FAQ, u"FAQ", False )
		
		m_Sizer_MainFrame.Add( self.m_NoteBook_MainFrame, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( m_Sizer_MainFrame )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

