'''
Created on 2013/9/12

@author: RobertChen
'''
import WinDataType 
from WinDataType import *

import platform
#constant
if platform.architecture()[0].startswith('64'):
    WIN_PACK_SIZE = 8
else:
    WIN_PACK_SIZE = 1
ANYSIZE_ARRAY = 1
#class      

class GUID(Structure):
    """
    typedef struct _GUID {
          DWORD Data1;
          WORD  Data2;
          WORD  Data3;
          BYTE  Data4[8];
        } GUID
    """
    _pack_ = 1
    _fields_ = [("Data1", DWORD),
                ("Data2", WORD),
                ("Data3", WORD),
                ("Data4", BYTE * 8)]
    def __str__(self):
        return "{%08x-%04x-%04x%s-%s}" % (
            self.Data1,
            self.Data2,
            self.Data3,
            ''.join(["%02x" % d for d in self.Data4[:2]]),
            ''.join(["%02x" % d for d in self.Data4[2:]]),
        )
    def __eq__(self, other):
        return ((self.Data1    == other.Data1   ) and 
                (self.Data2    == other.Data2   ) and 
                (self.Data3    == other.Data3   ) and 
                (self.Data4[0] == other.Data4[0]) and 
                (self.Data4[1] == other.Data4[1]) and
                (self.Data4[2] == other.Data4[2]) and
                (self.Data4[3] == other.Data4[3]) and
                (self.Data4[4] == other.Data4[4]) and
                (self.Data4[5] == other.Data4[5]) and
                (self.Data4[6] == other.Data4[6]) and
                (self.Data4[7] == other.Data4[7]))
PGUID = POINTER(GUID)
if __name__ == "__main__":
    print "sizeof(GUID) = %d" % sizeof(GUID) 

"""
typedef struct {
  SP_CLASSINSTALL_HEADER ClassInstallHeader;
  DWORD                  Flags;
  HPROPSHEETPAGE         DynamicPages[MAX_INSTALLWIZARD_DYNAPAGES];
  DWORD                  NumDynamicPages;
  HWND                   hwndWizardDlg;
} SP_ADDPROPERTYPAGE_DATA, *PSP_ADDPROPERTYPAGE_DATA;
  typedef struct {
  DWORD cbSize;
  DWORD Platform;
  DWORD MajorVersion;
  DWORD MinorVersion;
  WORD  ProcessorArchitecture;
  WORD  Reserved;
} SP_ALTPLATFORM_INFO, *PSP_ALTPLATFORM_INFO;
"""    
"""
typedef struct _SP_CLASSIMAGELIST_DATA {
  DWORD      cbSize;
  HIMAGELIST ImageList;
  ULONG_PTR  Reserved;
} SP_CLASSIMAGELIST_DATA, *PSP_CLASSIMAGELIST_DATA;
"""
"""
typedef struct _SP_CLASSINSTALL_HEADER {
  DWORD       cbSize;
  DI_FUNCTION InstallFunction;
} SP_CLASSINSTALL_HEADER, *PSP_CLASSINSTALL_HEADER;
"""
"""
typedef struct _SP_DETECTDEVICE_PARAMS {
  SP_CLASSINSTALL_HEADER  ClassInstallHeader;
  PDETECT_PROGRESS_NOTIFY DetectProgressNotify;
  PVOID                   ProgressNotifyParam;
} SP_DETECTDEVICE_PARAMS, *PSP_DETECTDEVICE_PARAMS;
"""
class SP_DEVICE_INTERFACE_DATA(Structure):
    """
typedef struct _SP_DEVICE_INTERFACE_DATA {
  DWORD     cbSize;
  GUID      InterfaceClassGuid;
  DWORD     Flags;
  ULONG_PTR Reserved;
} SP_DEVICE_INTERFACE_DATA, *PSP_DEVICE_INTERFACE_DATA;
    """
    #for Flags return value
    FLAGS_SPINT_ACTIVE  = 0x00000001
    FLAGS_SPINT_DEFAULT = 0x00000002
    FLAGS_SPINT_REMOVED = 0x00000004
    _pack_ = WIN_PACK_SIZE
    _fields_ = [("cbSize"            , DWORD),
                ("InterfaceClassGuid", GUID),
                ("Flags"             , DWORD),
                ("Reserved"          , ULONG_PTR)
                ]
    def __str__(self):
        return "SP_DEVICE_INTERFACE_DATA:cbSize:%d InterfaceClassGuid:%s Flags:0x%x" % (self.cbSize,self.InterfaceClassGuid, self.Flags)
    
