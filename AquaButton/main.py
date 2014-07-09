# -*- coding: utf-8 -*-
import wx
import wx.lib.agw.aquabutton as AB
from Preference_Urban import *
ColorList = ["BackgroundColour",
             "DisabledColour",
             "ForegroundColour",
             "ShadowColour",
             "HoverColour",
             "GraidentColour",
             "RectColour"]
class MyAquaButton(AB.AquaButton):
    def __init__(self, *args, **kwargs ):
        AB.AquaButton.__init__(self,*args, **kwargs)
        self._gradientColour = wx.WHITE
    def GetGraidentColour(self):
        return self._gradientColour
    def SetGraidentColour(self,colour):
        self._gradientColour = colour
        self.Invalidate()
    def OnPaint(self, event):
        """
        Handles the ``wx.EVT_PAINT`` event for :class:`AquaButton`.

        :param `event`: a :class:`PaintEvent` event to be processed.
        """

        dc = wx.BufferedPaintDC(self)
        gc = wx.GraphicsContext.Create(dc)

        xpos, ypos, width, height = self.GetClientRect()
         
        dc.SetBackground(wx.Brush(self._rectColour))
        dc.Clear()
        gc.SetBrush(wx.WHITE_BRUSH)

        shadowOffset = 5
        btnOffset = 0
        clr = self._backColour

        if self._mouseAction == AB.CLICK:
            shadowOffset = 3
            clr = self._hoverColour
            btnOffset = 2

        elif self._mouseAction == AB.HOVER:
            clr = self._hoverColour
            
        elif not self.IsEnabled():
            clr = self._disableColour

        rc1 = wx.Rect(btnOffset, btnOffset, width-8-btnOffset, height-8-btnOffset)        
        path1 = self.GetPath(gc, rc1, 10)
        br1 = gc.CreateLinearGradientBrush(0, 0, 0, rc1.height+6, clr, self._gradientColour)

        # Create shadow
        rc2 = wx.Rect(*rc1)
        rc2.Offset((shadowOffset, shadowOffset))
        path2 = self.GetPath(gc, rc2, 10)
        br2 = gc.CreateRadialGradientBrush(rc2.x, rc2.y,
                                           rc2.x+rc2.width, rc2.y+rc2.height,
                                           rc2.width, self._shadowColour, self._gradientColour)

        # Create top water colour to give "aqua" effect
        rc3 = wx.Rect(*rc1)
        rc3.Inflate(-5, -5)
        rc3.height = 15
        path3 = self.GetPath(gc, rc3, 10)
        r,g,b = self._gradientColour.Get()
        br3 = gc.CreateLinearGradientBrush(rc3.x, rc3.y, rc3.x, rc3.y+rc3.height,
                                           wx.Colour(r, g, b, 255), wx.Colour(r, g, b, 0))

        # draw shapes
        gc.SetBrush(br2)
        gc.FillPath(path2)  #draw shadow
        gc.SetBrush(br1)
        gc.FillPath(path1) #draw main
        gc.SetBrush(br3)
        gc.FillPath(path3) #draw top bubble

        font = gc.CreateFont(self.GetFont(), self._textColour)

        gc.SetFont(font)
        label = self.GetLabel()
        if not label:
            tw = 0
            th = 0
        else:
            tw, th = gc.GetTextExtent(label)

        if self._bitmap:
            bw, bh = self._bitmap.GetWidth(), self._bitmap.GetHeight()
        else:
            bw = bh = 0

        '''
        pos_x = (width-bw-tw)/2+btnOffset-shadowOffset      # adjust for bitmap and text to centre
        if self._bitmap:
            pos_y =  (height-bh-shadowOffset)/2+btnOffset
            gc.DrawBitmap(self._bitmap, pos_x, pos_y, bw, bh) # draw bitmap if available
            pos_x = pos_x + 2   # extra spacing from bitmap
        print pos_x,pos_y
        # Create a Path to draw the text
        gc.DrawText(label, pos_x + bw + btnOffset, (height-th-shadowOffset)/2+btnOffset)      # draw the text
        '''
        pos_y = (height-bh-th)/2+btnOffset-shadowOffset      # adjust for bitmap and text to centre
        if self._bitmap:
            pos_x =  (width-bw-shadowOffset)/2+btnOffset
            gc.DrawBitmap(self._bitmap, pos_x, pos_y, bw, bh) # draw bitmap if available
            pos_y = pos_y + 2   # extra spacing from bitmap
        
        # Create a Path to draw the text
        #dc.DrawLine((width-tw-shadowOffset)/2+btnOffset, pos_y + bw + btnOffset,(width-tw-shadowOffset)/2+btnOffset+tw, pos_y + bw + btnOffset)
        if label:
            gc.DrawText(label, (width-tw-shadowOffset)/2+btnOffset, pos_y + bw + btnOffset)      # draw the text
        #'''
        if self._saveBitmap:
            # Save the bitmap using wx.MemoryDC for later use
            self._saveBitmap = False
            memory = wx.MemoryDC()
            self._storedBitmap = wx.EmptyBitmapRGBA(max(width, 1), max(height, 1))
            memory.SelectObject(self._storedBitmap)

            gcMemory = wx.GraphicsContext.Create(memory)

            gcMemory.SetBrush(br1)
            gcMemory.FillPath(path1) #draw main
            gcMemory.SetBrush(br3)
            gcMemory.FillPath(path3) #draw top bubble

            if self._bitmap:
                gcMemory.DrawBitmap(self._bitmap, pos_x - 2, pos_y, bw, bh)

            gcMemory.SetFont(font)
            #gcMemory.DrawText(label, pos_x + bw + btnOffset, (height-th-shadowOffset)/2+btnOffset)
            if label:
                gcMemory.DrawText(label, (width-tw-shadowOffset)/2+btnOffset, pos_y + bw + btnOffset)

            memory.SelectObject(wx.NullBitmap)
            self._storedBitmap = self._storedBitmap.ConvertToImage()
    def DoGetBestSize(self):
        """
        Overridden base class virtual. Determines the best size of the
        button based on the label and bezel size.

        :return: An instance of :class:`Size`.
        
        :note: Overridden from :class:`PyControl`.
        """

        label = self.GetLabel()
        #if not label:
        #    return wx.Size(112, 48)

        dc = wx.ClientDC(self)
        dc.SetFont(self.GetFont())
        if not label:
            retWidth  = 0 
            retHeight = 0
        else:
            retWidth, retHeight = dc.GetTextExtent(label)
        
        bmpWidth = bmpHeight = 0
        constant = 24
        if self._bitmap:
            '''
            bmpWidth, bmpHeight = self._bitmap.GetWidth()+10, self._bitmap.GetHeight()
            retWidth += bmpWidth
            retHeight = max(bmpHeight, retHeight)
            '''
            bmpWidth, bmpHeight = self._bitmap.GetWidth()+10, self._bitmap.GetHeight()
            retWidth   = max(bmpWidth, retWidth)
            retHeight += bmpHeight
            #'''
            constant = 24

        return wx.Size(retWidth+constant, retHeight+constant)
            
