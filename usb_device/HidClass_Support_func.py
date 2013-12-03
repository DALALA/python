'''
Created on 2013/10/2

@author: RobertChen
'''
import HidClass
from HidClass import *
import SetupAPIClass
from SetupAPIClass import *
"""
BOOLEAN __stdcall HidD_FlushQueue(
  _In_  HANDLE HidDeviceObject
);
"""
"""
BOOLEAN __stdcall HidD_FreePreparsedData(
  _In_  PHIDP_PREPARSED_DATA PreparsedData
);
"""
HidD_FreePreparsedData = ctypes.windll.hid.HidD_FreePreparsedData
HidD_FreePreparsedData.restype = BOOLEAN
HidD_FreePreparsedData.argtypes = [
                                   ULONG_PTR
                                   ]
"""
BOOLEAN __stdcall HidD_GetAttributes(
  _In_   HANDLE HidDeviceObject,
  _Out_  PHIDD_ATTRIBUTES Attributes
);
"""
HidD_GetAttributes = ctypes.windll.hid.HidD_GetAttributes
HidD_GetAttributes.restype = BOOLEAN
HidD_GetAttributes.argtypes = [
                               HANDLE,
                               PHIDD_ATTRIBUTES
                               ]
"""
BOOLEAN __stdcall HidD_GetFeature(
  _In_   HANDLE HidDeviceObject,
  _Out_  PVOID ReportBuffer,
  _In_   ULONG ReportBufferLength
);
void __stdcall HidD_GetHidGuid(
  _Out_  LPGUID HidGuid
);
"""
HidD_GetHidGuid = ctypes.windll.hid.HidD_GetHidGuid
HidD_GetHidGuid.restype = None
HidD_GetHidGuid.argtypes = [
                            PGUID
                           ]
if __name__ == "__main__":
    hid_guid = GUID()
    HidD_GetHidGuid(byref(hid_guid))
    print "HidD_GetHidGuid:",hid_guid 
"""
BOOLEAN __stdcall HidD_GetIndexedString(
  _In_   HANDLE HidDeviceObject,
  _In_   ULONG StringIndex,
  _Out_  PVOID Buffer,
  _In_   ULONG BufferLength
);
BOOLEAN __stdcall HidD_GetInputReport(
  _In_   HANDLE HidDeviceObject,
  _Out_  PVOID ReportBuffer,
  _In_   ULONG ReportBufferLength
);
"""
"""
BOOLEAN __stdcall HidD_GetManufacturerString(
  _In_   HANDLE HidDeviceObject,
  _Out_  PVOID Buffer,
  _In_   ULONG BufferLength
);
"""
HidD_GetManufacturerString = ctypes.windll.hid.HidD_GetManufacturerString
HidD_GetManufacturerString.restype = BOOLEAN
HidD_GetManufacturerString.argtypes = [
                                       HANDLE,
                                       PVOID,
                                       ULONG
                                       ]
