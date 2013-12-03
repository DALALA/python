'''
Created on 2013/9/12

@author: RobertChen
'''
import SetupAPIClass
from SetupAPIClass import *
"""
BOOL DiInstallDevice(
  _In_opt_   HWND hwndParent,
  _In_       HDEVINFO DeviceInfoSet,
  _In_       PSP_DEVINFO_DATA DeviceInfoData,
  _In_opt_   PSP_DRVINFO_DATA DriverInfoData,
  _In_       DWORD Flags,
  _Out_opt_  PBOOL NeedReboot
);
BOOL DiInstallDriver(
  _In_opt_   HWND hwndParent,
  _In_       LPCTSTR FullInfPath,
  _In_       DWORD Flags,
  _Out_opt_  PBOOL NeedReboot
);
BOOL DiRollbackDriver(
  _In_       HDEVINFO DeviceInfoSet,
  _In_       PSP_DEVINFO_DATA DeviceInfoData,
  _In_opt_   HWND hwndParent,
  _In_       DWORD Flags,
  _Out_opt_  PBOOL NeedReboot
);
BOOL DiShowUpdateDevice(
  _In_opt_   HWND hwndParent,
  _In_       HDEVINFO DeviceInfoSet,
  _In_       PSP_DEVINFO_DATA DeviceInfoData,
  _In_       DWORD Flags,
  _Out_opt_  PBOOL NeedReboot
);
BOOL DiUninstallDevice(
  _In_       HWND hwndParent,
  _In_       HDEVINFO DeviceInfoSet,
  _In_       PSP_DEVINFO_DATA DeviceInfoData,
  _In_       DWORD Flags,
  _Out_opt_  PBOOL NeedReboot
);
BOOL WINAPI InstallSelectedDriver(
  _In_   HWND hwndParent,
  _In_   HDEVINFO DeviceInfoSet,
  _In_   LPCTSTR Reserved,
  _In_   BOOL Backup,
  _Out_  PDWORD bReboot
);
BOOL SetupDiAskForOEMDisk(
  _In_      HDEVINFO DeviceInfoSet,
  _In_opt_  PSP_DEVINFO_DATA DeviceInfoData
);
BOOL SetupDiBuildClassInfoList(
  _In_       DWORD Flags,
  _Out_opt_  LPGUID ClassGuidList,
  _In_       DWORD ClassGuidListSize,
  _Out_      PDWORD RequiredSize
);
BOOL SetupDiBuildClassInfoListEx(
  _In_        DWORD Flags,
  _Out_opt_   LPGUID ClassGuidList,
  _In_        DWORD ClassGuidListSize,
  _Out_       PDWORD RequiredSize,
  _In_opt_    PCTSTR MachineName,
  _Reserved_  PVOID Reserved
);
BOOL SetupDiBuildDriverInfoList(
  _In_     HDEVINFO DeviceInfoSet,
  _Inout_  PSP_DEVINFO_DATA DeviceInfoData,
  _In_     DWORD DriverType
);
BOOL SetupDiCallClassInstaller(
  _In_      DI_FUNCTION InstallFunction,
  _In_      HDEVINFO DeviceInfoSet,
  _In_opt_  PSP_DEVINFO_DATA DeviceInfoData
);
BOOL SetupDiCancelDriverInfoSearch(
  _In_  HDEVINFO DeviceInfoSet
);
BOOL SetupDiChangeState(
  _In_     HDEVINFO DeviceInfoSet,
  _Inout_  PSP_DEVINFO_DATA DeviceInfoData
);
BOOL SetupDiClassGuidsFromName(
  _In_   PCTSTR ClassName,
  _Out_  LPGUID ClassGuidList,
  _In_   DWORD ClassGuidListSize,
  _Out_  PDWORD RequiredSize
);
BOOL SetupDiClassGuidsFromNameEx(
  _In_        PCTSTR ClassName,
  _Out_       LPGUID ClassGuidList,
  _In_        DWORD ClassGuidListSize,
  _Out_       PDWORD RequiredSize,
  _In_opt_    PCTSTR MachineName,
  _Reserved_  PVOID Reserved
);
BOOL SetupDiClassNameFromGuid(
  _In_       const GUID *ClassGuid,
  _Out_      PTSTR ClassName,
  _In_       DWORD ClassNameSize,
  _Out_opt_  PDWORD RequiredSize
);
BOOL SetupDiClassNameFromGuidEx(
  _In_        const GUID *ClassGuid,
  _Out_       PTSTR ClassName,
  _In_        DWORD ClassNameSize,
  _Out_opt_   PDWORD RequiredSize,
  _In_opt_    PCTSTR MachineName,
  _Reserved_  PVOID Reserved
);
BOOL SetupDiCreateDeviceInfo(
  _In_       HDEVINFO DeviceInfoSet,
  _In_       PCTSTR DeviceName,
  _In_       const GUID *ClassGuid,
  _In_opt_   PCTSTR DeviceDescription,
  _In_opt_   HWND hwndParent,
  _In_       DWORD CreationFlags,
  _Out_opt_  PSP_DEVINFO_DATA DeviceInfoData
);
HDEVINFO SetupDiCreateDeviceInfoList(
  _In_opt_  const GUID *ClassGuid,
  _In_opt_  HWND hwndParent
);
HDEVINFO SetupDiCreateDeviceInfoListEx(
  _In_opt_    const GUID *ClassGuid,
  _In_opt_    HWND hwndParent,
  _In_opt_    PCTSTR MachineName,
  _Reserved_  PVOID Reserved
);
BOOL SetupDiCreateDeviceInterface(
  _In_       HDEVINFO DeviceInfoSet,
  _In_       PSP_DEVINFO_DATA DeviceInfoData,
  _In_       const GUID *InterfaceClassGuid,
  _In_opt_   PCTSTR ReferenceString,
  _In_       DWORD CreationFlags,
  _Out_opt_  PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData
);
HKEY SetupDiCreateDeviceInterfaceRegKey(
  _In_        HDEVINFO DeviceInfoSet,
  _In_        PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
  _Reserved_  DWORD Reserved,
  _In_        REGSAM samDesired,
  _In_opt_    HINF InfHandle,
  _In_opt_    PCTSTR InfSectionName
);
HKEY SetupDiCreateDevRegKey(
  _In_      HDEVINFO DeviceInfoSet,
  _In_      PSP_DEVINFO_DATA DeviceInfoData,
  _In_      DWORD Scope,
  _In_      DWORD HwProfile,
  _In_      DWORD KeyType,
  _In_opt_  HINF InfHandle,
  _In_opt_  PCTSTR InfSectionName
);
BOOL SetupDiDeleteDeviceInfo(
  _In_  HDEVINFO DeviceInfoSet,
  _In_  PSP_DEVINFO_DATA DeviceInfoData
);
BOOL SetupDiDeleteDeviceInterfaceData(
  _In_  HDEVINFO DeviceInfoSet,
  _In_  PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData
);
BOOL SetupDiDeleteDeviceInterfaceRegKey(
  _In_        HDEVINFO DeviceInfoSet,
  _In_        PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
  _Reserved_  DWORD Reserved
);
BOOL SetupDiDeleteDevRegKey(
  _In_  HDEVINFO DeviceInfoSet,
  _In_  PSP_DEVINFO_DATA DeviceInfoData,
  _In_  DWORD Scope,
  _In_  DWORD HwProfile,
  _In_  DWORD KeyType
);
BOOL SetupDiDestroyClassImageList(
  _In_  PSP_CLASSIMAGELIST_DATA ClassImageListData
);
"""
"""
BOOL SetupDiDestroyDeviceInfoList(
  _In_  HDEVINFO DeviceInfoSet
);
"""
SetupDiDestroyDeviceInfoList = ctypes.windll.setupapi.SetupDiDestroyDeviceInfoList
SetupDiDestroyDeviceInfoList.restype = BOOL
SetupDiDestroyDeviceInfoList.argtypes = [
                                         HDEVINFO
                                         ]
