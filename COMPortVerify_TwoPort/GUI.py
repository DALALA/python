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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"COM Port Verify", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		bSizer_Port1 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_choice_Port1Choices = []
		self.m_choice_Port1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_Port1Choices, 0 )
		self.m_choice_Port1.SetSelection( 0 )
		bSizer_Port1.Add( self.m_choice_Port1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_st_Port1SendTitle = wx.StaticText( self, wx.ID_ANY, u"傳送:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_st_Port1SendTitle.Wrap( -1 )
		bSizer_Port1.Add( self.m_st_Port1SendTitle, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_st_Port1Send = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_st_Port1Send.Wrap( -1 )
		bSizer_Port1.Add( self.m_st_Port1Send, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_st_Port1RecvTitle = wx.StaticText( self, wx.ID_ANY, u"接收:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_st_Port1RecvTitle.Wrap( -1 )
		bSizer_Port1.Add( self.m_st_Port1RecvTitle, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_st_Port1Recv = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_st_Port1Recv.Wrap( -1 )
		bSizer_Port1.Add( self.m_st_Port1Recv, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_st_Port1ErrTitle = wx.StaticText( self, wx.ID_ANY, u"錯誤:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_st_Port1ErrTitle.Wrap( -1 )
		bSizer_Port1.Add( self.m_st_Port1ErrTitle, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_st_Port1Err = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_st_Port1Err.Wrap( -1 )
		bSizer_Port1.Add( self.m_st_Port1Err, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer.Add( bSizer_Port1, 0, wx.EXPAND, 5 )
		
		bSizer_Port2 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_choice_Port2Choices = []
		self.m_choice_Port2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_Port2Choices, 0 )
		self.m_choice_Port2.SetSelection( 0 )
		bSizer_Port2.Add( self.m_choice_Port2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_st_Port2SendTitle = wx.StaticText( self, wx.ID_ANY, u"傳送:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_st_Port2SendTitle.Wrap( -1 )
		bSizer_Port2.Add( self.m_st_Port2SendTitle, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_st_Port2Send = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_st_Port2Send.Wrap( -1 )
		bSizer_Port2.Add( self.m_st_Port2Send, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_st_Port2RecvTitle = wx.StaticText( self, wx.ID_ANY, u"接收:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_st_Port2RecvTitle.Wrap( -1 )
		bSizer_Port2.Add( self.m_st_Port2RecvTitle, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_st_Port2Recv = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_st_Port2Recv.Wrap( -1 )
		bSizer_Port2.Add( self.m_st_Port2Recv, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_st_Port2ErrTitle = wx.StaticText( self, wx.ID_ANY, u"錯誤:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_st_Port2ErrTitle.Wrap( -1 )
		bSizer_Port2.Add( self.m_st_Port2ErrTitle, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_st_Port2Err = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_st_Port2Err.Wrap( -1 )
		bSizer_Port2.Add( self.m_st_Port2Err, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer.Add( bSizer_Port2, 0, wx.EXPAND, 5 )
		
		bSizer_Ctrl = wx.BoxSizer( wx.VERTICAL )
		
		bSizerLen = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_st_xferLen = wx.StaticText( self, wx.ID_ANY, u"傳送長度(B)", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_st_xferLen.Wrap( -1 )
		bSizerLen.Add( self.m_st_xferLen, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_spinCtrlLen = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 256, 32 )
		bSizerLen.Add( self.m_spinCtrlLen, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer_Ctrl.Add( bSizerLen, 1, wx.EXPAND, 5 )
		
		bSizerDelay = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_st_xferTime = wx.StaticText( self, wx.ID_ANY, u"傳送延遲(ms)", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_st_xferTime.Wrap( -1 )
		bSizerDelay.Add( self.m_st_xferTime, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_spinCtrlTime = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 100, 5000, 500 )
		bSizerDelay.Add( self.m_spinCtrlTime, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer_Ctrl.Add( bSizerDelay, 1, wx.EXPAND, 5 )
		
		
		bSizer.Add( bSizer_Ctrl, 0, wx.EXPAND, 5 )
		
		bSizer_btn = wx.BoxSizer( wx.VERTICAL )
		
		self.m_btn_Exe = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_btn_Exe.SetDefault() 
		bSizer_btn.Add( self.m_btn_Exe, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer.Add( bSizer_btn, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer )
		self.Layout()
		bSizer.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_SIZE, self.OnSize )
		self.m_choice_Port1.Bind( wx.EVT_CHOICE, self.OnChoicePort )
		self.m_choice_Port2.Bind( wx.EVT_CHOICE, self.OnChoicePort )
		self.m_btn_Exe.Bind( wx.EVT_BUTTON, self.OnBtnClickExe )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSize( self, event ):
		event.Skip()
	
	def OnChoicePort( self, event ):
		event.Skip()
	
	
	def OnBtnClickExe( self, event ):
		event.Skip()
	