class MyFrame ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "AquaButton Attribute Setting", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        ft = self.GetFont()
        ft.SetPointSize(12)
        ft.SetFaceName(u"Eras Medium ITC")
        self.SetFont(ft)        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour(wx.WHITE)
        gbSizer = wx.GridBagSizer( 0, 0 )
        gbSizer.SetFlexibleDirection( wx.BOTH )
        gbSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        self.btn1 = MyAquaButton(self, wx.ID_ANY, Preference_Urban.GetBitmap(), "AquaButton")
        self.btn1.SetForegroundColour(wx.BLACK)        
        h=0
        self.m_ButtonText = wx.TextCtrl( self, wx.ID_ANY, self.btn1.GetLabel(), wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        gbSizer.Add( wx.StaticText( self, wx.ID_ANY, "Button Label"), wx.GBPosition( h, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        gbSizer.Add( self.m_ButtonText                              , wx.GBPosition( h, 2 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
        h +=1
        for attr in ColorList:
            setattr(self, "m_"+attr, wx.ColourPickerCtrl(self , col=getattr(self.btn1,"Get"+attr)()))
            gbSizer.Add( wx.StaticText( self, wx.ID_ANY, attr), wx.GBPosition( h, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
            gbSizer.Add( getattr(self,"m_"+attr)              , wx.GBPosition( h, 2 ), wx.GBSpan( 1, 1 ), wx.ALL | wx.ALIGN_RIGHT, 5 )
            gbSizer.Add( wx.StaticText( self, wx.ID_ANY, getattr(self.btn1,"Get"+attr)().GetAsString(wx.C2S_HTML_SYNTAX)), wx.GBPosition( h, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER, 5 )
            h += 1
        self.m_cbPulseOnFocus = wx.CheckBox(self, wx.ID_ANY, "Pulse On Press")
        gbSizer.Add( self.m_cbPulseOnFocus, wx.GBPosition( h, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_LEFT, 5 )
        h += 1
        self.m_cbDisable = wx.CheckBox(self, wx.ID_ANY, "Disable Button")
        gbSizer.Add( self.m_cbDisable, wx.GBPosition( h, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_LEFT, 5 )
        h += 1
        self.m_PointSize = wx.ComboBox( self, choices = ["8","9","10","11","12","14","16","18","20","22","24","26","28","36","48","72"],style = wx.TE_PROCESS_ENTER )
        gbSizer.Add( wx.StaticText( self, wx.ID_ANY, "PointSize"), wx.GBPosition( h, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        gbSizer.Add( self.m_PointSize                            , wx.GBPosition( h, 2 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
        self.m_PointSize.SetValue(str(self.btn1.GetFont().GetPointSize()))
        h += 1
        e = wx.FontEnumerator()
        e.EnumerateFacenames()
        flist = e.GetFacenames()
        flist.sort()
        self.m_FaceName = wx.ComboBox( self, choices = flist,style = wx.TE_PROCESS_ENTER)
        gbSizer.Add( wx.StaticText( self, wx.ID_ANY, "FaceName"), wx.GBPosition( h, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        gbSizer.Add( self.m_FaceName                            , wx.GBPosition( h, 2 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER, 5 )
        self.m_FaceName.SetValue(str(self.btn1.GetFont().GetFaceName()))
        h += 1
        
        gbSizer.Add( self.btn1, wx.GBPosition( 0, 0 ), wx.GBSpan( h, 1 ), wx.ALL|wx.ALIGN_CENTER, 5 )
        self.SetSizer( gbSizer )
        self.Layout()
        self.SetClientSize(self.GetEffectiveMinSize())
        self.Centre( wx.BOTH )
        self.Bind(wx.EVT_COLOURPICKER_CHANGED, self.OnPickColour)
        self.Bind(wx.EVT_CHECKBOX    , self.OnCheck)
        self.m_PointSize.Bind(wx.EVT_COMBOBOX    , self.OnChoice)
        self.m_PointSize.Bind(wx.EVT_TEXT_ENTER  , self.OnChoice)
        self.m_FaceName.Bind(wx.EVT_COMBOBOX    , self.OnChoice)
        self.m_FaceName.Bind(wx.EVT_TEXT_ENTER  , self.OnChoice)
        self.m_ButtonText.Bind( wx.EVT_TEXT, self.OnText )
        self.OnCheck(None)
    def OnPickColour(self, event):
        for attr in ColorList:
            if(getattr(self,"m_"+attr)==event.GetEventObject()):
                getattr(self.btn1,"Set"+attr)(event.GetColour())
    def OnCheck(self, event):
        self.btn1.SetPulseOnFocus(self.m_cbPulseOnFocus.IsChecked())
        self.btn1.Enable(not self.m_cbDisable.IsChecked())
    def OnChoice(self, event):
        ft = self.btn1.GetFont()
        ft.SetPointSize(int(self.m_PointSize.GetValue()))
        ft.SetFaceName(self.m_FaceName.GetValue())
        self.btn1.SetFont(ft)
        self.btn1.Refresh()
        self.Layout()
        self.SetClientSize(self.GetEffectiveMinSize())
    def OnText(self, event):
        self.btn1.SetLabel(self.m_ButtonText.GetValue())
        self.btn1.Refresh()
        self.Layout()
        self.SetClientSize(self.GetEffectiveMinSize())
if __name__=='__main__':
    #'''
    app = wx.App()
    my_frame = MyFrame(None)
    my_frame.Center()
    my_frame.Show()
    app.MainLoop()
    '''    
    for mstr in dir(AB.AquaButton):
        if(((mstr.find("Colour")>=0) or (mstr.find("Color")>=0) )and ((mstr.find("Set")>=0) or (mstr.find("Get")>=0) )):
            print mstr
    #'''