INVALID_HANDLE_VALUE  = 0xFFFFFFFF
"""
BOOL SetupDiDestroyDriverInfoList(
  _In_      HDEVINFO DeviceInfoSet,
  _In_opt_  PSP_DEVINFO_DATA DeviceInfoData,
  _In_      DWORD DriverType
);
INT SetupDiDrawMiniIcon(
  _In_  HDC hdc,
  _In_  RECT rc,
  _In_  INT MiniIconIndex,
  _In_  DWORD Flags
);
"""
"""
BOOL SetupDiEnumDeviceInfo(
  _In_   HDEVINFO DeviceInfoSet,
  _In_   DWORD MemberIndex,
  _Out_  PSP_DEVINFO_DATA DeviceInfoData
);
"""
SetupDiEnumDeviceInfo = ctypes.windll.setupapi.SetupDiEnumDeviceInfo
SetupDiEnumDeviceInfo.restype = BOOL
SetupDiEnumDeviceInfo.argtypes = [
                                  HDEVINFO,
                                  DWORD,
                                  PSP_DEVINFO_DATA
                                  ]
"""
BOOL SetupDiEnumDeviceInterfaces(
  _In_      HDEVINFO DeviceInfoSet,
  _In_opt_  PSP_DEVINFO_DATA DeviceInfoData,
  _In_      const GUID *InterfaceClassGuid,
  _In_      DWORD MemberIndex,
  _Out_     PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData
);
"""
SetupDiEnumDeviceInterfaces = ctypes.windll.setupapi.SetupDiEnumDeviceInterfaces
SetupDiEnumDeviceInterfaces.restype = BOOL
SetupDiEnumDeviceInterfaces.argtypes = [
                                        HDEVINFO,
                                        PSP_DEVINFO_DATA,
                                        PGUID,
                                        DWORD,
                                        PSP_DEVICE_INTERFACE_DATA
                                        ]