PSP_DEVICE_INTERFACE_DATA = POINTER(SP_DEVICE_INTERFACE_DATA)
if __name__ == "__main__":
    print "sizeof(SP_DEVICE_INTERFACE_DATA) = %d" % sizeof(SP_DEVICE_INTERFACE_DATA)

class SP_DEVICE_INTERFACE_DETAIL_DATA(Structure):    
    """
typedef struct _SP_DEVICE_INTERFACE_DETAIL_DATA {
  DWORD cbSize;
  TCHAR DevicePath[ANYSIZE_ARRAY];
} SP_DEVICE_INTERFACE_DETAIL_DATA, *PSP_DEVICE_INTERFACE_DETAIL_DATA;
    """
    _pack_ = WIN_PACK_SIZE
    _fields_ = [("cbSize"    , DWORD),
                ("DevicePath", TCHAR * ANYSIZE_ARRAY)
                ]
    def __str__(self):
        return "SP_DEVICE_INTERFACE_DETAIL_DATA:cbSize:%d,DevicePath:%s" % (self.cbSize,ctypes.wstring_at(byref(self,sizeof(DWORD))))

PSP_DEVICE_INTERFACE_DETAIL_DATA = POINTER(SP_DEVICE_INTERFACE_DETAIL_DATA)
if __name__ == "__main__":
    print "sizeof(SP_DEVICE_INTERFACE_DETAIL_DATA)=%d" % sizeof(SP_DEVICE_INTERFACE_DETAIL_DATA) 

class SP_DEVINFO_DATA(Structure):
    """
typedef struct _SP_DEVINFO_DATA {
  DWORD     cbSize;
  GUID      ClassGuid;
  DWORD     DevInst;
  ULONG_PTR Reserved;
} SP_DEVINFO_DATA, *PSP_DEVINFO_DATA;
    """
    _pack_ = WIN_PACK_SIZE
    _fields_ = [("cbSize"   , DWORD),
               ("ClassGuid" , GUID),
               ("DevInst"   , DWORD),
               ("Reserved"  , ULONG_PTR)
               ]
    def __str__(self):
        return "SP_DEVINFO_DATA:cbSize:%d ClassGuid:%s DevInst:0x%x" % (self.cbSize,self.ClassGuid, self.DevInst)

PSP_DEVINFO_DATA = POINTER(SP_DEVINFO_DATA)
if __name__ == "__main__":
    print "sizeof(SP_DEVINFO_DATA)=%d" % sizeof(SP_DEVINFO_DATA) 