"""
BOOLEAN __stdcall HidD_GetNumInputBuffers(
  _In_   HANDLE HidDeviceObject,
  _Out_  PULONG NumberBuffers
);
BOOLEAN __stdcall HidD_GetPhysicalDescriptor(
  _In_   HANDLE HidDeviceObject,
  _Out_  PVOID Buffer,
  _In_   ULONG BufferLength
);
"""
"""
BOOLEAN __stdcall HidD_GetPreparsedData(
  _In_   HANDLE HidDeviceObject,
  _Out_  PHIDP_PREPARSED_DATA *PreparsedData
);
"""
"""
BOOLEAN __stdcall HidD_GetProductString(
  _In_   HANDLE HidDeviceObject,
  _Out_  PVOID Buffer,
  _In_   ULONG BufferLength
);
BOOLEAN __stdcall HidD_GetSerialNumberString(
  _In_   HANDLE HidDeviceObject,
  _Out_  PVOID Buffer,
  _In_   ULONG BufferLength
);
BOOLEAN __stdcall HidD_SetFeature(
  _In_  HANDLE HidDeviceObject,
  _In_  PVOID ReportBuffer,
  _In_  ULONG ReportBufferLength
);
BOOLEAN __stdcall HidD_SetNumInputBuffers(
  _In_  HANDLE HidDeviceObject,
  _In_  ULONG NumberBuffers
);
BOOLEAN __stdcall HidD_SetOutputReport(
  _In_  HANDLE HidDeviceObject,
  _In_  PVOID ReportBuffer,
  _In_  ULONG ReportBufferLength
);
NTSTATUS __stdcall HidP_GetButtonCaps(
  _In_     HIDP_REPORT_TYPE ReportType,
  _Out_    PHIDP_BUTTON_CAPS ButtonCaps,
  _Inout_  PUSHORT ButtonCapsLength,
  _In_     PHIDP_PREPARSED_DATA PreparsedData
);
#define HidP_GetButtons(Rty, UPa, LCo, ULi, ULe, Ppd, Rep, RLe) \
        HidP_GetUsages(Rty, UPa, LCo, ULi, ULe, Ppd, Rep, RLe)
#define HidP_GetButtonsEx(Rty, LCo, BLi, ULe, Ppd, Rep, RLe)  \
         HidP_GetUsagesEx(Rty, LCo, BLi, ULe, Ppd, Rep, RLe)
NTSTATUS __stdcall HidP_GetCaps(
  _In_   PHIDP_PREPARSED_DATA PreparsedData,
  _Out_  PHIDP_CAPS Capabilities
);
NTSTATUS __stdcall HidP_GetData(
  _In_     HIDP_REPORT_TYPE ReportType,
  _Out_    PHIDP_DATA DataList,
  _Inout_  PULONG DataLength,
  _In_     PHIDP_PREPARSED_DATA PreparsedData,
  _Out_    PCHAR Report,
  _In_     ULONG ReportLength
);
NTSTATUS __stdcall HidP_GetExtendedAttributes(
  _In_     HIDP_REPORT_TYPE ReportType,
  _In_     USHORT DataIndex,
  _In_     PHIDP_PREPARSED_DATA PreparsedData,
  _Out_    PHIDP_EXTENDED_ATTRIBUTES Attributes,
  _Inout_  PULONG LengthAttributes
);
NTSTATUS __stdcall HidP_GetLinkCollectionNodes(
  _Out_    PHIDP_LINK_COLLECTION_NODE LinkCollectionNodes,
  _Inout_  PULONG LinkCollectionNodesLength,
  _In_     PHIDP_PREPARSED_DATA PreparsedData
);
NTSTATUS __stdcall HidP_GetScaledUsageValue(
  _In_   HIDP_REPORT_TYPE ReportType,
  _In_   USAGE UsagePage,
  _In_   USHORT LinkCollection,
  _In_   USAGE Usage,
  _Out_  PLONG UsageValue,
  _In_   PHIDP_PREPARSED_DATA PreparsedData,
  _In_   PCHAR Report,
  _In_   ULONG ReportLength
);
NTSTATUS __stdcall HidP_GetSpecificButtonCaps(
  _In_     HIDP_REPORT_TYPE ReportType,
  _In_     USAGE UsagePage,
  _In_     USHORT LinkCollection,
  _In_     USAGE Usage,
  _Out_    PHIDP_BUTTON_CAPS ButtonCaps,
  _Inout_  PUSHORT ButtonCapsLength,
  _In_     PHIDP_PREPARSED_DATA PreparsedData
);
NTSTATUS __stdcall HidP_GetSpecificValueCaps(
  _In_     HIDP_REPORT_TYPE ReportType,
  _In_     USAGE UsagePage,
  _In_     USHORT LinkCollection,
  _In_     USAGE Usage,
  _Out_    PHIDP_VALUE_CAPS ValueCaps,
  _Inout_  PUSHORT ValueCapsLength,
  _In_     PHIDP_PREPARSED_DATA PreparsedData
);
NTSTATUS __stdcall HidP_GetUsages(
  _In_     HIDP_REPORT_TYPE ReportType,
  _In_     USAGE UsagePage,
  _In_     USHORT LinkCollection,
  _Out_    PUSAGE UsageList,
  _Inout_  PULONG UsageLength,
  _In_     PHIDP_PREPARSED_DATA PreparsedData,
  _Out_    PCHAR Report,
  _In_     ULONG ReportLength
);
NTSTATUS __stdcall HidP_GetUsagesEx(
  _In_     HIDP_REPORT_TYPE ReportType,
  _In_     USHORT LinkCollection,
  _Inout_  PUSAGE_AND_PAGE ButtonList,
  _Inout_  ULONG *UsageLength,
  _In_     PHIDP_PREPARSED_DATA PreparsedData,
  _In_     PCHAR Report,
  _In_     ULONG ReportLength
);
NTSTATUS __stdcall HidP_GetUsageValue(
  _In_   HIDP_REPORT_TYPE ReportType,
  _In_   USAGE UsagePage,
  _In_   USHORT LinkCollection,
  _In_   USAGE Usage,
  _Out_  PULONG UsageValue,
  _In_   PHIDP_PREPARSED_DATA PreparsedData,
  _In_   PCHAR Report,
  _In_   ULONG ReportLength
);
NTSTATUS __stdcall HidP_GetUsageValueArray(
  _In_     HIDP_REPORT_TYPE ReportType,
  _In_     USAGE UsagePage,
  _In_     USHORT LinkCollection,
  _In_     USAGE Usage,
  _Inout_  PCHAR UsageValue,
  _In_     USHORT UsageValueByteLength,
  _In_     PHIDP_PREPARSED_DATA PreparsedData,
  _In_     PCHAR Report,
  _In_     ULONG ReportLength
);
NTSTATUS __stdcall HidP_GetValueCaps(
  _In_     HIDP_REPORT_TYPE ReportType,
  _Out_    PHIDP_VALUE_CAPS ValueCaps,
  _Inout_  PUSHORT ValueCapsLength,
  _In_     PHIDP_PREPARSED_DATA PreparsedData
);
NTSTATUS __stdcall HidP_InitializeReportForID(
  _In_   HIDP_REPORT_TYPE ReportType,
  _In_   UCHAR ReportID,
  _In_   PHIDP_PREPARSED_DATA PreparsedData,
  _Out_  PCHAR Report,
  _In_   ULONG ReportLength
);
BOOLEAN HidP_IsSameUsageAndPage(
  USAGE_AND_PAGE u1,
  USAGE_AND_PAGE u2
);
ULONG __stdcall HidP_MaxDataListLength(
  _In_  HIDP_REPORT_TYPE ReportType,
  _In_  PHIDP_PREPARSED_DATA PreparsedData
);
ULONG __stdcall HidP_MaxUsageListLength(
  _In_  HIDP_REPORT_TYPE ReportType,
  _In_  USAGE UsagePage,
  _In_  PHIDP_PREPARSED_DATA PreparsedData
);
#define HidP_SetButtons(Rty, Up, Lco, ULi, ULe, Ppd, Rep, Rle) \
        HidP_SetUsages(Rty, Up, Lco, ULi, ULe, Ppd, Rep, Rle)
NTSTATUS __stdcall HidP_SetData(
  _In_     HIDP_REPORT_TYPE ReportType,
  _Inout_  PHIDP_DATA DataList,
  _Inout_  PULONG DataLength,
  _In_     PHIDP_PREPARSED_DATA PreparsedData,
  _In_     PCHAR Report,
  _In_     ULONG ReportLength
);
NTSTATUS __stdcall HidP_SetScaledUsageValue(
  _In_     HIDP_REPORT_TYPE ReportType,
  _In_     USAGE UsagePage,
  _In_     USHORT LinkCollection,
  _In_     USAGE Usage,
  _In_     LONG UsageValue,
  _In_     PHIDP_PREPARSED_DATA PreparsedData,
  _Inout_  PCHAR Report,
  _In_     ULONG ReportLength
);
NTSTATUS __stdcall HidP_SetUsages(
  _In_     HIDP_REPORT_TYPE ReportType,
  _In_     USAGE UsagePage,
  _In_     USHORT LinkCollection,
  _Inout_  PUSAGE UsageList,
  _Inout_  PULONG UsageLength,
  _In_     PHIDP_PREPARSED_DATA PreparsedData,
  _In_     PCHAR Report,
  _In_     ULONG ReportLength
);
NTSTATUS __stdcall HidP_SetUsageValue(
  _In_     HIDP_REPORT_TYPE ReportType,
  _In_     USAGE UsagePage,
  _In_     USHORT LinkCollection,
  _In_     USAGE Usage,
  _In_     ULONG UsageValue,
  _In_     PHIDP_PREPARSED_DATA PreparsedData,
  _Inout_  PCHAR Report,
  _In_     ULONG ReportLength
);
NTSTATUS __stdcall HidP_SetUsageValueArray(
  _In_     HIDP_REPORT_TYPE ReportType,
  _In_     USAGE UsagePage,
  _In_     USHORT LinkCollection,
  _In_     USAGE Usage,
  _In_     PCHAR UsageValue,
  _In_     USHORT UsageValueByteLength,
  _In_     PHIDP_PREPARSED_DATA PreparsedData,
  _Inout_  PCHAR Report,
  _In_     ULONG ReportLength
);
NTSTATUS __stdcall HidP_TranslateUsagesToI8042ScanCodes(
  _In_      PUSAGE ChangedUsageList,
  _In_      ULONG UsageListLength,
  _In_      HIDP_KEYBOARD_DIRECTION KeyAction,
  _Inout_   PHIDP_KEYBOARD_MODIFIER_STATE ModifierState,
  _In_      PHIDP_INSERT_SCANCODES InsertCodesProcedure,
  _In_opt_  PVOID InsertCodesContext
);
#define HidP_UnsetButtons(Rty, Up, Lco, ULi, ULe, Ppd, Rep, Rle) \
        HidP_UnsetUsages(Rty, Up, Lco, ULi, ULe, Ppd, Rep, Rle)
NTSTATUS __stdcall HidP_UnsetUsages(
  _In_      HIDP_REPORT_TYPE ReportType,
  _In_      USAGE UsagePage,
  _In_opt_  USHORT LinkCollection,
  _Inout_   PUSAGE UsageList,
  _Inout_   PULONG UsageLength,
  _In_      PHIDP_PREPARSED_DATA PreparsedData,
  _In_      PCHAR Report,
  _In_      ULONG ReportLength
);
HidP_UsageAndPageListDifference 
NTSTATUS __stdcall HidP_UsageListDifference(
  _In_   PUSAGE PreviousUsageList,
  _In_   PUSAGE CurrentUsageList,
  _Out_  PUSAGE BreakUsageList,
  _Out_  PUSAGE MakeUsageList,
  _In_   ULONG UsageListLength
);
NTSTATUS HidRegisterMinidriver(
  _In_  PHID_MINIDRIVER_REGISTRATION MinidriverRegistration
);
"""
"""
HANDLE WINAPI CreateFile(
  _In_      LPCTSTR lpFileName,
  _In_      DWORD dwDesiredAccess,
  _In_      DWORD dwShareMode,
  _In_opt_  LPSECURITY_ATTRIBUTES lpSecurityAttributes,
  _In_      DWORD dwCreationDisposition,
  _In_      DWORD dwFlagsAndAttributes,
  _In_opt_  HANDLE hTemplateFile
);
"""
CreateFile = ctypes.windll.kernel32.CreateFileW
CreateFile.restype = HANDLE
CreateFile.argtypes = [
                       LPCTSTR,
                       DWORD,
                       DWORD,
                       LPSECURITY_ATTRIBUTES,
                       DWORD,
                       DWORD,
                       HANDLE 
                       ]
"""
BOOL WINAPI CloseHandle(
  _In_  HANDLE hObject
);
"""
CloseHandle = ctypes.windll.kernel32.CloseHandle
CloseHandle.restype = BOOL
CloseHandle.argtypes = [
                        HANDLE
                        ]