"""
BOOL SetupDiEnumDriverInfo(
  _In_      HDEVINFO DeviceInfoSet,
  _In_opt_  PSP_DEVINFO_DATA DeviceInfoData,
  _In_      DWORD DriverType,
  _In_      DWORD MemberIndex,
  _Out_     PSP_DRVINFO_DATA_W DriverInfoData
);
BOOL SetupDiFinishInstallAction(
  _In_  HDEVINFO DeviceInfoSet,
  _In_  PSP_DEVINFO_DATA DeviceInfoData
);
BOOL SetupDiGetActualModelsSection(
  _In_        PINFCONTEXT Context,
  _In_opt_    PSP_ALTPLATFORM_INFO AlternatePlatformInfo,
  _Out_opt_   PTSTR DecoratedModelsSection,
  _In_        DWORD DecoratedModelsSectionSize,
  _Out_opt_   PDWORD RequiredSize,
  _Reserved_  PVOID Reserved
);
BOOL SetupDiGetActualSectionToInstall(
  _In_       HINF InfHandle,
  _In_       PCTSTR InfSectionName,
  _Out_opt_  PTSTR InfSectionWithExt,
  _In_       DWORD InfSectionWithExtSize,
  _Out_opt_  PDWORD RequiredSize,
  _Out_opt_  PTSTR *Extension
);
BOOL SetupDiGetActualSectionToInstallEx(
  _In_        HINF InfHandle,
  _In_        PCTSTR InfSectionName,
  _In_opt_    PSP_ALTPLATFORM_INFO AlternatePlatformInfo,
  _Out_opt_   PTSTR InfSectionWithExt,
  _In_        DWORD InfSectionWithExtSize,
  _Out_opt_   PDWORD RequiredSize,
  _Out_opt_   PTSTR *Extension,
  _Reserved_  PVOID Reserved
);
BOOL SetupDiGetClassBitmapIndex(
  _In_opt_  const GUID *ClassGuid,
  _Out_     PINT MiniIconIndex
);
BOOL SetupDiGetClassDescription(
  _In_       const GUID *ClassGuid,
  _Out_      PTSTR ClassDescription,
  _In_       DWORD ClassDescriptionSize,
  _Out_opt_  PDWORD RequiredSize
);
BOOL SetupDiGetClassDescriptionEx(
  _In_        const GUID *ClassGuid,
  _Out_       PTSTR ClassDescription,
  _In_        DWORD ClassDescriptionSize,
  _Out_opt_   PDWORD RequiredSize,
  _In_opt_    PCTSTR MachineName,
  _Reserved_  PVOID Reserved
);
BOOL SetupDiGetClassDevPropertySheets(
  _In_       HDEVINFO DeviceInfoSet,
  _In_opt_   PSP_DEVINFO_DATA DeviceInfoData,
  _In_       LPPROPSHEETHEADER PropertySheetHeader,
  _In_       DWORD PropertySheetHeaderPageListSize,
  _Out_opt_  PDWORD RequiredSize,
  _In_       DWORD PropertySheetType
);
"""
"""
HDEVINFO SetupDiGetClassDevs(
  _In_opt_  const GUID *ClassGuid,
  _In_opt_  PCTSTR Enumerator,
  _In_opt_  HWND hwndParent,
  _In_      DWORD Flags
);
"""
SetupDiGetClassDevs = ctypes.windll.setupapi.SetupDiGetClassDevsW
SetupDiGetClassDevs.restype = HDEVINFO
SetupDiGetClassDevs.argtypes = [
                                PGUID,
                                PCTSTR,
                                HWND,
                                DWORD
                                ]
"""Flags enum"""
DIGCF_ALLCLASSES      = 0x00000001
DIGCF_DEVICEINTERFACE = 0x00000002
DIGCF_DEFAULT         = 0x00000004
DIGCF_PRESENT         = 0x00000008
DIGCF_PROFILE         = 0x00000010
"""
HDEVINFO SetupDiGetClassDevsEx(
  _In_opt_    const GUID *ClassGuid,
  _In_opt_    PCTSTR Enumerator,
  _In_opt_    HWND hwndParent,
  _In_        DWORD Flags,
  _In_opt_    HDEVINFO DeviceInfoSet,
  _In_opt_    PCTSTR MachineName,
  _Reserved_  PVOID Reserved
);
BOOL SetupDiGetClassImageIndex(
  _In_   PSP_CLASSIMAGELIST_DATA ClassImageListData,
  _In_   const GUID *ClassGuid,
  _Out_  PINT ImageIndex
);
BOOL SetupDiGetClassImageList(
  _Out_  PSP_CLASSIMAGELIST_DATA ClassImageListData
);
BOOL SetupDiGetClassImageListEx(
  _Out_       PSP_CLASSIMAGELIST_DATA ClassImageListData,
  _In_opt_    PCTSTR MachineName,
  _Reserved_  PVOID Reserved
);
BOOL SetupDiGetClassInstallParams(
  _In_       HDEVINFO DeviceInfoSet,
  _In_opt_   PSP_DEVINFO_DATA DeviceInfoData,
  _Out_opt_  PSP_CLASSINSTALL_HEADER ClassInstallParams,
  _In_       DWORD ClassInstallParamsSize,
  _Out_opt_  PDWORD RequiredSize
);
BOOL SetupDiGetClassProperty(
  _In_       const GUID *ClassGuid,
  _In_       const DEVPROPKEY *PropertyKey,
  _Out_      DEVPROPTYPE *PropertyType,
  _Out_      PBYTE PropertyBuffer,
  _In_       DWORD PropertyBufferSize,
  _Out_opt_  PDWORD RequiredSize,
  _In_       DWORD Flags
);
BOOL SetupDiGetClassPropertyEx(
  _In_        const GUID *ClassGuid,
  _In_        const DEVPROPKEY *PropertyKey,
  _Out_       DEVPROPTYPE *PropertyType,
  _Out_opt_   PBYTE PropertyBuffer,
  _In_        DWORD PropertyBufferSize,
  _Out_opt_   PDWORD RequiredSize,
  _In_        DWORD Flags,
  _In_opt_    PCTSTR MachineName,
  _Reserved_  PVOID Reserved
);
BOOL SetupDiGetClassPropertyKeys(
  _In_       const GUID *ClassGuid,
  _Out_opt_  DEVPROPKEY *PropertyKeyArray,
  _In_       DWORD PropertyKeyCount,
  _Out_opt_  PDWORD RequiredPropertyKeyCount,
  _In_       DWORD Flags
);
BOOL SetupDiGetClassPropertyKeysEx(
  _In_        const GUID *ClassGuid,
  _Out_opt_   DEVPROPKEY *PropertyKeyArray,
  _In_        DWORD PropertyKeyCount,
  _Out_opt_   PDWORD RequiredPropertyKeyCount,
  _In_        DWORD Flags,
  _In_opt_    PCTSTR MachineName,
  _Reserved_  PVOID Reserved
);
BOOL SetupDiGetClassRegistryProperty(
  _In_        const GUID *ClassGuid,
  _In_        DWORD Property,
  _Out_opt_   PDWORD PropertyRegDataType,
  _Out_       PBYTE PropertyBuffer,
  _In_        DWORD PropertyBufferSize,
  _Out_opt_   PDWORD RequiredSize,
  _In_opt_    PCTSTR MachineName,
  _Reserved_  PVOID Reserved
);
BOOL SetupDiGetCustomDeviceProperty(
  _In_       HDEVINFO DeviceInfoSet,
  _In_       PSP_DEVINFO_DATA DeviceInfoData,
  _In_       PCTSTR CustomPropertyName,
  _In_       DWORD Flags,
  _Out_opt_  PDWORD PropertyRegDataType,
  _Out_      PBYTE PropertyBuffer,
  _In_       DWORD PropertyBufferSize,
  _Out_opt_  PDWORD RequiredSize
);
BOOL SetupDiGetDeviceInfoListClass(
  _In_   HDEVINFO DeviceInfoSet,
  _Out_  LPGUID ClassGuid
);
BOOL SetupDiGetDeviceInfoListDetail(
  _In_   HDEVINFO DeviceInfoSet,
  _Out_  PSP_DEVINFO_LIST_DETAIL_DATA DeviceInfoSetDetailData
);
BOOL SetupDiGetDeviceInstallParams(
  _In_      HDEVINFO DeviceInfoSet,
  _In_opt_  PSP_DEVINFO_DATA DeviceInfoData,
  _Out_     PSP_DEVINSTALL_PARAMS DeviceInstallParams
);
"""
"""
BOOL SetupDiGetDeviceInstanceId(
  _In_       HDEVINFO DeviceInfoSet,
  _In_       PSP_DEVINFO_DATA DeviceInfoData,
  _Out_opt_  PTSTR DeviceInstanceId,
  _In_       DWORD DeviceInstanceIdSize,
  _Out_opt_  PDWORD RequiredSize
);
"""
SetupDiGetDeviceInstanceId = ctypes.windll.setupapi.SetupDiGetDeviceInstanceIdW
SetupDiGetDeviceInstanceId.restype = BOOL
SetupDiGetDeviceInstanceId.argtypes = [
                                       HDEVINFO,
                                       PSP_DEVINFO_DATA,
                                       PTSTR,
                                       DWORD,
                                       PDWORD
                                       ]
