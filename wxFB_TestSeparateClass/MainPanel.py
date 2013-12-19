"""Subclass of MainPanel, which is generated by wxFormBuilder."""

import wx
import FrameBase

# Implementing MainPanel
class MainPanel( FrameBase.MainPanel ):
	def __init__( self, parent ):
		FrameBase.MainPanel.__init__( self, parent )
		self._parent = parent
	
	# Handlers for MainPanel events.
	def OnBtnClick_Close( self, event ):
		# TODO: Implement OnBtnClick_Close
		self._parent.Destroy()
		pass
	
	