"""
typedef struct _SP_DEVINFO_LIST_DETAIL_DATA {
  DWORD  cbSize;
  GUID   ClassGuid;
  HANDLE RemoteMachineHandle;
  TCHAR  RemoteMachineName[SP_MAX_MACHINENAME_LENGTH];
} SP_DEVINFO_LIST_DETAIL_DATA, *PSP_DEVINFO_LIST_DETAIL_DATA;
"""
"""
typedef struct _SP_DEVINSTALL_PARAMS {
  DWORD             cbSize;
  DWORD             Flags;
  DWORD             FlagsEx;
  HWND              hwndParent;
  PSP_FILE_CALLBACK InstallMsgHandler;
  PVOID             InstallMsgHandlerContext;
  HSPFILEQ          FileQueue;
  ULONG_PTR         ClassInstallReserved;
  DWORD             Reserved;
  TCHAR             DriverPath[MAX_PATH];
} SP_DEVINSTALL_PARAMS, *PSP_DEVINSTALL_PARAMS;
"""
"""
typedef struct {
  DWORD     cbSize;
  DWORD     DriverType;
  ULONG_PTR Reserved;
  TCHAR     Description[LINE_LEN];
  TCHAR     MfgName[LINE_LEN];
  TCHAR     ProviderName[LINE_LEN];
  FILETIME  DriverDate;
  DWORDLONG DriverVersion;
} SP_DRVINFO_DATA, *PSP_DRVINFO_DATA;
"""
"""
typedef struct _SP_DRVINFO_DETAIL_DATA {
  DWORD     cbSize;
  FILETIME  InfDate;
  DWORD     CompatIDsOffset;
  DWORD     CompatIDsLength;
  ULONG_PTR Reserved;
  TCHAR     SectionName[LINE_LEN];
  TCHAR     InfFileName[MAX_PATH];
  TCHAR     DrvDescription[LINE_LEN];
  TCHAR     HardwareID[ANYSIZE_ARRAY];
} SP_DRVINFO_DETAIL_DATA, *PSP_DRVINFO_DETAIL_DATA;
"""
"""
typedef struct _SP_DRVINSTALL_PARAMS {
  DWORD     cbSize;
  DWORD     Rank;
  DWORD     Flags;
  DWORD_PTR PrivateData;
  DWORD     Reserved;
} SP_DRVINSTALL_PARAMS, *PSP_DRVINSTALL_PARAMS;
"""
"""
typedef struct _SP_NEWDEVICEWIZARD_DATA {
  SP_CLASSINSTALL_HEADER ClassInstallHeader;
  DWORD                  Flags;
  HPROPSHEETPAGE         DynamicPages[MAX_INSTALLWIZARD_DYNAPAGES];
  DWORD                  NumDynamicPages;
  HWND                   hwndWizardDlg;
} SP_NEWDEVICEWIZARD_DATA, *PSP_NEWDEVICEWIZARD_DATA;
"""
"""
typedef struct _SP_POWERMESSAGEWAKE_PARAMS {
  SP_CLASSINSTALL_HEADER ClassInstallHeader;
  TCHAR                  PowerMessageWake[LINE_LEN*2];
} SP_POWERMESSAGEWAKE_PARAMS, *PSP_POWERMESSAGEWAKE_PARAMS;
"""
"""
typedef struct _SP_PROPCHANGE_PARAMS {
  SP_CLASSINSTALL_HEADER ClassInstallHeader;
  DWORD                  StateChange;
  DWORD                  Scope;
  DWORD                  HwProfile;
} SP_PROPCHANGE_PARAMS, *PSP_PROPCHANGE_PARAMS;
"""
"""
typedef struct _SP_PROPSHEETPAGE_REQUEST {
  DWORD            cbSize;
  DWORD            PageRequested;
  HDEVINFO         DeviceInfoSet;
  PSP_DEVINFO_DATA DeviceInfoData;
} SP_PROPSHEETPAGE_REQUEST, *PSP_PROPSHEETPAGE_REQUEST;
"""
"""
typedef struct _SP_REMOVEDEVICE_PARAMS {
  SP_CLASSINSTALL_HEADER ClassInstallHeader;
  DWORD                  Scope;
  DWORD                  HwProfile;
} SP_REMOVEDEVICE_PARAMS, *PSP_REMOVEDEVICE_PARAMS;
"""
"""
typedef struct _SP_SELECTDEVICE_PARAMS {
  SP_CLASSINSTALL_HEADER ClassInstallHeader;
  TCHAR                  Title[MAX_TITLE_LEN];
  TCHAR                  Instructions[MAX_INSTRUCTION_LEN];
  TCHAR                  ListLabel[MAX_LABEL_LEN];
  TCHAR                  SubTitle[MAX_SUBTITLE_LEN];
  BYTE                   Reserved[2];
} SP_SELECTDEVICE_PARAMS, *PSP_SELECTDEVICE_PARAMS;
"""
"""
typedef struct _SP_TROUBLESHOOTER_PARAMS {
  SP_CLASSINSTALL_HEADER ClassInstallHeader;
  TCHAR                  ChmFile[MAX_PATH];
  TCHAR                  HtmlTroubleShooter[MAX_PATH];
} SP_TROUBLESHOOTER_PARAMS, *PSP_TROUBLESHOOTER_PARAMS;
"""
"""
typedef struct _SP_UNREMOVEDEVICE_PARAMS {
  SP_CLASSINSTALL_HEADER ClassInstallHeader;
  DWORD                  Scope;
  DWORD                  HwProfile;
} SP_UNREMOVEDEVICE_PARAMS, *PSP_UNREMOVEDEVICE_PARAMS;
"""