"""
BOOL SetupDiGetDeviceInterfaceAlias(
  _In_   HDEVINFO DeviceInfoSet,
  _In_   PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
  _In_   const GUID *AliasInterfaceClassGuid,
  _Out_  PSP_DEVICE_INTERFACE_DATA AliasDeviceInterfaceData
);
"""
"""
BOOL SetupDiGetDeviceInterfaceDetail(
  _In_       HDEVINFO DeviceInfoSet,
  _In_       PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
  _Out_opt_  PSP_DEVICE_INTERFACE_DETAIL_DATA DeviceInterfaceDetailData,
  _In_       DWORD DeviceInterfaceDetailDataSize,
  _Out_opt_  PDWORD RequiredSize,
  _Out_opt_  PSP_DEVINFO_DATA DeviceInfoData
);
"""
SetupDiGetDeviceInterfaceDetail = ctypes.windll.setupapi.SetupDiGetDeviceInterfaceDetailW
SetupDiGetDeviceInterfaceDetail.restype = BOOL
SetupDiGetDeviceInterfaceDetail.argtypes = [
                                            HDEVINFO,
                                            PSP_DEVICE_INTERFACE_DATA,
                                            PSP_DEVICE_INTERFACE_DETAIL_DATA,
                                            DWORD,
                                            PDWORD,
                                            PSP_DEVINFO_DATA
                                            ]
"""
BOOL SetupDiGetDeviceInterfaceProperty(
  _In_       HDEVINFO DeviceInfoSet,
  _In_       PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
  _In_       const DEVPROPKEY *PropertyKey,
  _Out_      DEVPROPTYPE *PropertyType,
  _Out_      PBYTE PropertyBuffer,
  _In_       DWORD PropertyBufferSize,
  _Out_opt_  PDWORD RequiredSize,
  _In_       DWORD Flags
);
BOOL SetupDiGetDeviceInterfacePropertyKeys(
  _In_       HDEVINFO DeviceInfoSet,
  _In_       PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
  _Out_opt_  DEVPROPKEY *PropertyKeyArray,
  _In_       DWORD PropertyKeyCount,
  _Out_opt_  PDWORD RequiredPropertyKeyCount,
  _In_       DWORD Flags
);
BOOL SetupDiGetDeviceProperty(
  _In_       HDEVINFO DeviceInfoSet,
  _In_       PSP_DEVINFO_DATA DeviceInfoData,
  _In_       const DEVPROPKEY *PropertyKey,
  _Out_      DEVPROPTYPE *PropertyType,
  _Out_opt_  PBYTE PropertyBuffer,
  _In_       DWORD PropertyBufferSize,
  _Out_opt_  PDWORD RequiredSize,
  _In_       DWORD Flags
);
BOOL SetupDiGetDevicePropertyKeys(
  _In_       HDEVINFO DeviceInfoSet,
  _In_       PSP_DEVINFO_DATA DeviceInfoData,
  _Out_opt_  DEVPROPKEY *PropertyKeyArray,
  _In_       DWORD PropertyKeyCount,
  _Out_opt_  PDWORD RequiredPropertyKeyCount,
  _In_       DWORD Flags
);
"""
"""
BOOL SetupDiGetDeviceRegistryProperty(
  _In_       HDEVINFO DeviceInfoSet,
  _In_       PSP_DEVINFO_DATA DeviceInfoData,
  _In_       DWORD Property,
  _Out_opt_  PDWORD PropertyRegDataType,
  _Out_opt_  PBYTE PropertyBuffer,
  _In_       DWORD PropertyBufferSize,
  _Out_opt_  PDWORD RequiredSize
);
"""
SetupDiGetDeviceRegistryProperty = ctypes.windll.setupapi.SetupDiGetDeviceRegistryPropertyW
SetupDiGetDeviceRegistryProperty.restype  = BOOL
SetupDiGetDeviceRegistryProperty.argtypes = [
    HDEVINFO,
    PSP_DEVINFO_DATA,
    DWORD,
    PDWORD,
    PBYTE,
    DWORD,
    PDWORD,
    ]
