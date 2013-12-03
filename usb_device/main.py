'''
Created on 2013/9/30

@author: RobertChen
'''
import fetch_setting
from fetch_setting import *

GUID_DEVCLASS_PORT            = GUID(0x4D36E978, 0xE325, 0x11CE, (BYTE*8)(-0x41, -0x3F, 0x08, 0x00, 0x2B, -0x1F, 0x03, 0x18))
GUID_DEVINTERFACE_USB_DEVICE  = GUID(0xA5DCBF10, 0x6530, 0x11D2, (BYTE*8)(0x90, 0x1F, 0x00, 0xC0, 0x4F, 0xB9, 0x51, 0xED))
GUID_DEVINTERFACE_COMPORT     = GUID(0x86E0D1E0, 0x8089, 0x11D0, (BYTE*8)(0x9C, 0xE4, 0x08, 0x00, 0x3E, 0x30, 0x1F, 0x73))

if __name__ == "__main__":
    usb_device = Hyena_USB_Device(GUID_DEVINTERFACE_COMPORT,GUID_DEVCLASS_PORT)
    #usb_device = Hyena_USB_Device(GUID_DEVINTERFACE_USB_DEVICE,GUID_DEVCLASS_PORT)
    usb_device.GetDeviceInfoAndInterface()
    usb_device.GetHidInfo()
    usb_device.CleanUp()
