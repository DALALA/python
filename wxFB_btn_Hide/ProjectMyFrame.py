"""Subclass of MyFrame, which is generated by wxFormBuilder."""

import wx
import MainFrame

# Implementing MyFrame
class ProjectMyFrame( MainFrame.MyFrame ):
	def __init__( self, parent ):
		MainFrame.MyFrame.__init__( self, parent )
		self.m_btn_Hide.Hide()
	
if __name__=='__main__':
    app = wx.App()
    my_frame = ProjectMyFrame(None)
    my_frame.Show()
    app.MainLoop()