SPDRP_DEVICEDESC                  = (0x00000000)  #// DeviceDesc (R/W)               
SPDRP_HARDWAREID                  = (0x00000001)  #// HardwareID (R/W)               
SPDRP_COMPATIBLEIDS               = (0x00000002)  #// CompatibleIDs (R/W)            
SPDRP_UNUSED0                     = (0x00000003)  #// unused
SPDRP_SERVICE                     = (0x00000004)  #// Service (R/W)                  
SPDRP_UNUSED1                     = (0x00000005)  #// unused
SPDRP_UNUSED2                     = (0x00000006)  #// unused
SPDRP_CLASS                       = (0x00000007)  #// Class (R--tied to ClassGUID)   
SPDRP_CLASSGUID                   = (0x00000008)  #// ClassGUID (R/W)                
SPDRP_DRIVER                      = (0x00000009)  #// Driver (R/W)                   
SPDRP_CONFIGFLAGS                 = (0x0000000A)  #// ConfigFlags (R/W)
SPDRP_MFG                         = (0x0000000B)  #// Mfg (R/W)                      
SPDRP_FRIENDLYNAME                = (0x0000000C)  #// FriendlyName (R/W)
SPDRP_LOCATION_INFORMATION        = (0x0000000D)  #// LocationInformation (R/W)      
SPDRP_PHYSICAL_DEVICE_OBJECT_NAME = (0x0000000E)  #// PhysicalDeviceObjectName (R)   
SPDRP_CAPABILITIES                = (0x0000000F)  #// Capabilities (R)
SPDRP_UI_NUMBER                   = (0x00000010)  #// UiNumber (R)
SPDRP_UPPERFILTERS                = (0x00000011)  #// UpperFilters (R/W)
SPDRP_LOWERFILTERS                = (0x00000012)  #// LowerFilters (R/W)
SPDRP_BUSTYPEGUID                 = (0x00000013)  #// BusTypeGUID (R)                
SPDRP_LEGACYBUSTYPE               = (0x00000014)  #// LegacyBusType (R)              
SPDRP_BUSNUMBER                   = (0x00000015)  #// BusNumber (R)
SPDRP_ENUMERATOR_NAME             = (0x00000016)  #// Enumerator Name (R)            
SPDRP_SECURITY                    = (0x00000017)  #// Security (R/W, binary form)
SPDRP_SECURITY_SDS                = (0x00000018)  #// Security (W, SDS form)
SPDRP_DEVTYPE                     = (0x00000019)  #// Device Type (R/W)
SPDRP_EXCLUSIVE                   = (0x0000001A)  #// Device is exclusive-access (R/W)
SPDRP_CHARACTERISTICS             = (0x0000001B)  #// Device Characteristics (R/W)
SPDRP_ADDRESS                     = (0x0000001C)  #// Device Address (R)             
SPDRP_UI_NUMBER_DESC_FORMAT       = (0X0000001D)  #// UiNumberDescFormat (R/W)
SPDRP_DEVICE_POWER_DATA           = (0x0000001E)  #// Device Power Data (R)          
SPDRP_REMOVAL_POLICY              = (0x0000001F)  #// Removal Policy (R)             
SPDRP_REMOVAL_POLICY_HW_DEFAULT   = (0x00000020)  #// Hardware Removal Policy (R)    
SPDRP_REMOVAL_POLICY_OVERRIDE     = (0x00000021)  #// Removal Policy Override (RW)
SPDRP_INSTALL_STATE               = (0x00000022)  #// Device Install State (R)
SPDRP_LOCATION_PATHS              = (0x00000023)  #// Device Location Paths (R)
SPDRP_BASE_CONTAINERID            = (0x00000024)  #// Base ContainerID (R)
list_SPDRP_Property = ('SPDRP_DEVICEDESC',
                       'SPDRP_HARDWAREID',
                       'SPDRP_COMPATIBLEIDS',
                       'SPDRP_UNUSED0',
                       'SPDRP_SERVICE',
                       'SPDRP_UNUSED1',
                       'SPDRP_UNUSED2',
                       'SPDRP_CLASS',
                       'SPDRP_CLASSGUID',
                       'SPDRP_DRIVER',
                       'SPDRP_CONFIGFLAGS',
                       'SPDRP_MFG',
                       'SPDRP_FRIENDLYNAME',
                       'SPDRP_LOCATION_INFORMATION',
                       'SPDRP_PHYSICAL_DEVICE_OBJECT_NAME',
                       'SPDRP_CAPABILITIES',
                       'SPDRP_UI_NUMBER',
                       'SPDRP_UPPERFILTERS',
                       'SPDRP_LOWERFILTERS',
                       'SPDRP_BUSTYPEGUID',
                       'SPDRP_LEGACYBUSTYPE',
                       'SPDRP_BUSNUMBER',
                       'SPDRP_ENUMERATOR_NAME',
                       'SPDRP_SECURITY',
                       'SPDRP_SECURITY_SDS',
                       'SPDRP_DEVTYPE',
                       'SPDRP_EXCLUSIVE',
                       'SPDRP_CHARACTERISTICS',
                       'SPDRP_ADDRESS',
                       'SPDRP_UI_NUMBER_DESC_FORMAT',
                       'SPDRP_DEVICE_POWER_DATA',
                       'SPDRP_REMOVAL_POLICY',
                       'SPDRP_REMOVAL_POLICY_HW_DEFAULT',
                       'SPDRP_REMOVAL_POLICY_OVERRIDE',
                       'SPDRP_INSTALL_STATE',
                       'SPDRP_LOCATION_PATHS',
                       'SPDRP_BASE_CONTAINERID'
                       )
