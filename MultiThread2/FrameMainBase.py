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
## Class Main
###########################################################################

class Main ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_btn_Run = wx.Button( self, wx.ID_ANY, u"&Run", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_btn_Run, 0, wx.ALL, 5 )
		
		self.m_btn_Break = wx.Button( self, wx.ID_ANY, u"&Break", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_btn_Break, 0, wx.ALL, 5 )
		
		self.m_btn_Stop = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_btn_Stop, 0, wx.ALL, 5 )
		
		self.m_staticText = wx.StaticText( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText.Wrap( -1 )
		bSizer1.Add( self.m_staticText, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnCloseWindow )
		self.m_btn_Run.Bind( wx.EVT_BUTTON, self.OnBtnRun_Click )
		self.m_btn_Break.Bind( wx.EVT_BUTTON, self.OnBtnBreak_Click )
		self.m_btn_Stop.Bind( wx.EVT_BUTTON, self.OnBtnStop_Click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnCloseWindow( self, event ):
		event.Skip()
	
	def OnBtnRun_Click( self, event ):
		event.Skip()
	
	def OnBtnBreak_Click( self, event ):
		event.Skip()
	
	def OnBtnStop_Click( self, event ):
		event.Skip()
	

