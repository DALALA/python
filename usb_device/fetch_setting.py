'''
Created on 2013/10/2

@author: DALALA
'''
import struct
import HidClass_Support_func
from HidClass_Support_func import *
import Dev_Install_func
from Dev_Install_func import *

class Hyena_USB_Device(object):
    def __init__(self,interface_guid,class_guid):
        """
        try to find the interface_guid and class_guid match device
        """
        print("Hyena_USB_Device:__init__")
        self.interface_guid                   = interface_guid
        self.class_guid                       = class_guid
        self.DeviceInfoSet                    = INVALID_HANDLE_VALUE
        self.DeviceInfoData                   = SP_DEVINFO_DATA()
        self.DeviceInfoData.cbSize            = sizeof(SP_DEVINFO_DATA)
        self.DeviceInterfaceData              = SP_DEVICE_INTERFACE_DATA()
        self.DeviceInterfaceData.cbSize       = sizeof(SP_DEVICE_INTERFACE_DATA)
        self.DeviceInterfaceDetailData        = SP_DEVICE_INTERFACE_DETAIL_DATA()
        self.DeviceInterfaceDetailData.cbSize = sizeof(SP_DEVICE_INTERFACE_DETAIL_DATA)
        self.parent_device_handle             = c_ulong()
        self.DeviceInstanceId                 = None
        self.hidd_attributes                  = HIDD_ATTRIBUTES()
        self.hidd_attributes.Size             = sizeof(HIDD_ATTRIBUTES)
        
    def __enter__(self):
        print "Hyena_USB_Device:__enter__"
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print "Hyena_USB_Device:__exit__" 
        self._DestroyDeviceInfoList()
    '''
    def __str__(self):
        return "Hyena_USB_Device paramter:\n\
     interface_guid:%s\n\
     class_guid:%s\n\
     DeviceInfoSet:%d\n\
     %s\n\
     %s\n\
     parent_device_handle:0x%x" % (
              self.interface_guid,
              self.class_guid,
              self.DeviceInfoSet,
              self.DeviceInfoData,
              self.DeviceInterfaceDetailData,
              self.parent_device_handle.value
              )
    '''
    def ShowLastErrorMsg(self):
        print ctypes.WinError(ctypes.GetLastError()) 

    def _GetDeviceInfoSet(self):
        """ 
        Gets a handle to a device information set that contains requested device information elements for a local computer
        Input:  self.interface_guid
        Output: self.DeviceInfoSet
        """
        self.DeviceInfoSet = SetupDiGetClassDevs(byref(self.interface_guid), None, None,  DIGCF_DEVICEINTERFACE|DIGCF_PROFILE|DIGCF_PRESENT)
        if self.DeviceInfoSet == INVALID_HANDLE_VALUE:
            self.ShowLastErrorMsg()
        print "_GetDeviceInfoSet:0x%x" % self.DeviceInfoSet 
        
    def _DestroyDeviceInfoList(self):
        """
        Deletes a device information set and frees all associated memory
        Input: self.DeviceInfoSet
        Output: None
        """
        print "_DestroyDeviceInfoList" 
        if self.DeviceInfoSet and self.DeviceInfoSet!= INVALID_HANDLE_VALUE:
            if not SetupDiDestroyDeviceInfoList(self.DeviceInfoSet):
                self.ShowLastErrorMsg()
            return
        self.DeviceInfoSet = INVALID_HANDLE_VALUE; 

    def _GetDeviceInfoData(self):
        """
        Gets a SP_DEVINFO_DATA structure that specifies a device information element in a device information set
        Here I Use class_guid to filter the list , and take first one As the expect
        ToDo : the filter is ok?
        Input:self.DeviceInfoSet
        Output:self.DeviceInfoData
        """
        FindDevice = False
        MemberIndex = 0
        while SetupDiEnumDeviceInfo(self.DeviceInfoSet,MemberIndex,byref(self.DeviceInfoData)) and not FindDevice:
            #print("index:%d,%s" % (MemberIndex , self.DeviceInfoData))            
            MemberIndex+=1
            if(self.DeviceInfoData.ClassGuid == self.class_guid):
                print "_GetDeviceInfoData:" , self.DeviceInfoData
                FindDevice = True
                break
        if not MemberIndex and not FindDevice:
            self.ShowLastErrorMsg()
    
    def _GetDeviceInterfaceData(self):
        """
        Enumerates the device interfaces that are contained in a device information set
        TODO: I take the first one as the expect , Is it OK?(filtered by self.DeviceInfoData)
        Input:self.DeviceInfoSet , self.DeviceInfoData
        Output:self.DeviceInterfaceData
        """
        FindDevice = False
        MemberIndex = 0
        while SetupDiEnumDeviceInterfaces(self.DeviceInfoSet,byref(self.DeviceInfoData),byref(self.interface_guid),MemberIndex,byref(self.DeviceInterfaceData)) and not FindDevice:
            #print "idx:%d,%s" %(MemberIndex,self.DeviceInterfaceData.InterfaceClassGuid) 
            MemberIndex += 1
            print "_GetDeviceInterfaceData:", self.DeviceInterfaceData 
            FindDevice = True
            break
        
        if not MemberIndex and not FindDevice:
            self.ShowLastErrorMsg() 
     
    def _GetDeviceInterfaceDetail(self):
        """
        Gets details about a device interface
        First Calling to get the actually size of output
        Input:self.DeviceInfoSet,self.DeviceInterfaceData
        Output:self.DeviceInterfaceDetailData
        """
        required_size = DWORD(0)
        SetupDiGetDeviceInterfaceDetail(self.DeviceInfoSet, byref(self.DeviceInterfaceData), 
                                        None, 0, byref(required_size), None)
        ctypes.resize(self.DeviceInterfaceDetailData, required_size.value)
        if not SetupDiGetDeviceInterfaceDetail(self.DeviceInfoSet, byref(self.DeviceInterfaceData), 
                                        byref(self.DeviceInterfaceDetailData), required_size, None,None):
            self.ShowLastErrorMsg()
        print "_GetDeviceInterfaceDetail:", self.DeviceInterfaceDetailData 

    def _GetParentDeviceHandle(self):
        """
        Get Parent Device Handle, it may be none(0)
        Input:self.DeviceInfoData.DevInst
        Output:self.parent_device_handle
        """
        if not ctypes.windll.setupapi.CM_Get_Parent(byref(self.parent_device_handle),self.DeviceInfoData.DevInst, 0):
                self.parent_device_handle.value = 0
        print "_GetParentDeviceHandle:0x%x" % self.parent_device_handle.value 

    def _GetDeviceInstanceId(self):
        """
        Retrieves the device instance ID that is associated with a device information element.
        First Calling to get the actually size of output
        Input:self.DeviceInfoSet,self.DeviceInfoData
        Output:self.DeviceInstanceId
        """
        required_size = DWORD(0)
        SetupDiGetDeviceInstanceId(self.DeviceInfoSet, byref(self.DeviceInfoData),
                    None, 0, byref(required_size) )
        self.DeviceInstanceId = create_unicode_buffer(required_size.value)
        if required_size.value > 0:
            SetupDiGetDeviceInstanceId(self.DeviceInfoSet, byref(self.DeviceInfoData),
                        self.DeviceInstanceId, required_size, byref(required_size))
        print "_GetDeviceInstanceId:" , bytearray(self.DeviceInstanceId).decode('utf-16le') 

    def _GetDeviceRegistryProperty(self,Property=SPDRP_DEVICEDESC):
        """
        Retrieves a specified Plug and Play device property.
        First Calling to get the actually size of output
        Input:self.DeviceInfoSet,self.DeviceInfoData,Property
        Output:PropertyBuffer
        """
        required_size = DWORD(0)
        PropertyRegDataType = DWORD(0)
        SetupDiGetDeviceRegistryProperty(self.DeviceInfoSet,
                                         byref(self.DeviceInfoData),
                                         Property,
                                         byref(PropertyRegDataType),
                                         None,
                                         0,
                                         byref(required_size))
        if not required_size.value:
            return
        PropertyBuffer = (BYTE*required_size.value)()
        if not SetupDiGetDeviceRegistryProperty(self.DeviceInfoSet,
                                                byref(self.DeviceInfoData),
                                                Property,
                                                byref(PropertyRegDataType),
                                                PropertyBuffer,
                                                required_size.value,
                                                byref(required_size)):
            self.ShowLastErrorMsg()
        message = "_GetDeviceRegistryProperty(%2d=%-33s):%d=%-13s:" % (Property,
                                                                    list_SPDRP_Property[Property],
                                                                    PropertyRegDataType.value,
                                                                    list_RegType[PropertyRegDataType.value]
                                                                   )
        if PropertyRegDataType.value==1 or PropertyRegDataType.value==7:
            message += "%s" % bytearray(PropertyBuffer).decode('utf-16le')
        elif PropertyRegDataType.value==4 or PropertyRegDataType.value==0:
            swap_PropertyBuffer = struct.unpack("I",(BYTE*required_size.value)(PropertyBuffer[0],PropertyBuffer[1],PropertyBuffer[2],PropertyBuffer[3]))[0]
            message += "0x%x" % swap_PropertyBuffer
            if Property==SPDRP_CAPABILITIES :
                message += "(%s)" % Parse_CM_DEVCAP(swap_PropertyBuffer)
        elif PropertyRegDataType.value==3:
            message += "CM_POWER_DATA"
        else:
            message += "unknown PropertyRegDataType"
        print message
        
    def GetDeviceInfoAndInterface(self):
        self._GetDeviceInfoSet()
        self._GetDeviceInfoData()
        self._GetDeviceInterfaceData()
        self._GetDeviceInterfaceDetail()
        self._GetParentDeviceHandle()
        self._GetDeviceInstanceId()
        
        self._GetDeviceRegistryProperty(SPDRP_DEVICEDESC)
        self._GetDeviceRegistryProperty(SPDRP_HARDWAREID)
        self._GetDeviceRegistryProperty(SPDRP_COMPATIBLEIDS)
        self._GetDeviceRegistryProperty(SPDRP_SERVICE)
        self._GetDeviceRegistryProperty(SPDRP_CLASS)
        self._GetDeviceRegistryProperty(SPDRP_CLASSGUID)
        self._GetDeviceRegistryProperty(SPDRP_DRIVER)
        self._GetDeviceRegistryProperty(SPDRP_CONFIGFLAGS)
        self._GetDeviceRegistryProperty(SPDRP_MFG)
        self._GetDeviceRegistryProperty(SPDRP_FRIENDLYNAME)
        self._GetDeviceRegistryProperty(SPDRP_LOCATION_INFORMATION)
        self._GetDeviceRegistryProperty(SPDRP_PHYSICAL_DEVICE_OBJECT_NAME)
        self._GetDeviceRegistryProperty(SPDRP_CAPABILITIES)
        self._GetDeviceRegistryProperty(SPDRP_UI_NUMBER)
        self._GetDeviceRegistryProperty(SPDRP_UPPERFILTERS)
        self._GetDeviceRegistryProperty(SPDRP_LOWERFILTERS)
        self._GetDeviceRegistryProperty(SPDRP_BUSTYPEGUID)
        self._GetDeviceRegistryProperty(SPDRP_LEGACYBUSTYPE)
        self._GetDeviceRegistryProperty(SPDRP_BUSNUMBER)
        self._GetDeviceRegistryProperty(SPDRP_ENUMERATOR_NAME)
        self._GetDeviceRegistryProperty(SPDRP_SECURITY)
        self._GetDeviceRegistryProperty(SPDRP_SECURITY_SDS)
        self._GetDeviceRegistryProperty(SPDRP_DEVTYPE)
        self._GetDeviceRegistryProperty(SPDRP_EXCLUSIVE)
        self._GetDeviceRegistryProperty(SPDRP_CHARACTERISTICS)
        self._GetDeviceRegistryProperty(SPDRP_ADDRESS)
        self._GetDeviceRegistryProperty(SPDRP_UI_NUMBER_DESC_FORMAT)
        self._GetDeviceRegistryProperty(SPDRP_DEVICE_POWER_DATA)
        self._GetDeviceRegistryProperty(SPDRP_REMOVAL_POLICY)
        self._GetDeviceRegistryProperty(SPDRP_REMOVAL_POLICY_HW_DEFAULT)
        self._GetDeviceRegistryProperty(SPDRP_REMOVAL_POLICY_OVERRIDE)
        self._GetDeviceRegistryProperty(SPDRP_INSTALL_STATE)
        self._GetDeviceRegistryProperty(SPDRP_LOCATION_PATHS)
        self._GetDeviceRegistryProperty(SPDRP_BASE_CONTAINERID)
    
    def CleanUp(self):
        self._DestroyDeviceInfoList()
        
    def GetHidInfo(self):
        print ctypes.wstring_at(byref(self.DeviceInterfaceDetailData,sizeof(DWORD))) 
        h_hid_device = CreateFile(ctypes.wstring_at(byref(self.DeviceInterfaceDetailData,sizeof(DWORD))), 
                                  GENERIC_READ | GENERIC_WRITE,
                                  FILE_SHARE_READ | FILE_SHARE_WRITE, 
                                  None, 
                                  OPEN_EXISTING, 
                                  FILE_ATTRIBUTE_NORMAL | FILE_FLAG_OVERLAPPED, 
                                  0)
        if h_hid_device == INVALID_HANDLE_VALUE:
            self.ShowLastErrorMsg()
            return
        print "CreateFile return 0x%x" % h_hid_device 
        if not HidD_GetAttributes(h_hid_device, byref(self.hidd_attributes)):
            print self.hidd_attributes 
            print "HidD_GetAttributes fail" 
            self.ShowLastErrorMsg()
        #vendor_string_type = c_wchar * 128
        #vendor_name = vendor_string_type()
        #if not HidD_GetManufacturerString(h_hid_device, 
        #            byref(vendor_name), sizeof(vendor_name)) or not len(vendor_name.value):
                # would be any possibility to get a vendor id table?, 
                # maybe not worth it
        #    print("vendor_name = %s" % "Unknown manufacturer")
        #    self.ShowLastErrorMsg()
        #else:
        #    print("vendor_name = %s" % vendor_name.value)
        #del vendor_name
        #del vendor_string_type
        #ptr_preparsed_data = c_ulong()
        #if not ctypes.windll.hid.HidD_GetPreparsedData(int(h_hid_device), 
        #        byref(ptr_preparsed_data)):
        #    CloseHandle(h_hid_device)
        #    print("Failure to get HID pre parsed data")
        #    self.ShowLastErrorMsg()
        #hid_caps = HIDP_CAPS()
        #status = ctypes.windll.hid.HidP_GetCaps(ptr_preparsed_data, 
        #    byref(hid_caps))
        #print(status)
        CloseHandle(h_hid_device)    
        