list_RegType = ('DOWRD'        , #//0 
                'REG_SZ'       , #//1
                'XXX'          , #//2
                'CM_POWER_DATA', #//3
                'DWORD'        , #//4
                'XXX'          , #//5
                'XXX'          , #//6
                'REG_MULTI_SZ'   #//7
                )
CM_DEVCAP_LOCKSUPPORTED      = 0x00000001
CM_DEVCAP_EJECTSUPPORTED     = 0x00000002
CM_DEVCAP_REMOVABLE          = 0x00000004
CM_DEVCAP_DOCKDEVICE         = 0x00000008
CM_DEVCAP_UNIQUEID           = 0x00000010
CM_DEVCAP_SILENTINSTALL      = 0x00000020
CM_DEVCAP_RAWDEVICEOK        = 0x00000040
CM_DEVCAP_SURPRISEREMOVALOK  = 0x00000080
CM_DEVCAP_HARDWAREDISABLED   = 0x00000100
CM_DEVCAP_NONDYNAMIC         = 0x00000200

def Parse_CM_DEVCAP(cm_devcap):
    result = ""
    prefix = ""
    if cm_devcap & CM_DEVCAP_LOCKSUPPORTED: 
        result += prefix + "CM_DEVCAP_LOCKSUPPORTED"
        prefix = "|"
    if cm_devcap & CM_DEVCAP_EJECTSUPPORTED: 
        result += prefix + "CM_DEVCAP_EJECTSUPPORTED"
        prefix = "|"
    if cm_devcap & CM_DEVCAP_REMOVABLE: 
        result += prefix + "CM_DEVCAP_REMOVABLE"
        prefix = "|"
    if cm_devcap & CM_DEVCAP_DOCKDEVICE: 
        result += prefix + "CM_DEVCAP_DOCKDEVICE"
        prefix = "|"
    if cm_devcap & CM_DEVCAP_UNIQUEID: 
        result += prefix + "CM_DEVCAP_UNIQUEID"
        prefix = "|"
    if cm_devcap & CM_DEVCAP_SILENTINSTALL: 
        result += prefix + "CM_DEVCAP_SILENTINSTALL"
        prefix = "|"
    if cm_devcap & CM_DEVCAP_RAWDEVICEOK: 
        result += prefix + "CM_DEVCAP_RAWDEVICEOK"
        prefix = "|"
    if cm_devcap & CM_DEVCAP_SURPRISEREMOVALOK: 
        result += prefix + "CM_DEVCAP_SURPRISEREMOVALOK"
        prefix = "|"
    if cm_devcap & CM_DEVCAP_HARDWAREDISABLED: 
        result += prefix + "CM_DEVCAP_HARDWAREDISABLED"
        prefix = "|"
    if cm_devcap & CM_DEVCAP_NONDYNAMIC: 
        result += prefix + "CM_DEVCAP_NONDYNAMIC"
        prefix = "|"
    return result
"""
BOOL SetupDiGetDriverInfoDetail(
  _In_       HDEVINFO DeviceInfoSet,
  _In_opt_   PSP_DEVINFO_DATA DeviceInfoData,
  _In_       PSP_DRVINFO_DATA DriverInfoData,
  _Inout_    PSP_DRVINFO_DETAIL_DATA DriverInfoDetailData,
  _In_       DWORD DriverInfoDetailDataSize,
  _Out_opt_  PDWORD RequiredSize
);
BOOL SetupDiGetDriverInstallParams(
  _In_      HDEVINFO DeviceInfoSet,
  _In_opt_  PSP_DEVINFO_DATA DeviceInfoData,
  _In_      PSP_DRVINFO_DATA DriverInfoData,
  _Out_     PSP_DRVINSTALL_PARAMS DriverInstallParams
);
BOOL SetupDiGetHwProfileFriendlyName(
  _In_       DWORD HwProfile,
  _Out_      PSTR FriendlyName,
  _In_       DWORD FriendlyNameSize,
  _Out_opt_  PDWORD RequiredSize
);
BOOL SetupDiGetHwProfileFriendlyNameEx(
  _In_        DWORD HwProfile,
  _Out_       PTSTR FriendlyName,
  _In_        DWORD FriendlyNameSize,
  _Out_opt_   PDWORD RequiredSize,
  _In_opt_    PCTSTR MachineName,
  _Reserved_  PVOID Reserved
);
BOOL SetupDiGetHwProfileList(
  _Out_      PDWORD HwProfileList,
  _In_       DWORD HwProfileListSize,
  _Out_      PDWORD RequiredSize,
  _Out_opt_  PDWORD CurrentlyActiveIndex
);
BOOL SetupDiGetHwProfileListEx(
  _Out_       PDWORD HwProfileList,
  _In_        DWORD HwProfileListSize,
  _Out_       PDWORD RequiredSize,
  _Out_opt_   PDWORD CurrentlyActiveIndex,
  _In_opt_    PCTSTR MachineName,
  _Reserved_  PVOID Reserved
);
BOOL SetupDiGetINFClass(
  _In_       PCTSTR InfName,
  _Out_      LPGUID ClassGuid,
  _Out_      PTSTR ClassName,
  _In_       DWORD ClassNameSize,
  _Out_opt_  PDWORD RequiredSize
);
BOOL SetupDiGetSelectedDevice(
  _In_   HDEVINFO DeviceInfoSet,
  _Out_  PSP_DEVINFO_DATA DeviceInfoData
);
BOOL SetupDiGetSelectedDriver(
  _In_      HDEVINFO DeviceInfoSet,
  _In_opt_  PSP_DEVINFO_DATA DeviceInfoData,
  _Out_     PSP_DRVINFO_DATA DriverInfoData
);
HPROPSHEETPAGE
 SetupDiGetWizardPage(
 IN HDEVINFO DeviceInfoSet, 
 IN PSP_DEVINFO_DATA DeviceInfoData..OPTIONAL,
 IN PSP_INSTALLWIZARD_DATA InstallWizardData,
 IN DWORD PageType,
    IN DWORD Flags
 );
 BOOL SetupDiInstallClass(
  _In_opt_  HWND hwndParent,
  _In_      PCTSTR InfFileName,
  _In_      DWORD Flags,
  _In_opt_  HSPFILEQ FileQueue
);
BOOL SetupDiInstallClassEx(
  _In_opt_    HWND hwndParent,
  _In_opt_    PCTSTR InfFileName,
  _In_        DWORD Flags,
  _In_opt_    HSPFILEQ FileQueue,
  _In_opt_    const GUID *InterfaceClassGuid,
  _Reserved_  PVOID Reserved1,
  _Reserved_  PVOID Reserved2
);
BOOL SetupDiInstallDevice(
  _In_     HDEVINFO DeviceInfoSet,
  _Inout_  PSP_DEVINFO_DATA DeviceInfoData
);
BOOL SetupDiInstallDeviceInterfaces(
  _In_  HDEVINFO DeviceInfoSet,
  _In_  PSP_DEVINFO_DATA DeviceInfoData
);
BOOL SetupDiInstallDriverFiles(
  _In_  HDEVINFO DeviceInfoSet,
  _In_  PSP_DEVINFO_DATA DeviceInfoData
);
BOOL SetupDiLoadClassIcon(
  _In_       const GUID *ClassGuid,
  _Out_opt_  HICON *LargeIcon,
  _Out_opt_  PINT MiniIconIndex
);
BOOL SetupDiLoadDeviceIcon(
  _In_   HDEVINFO DeviceInfoSet,
  _In_   PSP_DEVINFO_DATA DeviceInfoData,
  _In_   UINT cxIcon,
  _In_   UINT cyIcon,
  _In_   DWORD Flags,
  _Out_  HICON *hIcon
);
HKEY SetupDiOpenClassRegKey(
  _In_opt_  const GUID *ClassGuid,
  _In_      REGSAM samDesired
);
HKEY SetupDiOpenClassRegKeyEx(
  _In_opt_    const GUID *ClassGuid,
  _In_        REGSAM samDesired,
  _In_        DWORD Flags,
  _In_opt_    PCTSTR MachineName,
  _Reserved_  PVOID Reserved
);
BOOL SetupDiOpenDeviceInfo(
  _In_       HDEVINFO DeviceInfoSet,
  _In_       PCTSTR DeviceInstanceId,
  _In_opt_   HWND hwndParent,
  _In_       DWORD OpenFlags,
  _Out_opt_  PSP_DEVINFO_DATA DeviceInfoData
);
BOOL SetupDiOpenDeviceInterface(
  _In_       HDEVINFO DeviceInfoSet,
  _In_       PCTSTR DevicePath,
  _In_       DWORD OpenFlags,
  _Out_opt_  PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData
);
HKEY SetupDiOpenDeviceInterfaceRegKey(
  _In_        HDEVINFO DeviceInfoSet,
  _In_        PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
  _Reserved_  DWORD Reserved,
  _In_        REGSAM samDesired
);
HKEY SetupDiOpenDevRegKey(
  _In_  HDEVINFO DeviceInfoSet,
  _In_  PSP_DEVINFO_DATA DeviceInfoData,
  _In_  DWORD Scope,
  _In_  DWORD HwProfile,
  _In_  DWORD KeyType,
  _In_  REGSAM samDesired
);
BOOL SetupDiRegisterCoDeviceInstallers(
  _In_  HDEVINFO DeviceInfoSet,
  _In_  PSP_DEVINFO_DATA DeviceInfoData
);
BOOL SetupDiRegisterDeviceInfo(
  _In_       HDEVINFO DeviceInfoSet,
  _Inout_    PSP_DEVINFO_DATA DeviceInfoData,
  _In_       DWORD Flags,
  _In_opt_   PSP_DETSIG_CMPPROC CompareProc,
  _In_opt_   PVOID CompareContext,
  _Out_opt_  PSP_DEVINFO_DATA DupDeviceInfoData
);
BOOL SetupDiRemoveDevice(
  _In_     HDEVINFO DeviceInfoSet,
  _Inout_  PSP_DEVINFO_DATA DeviceInfoData
);
BOOL SetupDiRemoveDeviceInterface(
  _In_     HDEVINFO DeviceInfoSet,
  _Inout_  PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData
);
BOOL SetupDiRestartDevices(
  _In_     HDEVINFO DeviceInfoSet,
  _Inout_  PSP_DEVINFO_DATA DeviceInfoData
);
BOOL SetupDiSelectBestCompatDrv(
  _In_     HDEVINFO DeviceInfoSet,
  _Inout_  PSP_DEVINFO_DATA DeviceInfoData
);
BOOL SetupDiSelectDevice(
  _In_     HDEVINFO DeviceInfoSet,
  _Inout_  PSP_DEVINFO_DATA DeviceInfoData
);
BOOL SetupDiSelectOEMDrv(
  _In_opt_  HWND hwndParent,
  _In_      HDEVINFO DeviceInfoSet,
  _Inout_   PSP_DEVINFO_DATA DeviceInfoData
);
BOOL SetupDiSetClassInstallParams(
  _In_      HDEVINFO DeviceInfoSet,
  _In_opt_  PSP_DEVINFO_DATA DeviceInfoData,
  _In_opt_  PSP_CLASSINSTALL_HEADER ClassInstallParams,
  _In_      DWORD ClassInstallParamsSize
);
BOOL SetupDiSetClassProperty(
  _In_      const GUID *ClassGuid,
  _In_      const DEVPROPKEY *PropertyKey,
  _In_      DEVPROPTYPE PropertyType,
  _In_opt_  const PBYTE PropertyBuffer,
  _In_      DWORD PropertyBufferSize,
  _In_      DWORD Flags
);
BOOL SetupDiSetClassPropertyEx(
  _In_        const GUID *ClassGuid,
  _In_        const DEVPROPKEY *PropertyKey,
  _In_        DEVPROPTYPE PropertyType,
  _In_opt_    const PBYTE PropertyBuffer,
  _In_        DWORD PropertyBufferSize,
  _In_        DWORD Flags,
  _In_opt_    PCTSTR MachineName,
  _Reserved_  PVOID Reserved
);
BOOL SetupDiSetClassRegistryProperty(
  _In_        const GUID *ClassGuid,
  _In_        DWORD Property,
  _In_opt_    const BYTE *PropertyBuffer,
  _In_        DWORD PropertyBufferSize,
  _In_opt_    PCTSTR MachineName,
  _Reserved_  PVOID Reserved
);
BOOL SetupDiSetDeviceInstallParams(
  _In_      HDEVINFO DeviceInfoSet,
  _In_opt_  PSP_DEVINFO_DATA DeviceInfoData,
  _In_      PSP_DEVINSTALL_PARAMS DeviceInstallParams
);
BOOL SetupDiSetDeviceInterfaceDefault(
  _In_        HDEVINFO DeviceInfoSet,
  _Inout_     PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
  _In_        DWORD Flags,
  _Reserved_  PVOID Reserved
);
BOOL SetupDiSetDeviceInterfaceProperty(
  _In_      HDEVINFO DeviceInfoSet,
  _In_      PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
  _In_      const DEVPROPKEY *PropertyKey,
  _In_      DEVPROPTYPE PropertyType,
  _In_opt_  const PBYTE PropertyBuffer,
  _In_      DWORD PropertyBufferSize,
  _In_      DWORD Flags
);
BOOL SetupDiSetDeviceProperty(
  _In_      HDEVINFO DeviceInfoSet,
  _In_      PSP_DEVINFO_DATA DeviceInfoData,
  _In_      const DEVPROPKEY *PropertyKey,
  _In_      DEVPROPTYPE PropertyType,
  _In_opt_  const PBYTE PropertyBuffer,
  _In_      DWORD PropertyBufferSize,
  _In_      DWORD Flags
);
BOOL SetupDiSetDeviceRegistryProperty(
  _In_      HDEVINFO DeviceInfoSet,
  _Inout_   PSP_DEVINFO_DATA DeviceInfoData,
  _In_      DWORD Property,
  _In_opt_  const BYTE *PropertyBuffer,
  _In_      DWORD PropertyBufferSize
);
BOOL SetupDiSetDriverInstallParams(
  _In_      HDEVINFO DeviceInfoSet,
  _In_opt_  PSP_DEVINFO_DATA DeviceInfoData,
  _In_      PSP_DRVINFO_DATA DriverInfoData,
  _In_      PSP_DRVINSTALL_PARAMS DriverInstallParams
);
BOOL SetupDiSetSelectedDevice(
  _In_  HDEVINFO DeviceInfoSet,
  _In_  PSP_DEVINFO_DATA DeviceInfoData
);
BOOL SetupDiSetSelectedDriver(
  _In_     HDEVINFO DeviceInfoSet,
  _Inout_  PSP_DEVINFO_DATA DeviceInfoData,
  _Inout_  PSP_DRVINFO_DATA DriverInfoData
);
BOOL SetupDiUnremoveDevice(
  _In_     HDEVINFO DeviceInfoSet,
  _Inout_  PSP_DEVINFO_DATA DeviceInfoData
);
BOOL UpdateDriverForPlugAndPlayDevices(
  _In_opt_   HWND hwndParent,
  _In_       LPCTSTR HardwareId,
  _In_       LPCTSTR FullInfPath,
  _In_       DWORD InstallFlags,
  _Out_opt_  PBOOL bRebootRequired
);
"""
"""
CMAPI
CONFIGRET
WINAPI CM_Get_Parent(
  _Out_  PDEVINST pdnDevInst,
  _In_   DEVINST dnDevInst ,
  _In_   ULONG ulFlags
);
"""