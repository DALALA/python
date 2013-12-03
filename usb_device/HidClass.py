'''
Created on 2013/9/13

@author: RobertChen
'''
import WinDataType 
from WinDataType import *
"""
typedef struct _HID_COLLECTION_INFORMATION {
  ULONG   DescriptorSize;
  BOOLEAN Polled;
  UCHAR   Reserved1[1];
  USHORT  VendorID;
  USHORT  ProductID;
  USHORT  VersionNumber;
} HID_COLLECTION_INFORMATION, *PHID_COLLECTION_INFORMATION;
"""
"""
typedef struct _HIDD_ATTRIBUTES {
  ULONG  Size;
  USHORT VendorID;
  USHORT ProductID;
  USHORT VersionNumber;
} HIDD_ATTRIBUTES, *PHIDD_ATTRIBUTES;
"""
class HIDD_ATTRIBUTES(Structure):
    _fields_ = [("Size"         , ULONG),
                ("VendorID"     , USHORT),
                ("ProductID"    , USHORT),
                ("VersionNumber", USHORT)
                ]
    def __str__(self):
        return "HIDD_ATTRIBUTES:Size:%d VendorID:0x%x ProductID:0x%x VersionNumber:0x%x" % (self.Size,self.VendorID,self.ProductID,self.VersionNumber)

PHIDD_ATTRIBUTES = POINTER(HIDD_ATTRIBUTES)
"""
typedef struct _HIDP_BUTTON_CAPS {
  USAGE   UsagePage;
  UCHAR   ReportID;
  BOOLEAN IsAlias;
  USHORT  BitField;
  USHORT  LinkCollection;
  USAGE   LinkUsage;
  USAGE   LinkUsagePage;
  BOOLEAN IsRange;
  BOOLEAN IsStringRange;
  BOOLEAN IsDesignatorRange;
  BOOLEAN IsAbsolute;
  ULONG   Reserved[10];
  union {
    struct {
      USAGE  UsageMin;
      USAGE  UsageMax;
      USHORT StringMin;
      USHORT StringMax;
      USHORT DesignatorMin;
      USHORT DesignatorMax;
      USHORT DataIndexMin;
      USHORT DataIndexMax;
    } Range;
    struct {
      USAGE  Usage;
      USAGE  Reserved1;
      USHORT StringIndex;
      USHORT Reserved2;
      USHORT DesignatorIndex;
      USHORT Reserved3;
      USHORT DataIndex;
      USHORT Reserved4;
    } NotRange;
  };
} HIDP_BUTTON_CAPS, *PHIDP_BUTTON_CAPS;
"""
class TypeRange(Structure):
    _fields_ = [\
               ("UsageMin"     , USAGE),
               ("UsageMax"     , USAGE),
               ("StringMin"    , USHORT),
               ("StringMax"    , USHORT),
               ("DesignatorMin", USHORT),
               ("DesignatorMax", USHORT),
               ("DataIndexMin" , USHORT),
               ("DataIndexMax" , USHORT)
               ]

class TypeNotRange(Structure):
    _fields_ = [\
               ("Usage"          , USAGE),
               ("Reserved1"      , USAGE),
               ("StringIndex"    , USHORT),
               ("Reserved2"      , USHORT),
               ("DesignatorIndex", USHORT),
               ("Reserved3"      , USHORT),
               ("DataIndex"      , USHORT),
               ("Reserved4"      , USHORT),
               ]

class TypeRangeUnionNotRange(Union):
    _fields_ = [\
               ("Range"   , TypeRange),
               ("NotRange", TypeNotRange)
               ]

class HIDP_BUTTON_CAPS(Structure):
    _fields_ = [\
                ("UsagePage"         , USAGE),
                ("ReportID"          , UCHAR),
                ("IsAlias"           , BOOLEAN),
                ("BitField"          , USHORT),
                ("LinkCollection"    , USHORT),
                ("LinkUsage"         , USAGE),
                ("LinkUsagePage"     , USAGE),
                ("IsRange"           , BOOLEAN),
                ("IsStringRange"     , BOOLEAN),
                ("IsDesignatorRange" , BOOLEAN),
                ("IsAbsolute"        , BOOLEAN),
                ("Reserved"          , ULONG*10),
                ("RangeUnionNotRange", TypeRangeUnionNotRange)
               ]
PHIDP_BUTTON_CAPS = POINTER(HIDP_BUTTON_CAPS)
"""
typedef struct _HIDP_CAPS {
  USAGE  Usage;
  USAGE  UsagePage;
  USHORT InputReportByteLength;
  USHORT OutputReportByteLength;
  USHORT FeatureReportByteLength;
  USHORT Reserved[17];
  USHORT NumberLinkCollectionNodes;
  USHORT NumberInputButtonCaps;
  USHORT NumberInputValueCaps;
  USHORT NumberInputDataIndices;
  USHORT NumberOutputButtonCaps;
  USHORT NumberOutputValueCaps;
  USHORT NumberOutputDataIndices;
  USHORT NumberFeatureButtonCaps;
  USHORT NumberFeatureValueCaps;
  USHORT NumberFeatureDataIndices;
} HIDP_CAPS, *PHIDP_CAPS;
"""
class HIDP_CAPS(Structure):
    _fields_ = [\
               ("Usage"                    , USAGE),
               ("UsagePage"                , USAGE),
               ("InputReportByteLength"    , USHORT),
               ("OutputReportByteLength"   , USHORT),
               ("FeatureReportByteLength"  , USHORT),
               ("Reserved"                 , USHORT*17),
               ("NumberLinkCollectionNodes", USHORT),
               ("NumberInputButtonCaps"    , USHORT),
               ("NumberInputValueCaps"     , USHORT),
               ("NumberInputDataIndices"   , USHORT),
               ("NumberOutputButtonCaps"   , USHORT),
               ("NumberOutputValueCaps"    , USHORT),
               ("NumberOutputDataIndices"  , USHORT),
               ("NumberFeatureButtonCaps"  , USHORT),
               ("NumberFeatureValueCaps"   , USHORT),
               ("NumberFeatureDataIndices" , USHORT)
               ]
PHIDP_CAPS = POINTER(HIDP_CAPS)
"""
typedef struct _HIDP_DATA {
  USHORT DataIndex;
  USHORT Reserved;
  union {
    ULONG   RawValue;
    BOOLEAN On;
  };
} HIDP_DATA, *PHIDP_DATA;
"""
class HIDP_DATA(Structure):
    class TypeControlData(Union):
        _fields_ = [\
                   ("RawValue", ULONG),
                   ("On"      , BOOLEAN)
                   ]
    _fields_ = [\
               ("DataIndex"       , USHORT),
               ("Reserved"        , USHORT),
               ("UnionControlData", TypeControlData)
               ]

"""
typedef struct _HIDP_EXTENDED_ATTRIBUTES {
  UCHAR               NumGlobalUnknowns;
  UCHAR               Reserved[3];
  PHIDP_UNKNOWN_TOKEN GlobalUnknowns;
  ULONG               Data[1];
} HIDP_EXTENDED_ATTRIBUTES, *PHIDP_EXTENDED_ATTRIBUTES;
typedef struct _HIDP_LINK_COLLECTION_NODE {
  USAGE  LinkUsage;
  USAGE  LinkUsagePage;
  USHORT Parent;
  USHORT NumberOfChildren;
  USHORT NextSibling;
  USHORT FirstChild;
  ULONG  CollectionType  :8;
  ULONG  IsAlias  :1;
  ULONG  Reserved  :23;
  PVOID  UserContext;
} HIDP_LINK_COLLECTION_NODE, *PHIDP_LINK_COLLECTION_NODE;
"""
"""
typedef struct _HIDP_VALUE_CAPS {
  USAGE   UsagePage;
  UCHAR   ReportID;
  BOOLEAN IsAlias;
  USHORT  BitField;
  USHORT  LinkCollection;
  USAGE   LinkUsage;
  USAGE   LinkUsagePage;
  BOOLEAN IsRange;
  BOOLEAN IsStringRange;
  BOOLEAN IsDesignatorRange;
  BOOLEAN IsAbsolute;
  BOOLEAN HasNull;
  UCHAR   Reserved;
  USHORT  BitSize;
  USHORT  ReportCount;
  USHORT  Reserved2[5];
  ULONG   UnitsExp;
  ULONG   Units;
  LONG    LogicalMin;
  LONG    LogicalMax;
  LONG    PhysicalMin;
  LONG    PhysicalMax;
  union {
    struct {
      USAGE  UsageMin;
      USAGE  UsageMax;
      USHORT StringMin;
      USHORT StringMax;
      USHORT DesignatorMin;
      USHORT DesignatorMax;
      USHORT DataIndexMin;
      USHORT DataIndexMax;
    } Range;
    struct {
      USAGE  Usage;
      USAGE  Reserved1;
      USHORT StringIndex;
      USHORT Reserved2;
      USHORT DesignatorIndex;
      USHORT Reserved3;
      USHORT DataIndex;
      USHORT Reserved4;
    } NotRange;
  };
} HIDP_VALUE_CAPS, *PHIDP_VALUE_CAPS;
"""
class HIDP_VALUE_CAPS(Structure):
    _fields_ = [\
               ("UsagePage"         , USAGE),
               ("ReportID"          , UCHAR),
               ("IsAlias"           , BOOLEAN),
               ("BitField"          , USHORT),
               ("LinkCollection"    , USHORT),
               ("LinkUsage"         , USAGE),
               ("LinkUsagePage"     , USAGE),
               ("IsRange"           , BOOLEAN),
               ("IsStringRange"     , BOOLEAN),
               ("IsDesignatorRange" , BOOLEAN),
               ("IsAbsolute"        , BOOLEAN),
               ("HasNull"           , BOOLEAN),
               ("Reserved"          , UCHAR),
               ("BitSize"           , USHORT),
               ("ReportCount"       , USHORT),
               ("Reserved2"         , USHORT*5),
               ("UnitsExp"          , ULONG),
               ("Units"             , ULONG),
               ("LogicalMin"        , LONG),
               ("LogicalMax"        , LONG),
               ("PhysicalMin"       , LONG),
               ("PhysicalMax"       , LONG),
               ("RangeUnionNotRange", TypeRangeUnionNotRange)
               ]
PHIDP_VALUE_CAPS = POINTER(HIDP_VALUE_CAPS)
"""
typedef enum _HIDP_REPORT_TYPE { 
  HidP_Input,
  HidP_Output,
  HidP_Feature
} HIDP_REPORT_TYPE;
"""
HidP_Input   = 0x0000
HidP_Output  = 0x0001
HidP_Feature = 0x0002

"""
typedef struct _HIDP_UNKNOWN_TOKEN {
  UCHAR Token;
  UCHAR Reserved[3];
  ULONG BitField;
} HIDP_UNKNOWN_TOKEN, *PHIDP_UNKNOWN_TOKEN;
typedef struct _HIDP_PREPARSED_DATA * PHIDP_PREPARSED_DATA;
typedef struct _USAGE_AND_PAGE {
  USAGE Usage;
  USAGE UsagePage;
} USAGE_AND_PAGE, *PUSAGE_AND_PAGE;
"""
"""
Hidpi.h
return values
"""
FACILITY_HID_ERROR_CODE = 0x11

HIDP_STATUS_SUCCESS                  = ( (0x0 << 28) | (FACILITY_HID_ERROR_CODE << 16) | (   0) ) & 0xFFFFFFFF
HIDP_STATUS_NULL                     = ( (0x8 << 28) | (FACILITY_HID_ERROR_CODE << 16) | (   1) ) & 0xFFFFFFFF
HIDP_STATUS_INVALID_PREPARSED_DATA   = ( (0xC << 28) | (FACILITY_HID_ERROR_CODE << 16) | (   1) ) & 0xFFFFFFFF
HIDP_STATUS_INVALID_REPORT_TYPE      = ( (0xC << 28) | (FACILITY_HID_ERROR_CODE << 16) | (   2) ) & 0xFFFFFFFF
HIDP_STATUS_INVALID_REPORT_LENGTH    = ( (0xC << 28) | (FACILITY_HID_ERROR_CODE << 16) | (   3) ) & 0xFFFFFFFF
HIDP_STATUS_USAGE_NOT_FOUND          = ( (0xC << 28) | (FACILITY_HID_ERROR_CODE << 16) | (   4) ) & 0xFFFFFFFF
HIDP_STATUS_VALUE_OUT_OF_RANGE       = ( (0xC << 28) | (FACILITY_HID_ERROR_CODE << 16) | (   5) ) & 0xFFFFFFFF
HIDP_STATUS_BAD_LOG_PHY_VALUES       = ( (0xC << 28) | (FACILITY_HID_ERROR_CODE << 16) | (   6) ) & 0xFFFFFFFF
HIDP_STATUS_BUFFER_TOO_SMALL         = ( (0xC << 28) | (FACILITY_HID_ERROR_CODE << 16) | (   7) ) & 0xFFFFFFFF
HIDP_STATUS_INTERNAL_ERROR           = ( (0xC << 28) | (FACILITY_HID_ERROR_CODE << 16) | (   8) ) & 0xFFFFFFFF
HIDP_STATUS_I8042_TRANS_UNKNOWN      = ( (0xC << 28) | (FACILITY_HID_ERROR_CODE << 16) | (   9) ) & 0xFFFFFFFF
HIDP_STATUS_INCOMPATIBLE_REPORT_ID   = ( (0xC << 28) | (FACILITY_HID_ERROR_CODE << 16) | ( 0xA) ) & 0xFFFFFFFF
HIDP_STATUS_NOT_VALUE_ARRAY          = ( (0xC << 28) | (FACILITY_HID_ERROR_CODE << 16) | ( 0xB) ) & 0xFFFFFFFF
HIDP_STATUS_IS_VALUE_ARRAY           = ( (0xC << 28) | (FACILITY_HID_ERROR_CODE << 16) | ( 0xC) ) & 0xFFFFFFFF
HIDP_STATUS_DATA_INDEX_NOT_FOUND     = ( (0xC << 28) | (FACILITY_HID_ERROR_CODE << 16) | ( 0xD) ) & 0xFFFFFFFF
HIDP_STATUS_DATA_INDEX_OUT_OF_RANGE  = ( (0xC << 28) | (FACILITY_HID_ERROR_CODE << 16) | ( 0xE) ) & 0xFFFFFFFF
HIDP_STATUS_BUTTON_NOT_PRESSED       = ( (0xC << 28) | (FACILITY_HID_ERROR_CODE << 16) | ( 0xF) ) & 0xFFFFFFFF
HIDP_STATUS_REPORT_DOES_NOT_EXIST    = ( (0xC << 28) | (FACILITY_HID_ERROR_CODE << 16) | (0x10) ) & 0xFFFFFFFF
HIDP_STATUS_NOT_IMPLEMENTED          = ( (0xC << 28) | (FACILITY_HID_ERROR_CODE << 16) | (0x20) ) & 0xFFFFFFFF
HIDP_STATUS_MESSAGE_DICT = {
        HIDP_STATUS_SUCCESS                  : "HIDP STATUS SUCCESS",
        HIDP_STATUS_NULL                     : "HIDP STATUS NULL",
        HIDP_STATUS_INVALID_PREPARSED_DATA   : "HIDP STATUS INVALID PREPARSED DATA",
        HIDP_STATUS_INVALID_REPORT_TYPE      : "HIDP STATUS INVALID REPORT TYPE",
        HIDP_STATUS_INVALID_REPORT_LENGTH    : "HIDP STATUS INVALID REPORT LENGTH",
        HIDP_STATUS_USAGE_NOT_FOUND          : "HIDP STATUS USAGE NOT FOUND",
        HIDP_STATUS_VALUE_OUT_OF_RANGE       : "HIDP STATUS VALUE OUT OF RANGE",
        HIDP_STATUS_BAD_LOG_PHY_VALUES       : "HIDP STATUS BAD LOG PHY VALUES",
        HIDP_STATUS_BUFFER_TOO_SMALL         : "HIDP STATUS BUFFER TOO SMALL",
        HIDP_STATUS_INTERNAL_ERROR           : "HIDP STATUS INTERNAL ERROR",
        HIDP_STATUS_I8042_TRANS_UNKNOWN      : "HIDP STATUS I8042 TRANS UNKNOWN",
        HIDP_STATUS_INCOMPATIBLE_REPORT_ID   : "HIDP STATUS INCOMPATIBLE REPORT ID",
        HIDP_STATUS_NOT_VALUE_ARRAY          : "HIDP STATUS NOT VALUE ARRAY",
        HIDP_STATUS_IS_VALUE_ARRAY           : "HIDP STATUS IS VALUE ARRAY",
        HIDP_STATUS_DATA_INDEX_NOT_FOUND     : "HIDP STATUS DATA INDEX NOT FOUND",
        HIDP_STATUS_DATA_INDEX_OUT_OF_RANGE  : "HIDP STATUS DATA INDEX OUT OF RANGE",
        HIDP_STATUS_BUTTON_NOT_PRESSED       : "HIDP STATUS BUTTON NOT PRESSED",
        HIDP_STATUS_REPORT_DOES_NOT_EXIST    : "HIDP STATUS REPORT DOES NOT EXIST",
        HIDP_STATUS_NOT_IMPLEMENTED          : "HIDP STATUS NOT IMPLEMENTED"
                            }
#HID_EVENT_NONE     = 0
#HID_EVENT_ALL      = 1
#HID_EVENT_CHANGED  = 2
#HID_EVENT_PRESSED  = 3
#HID_EVENT_RELEASED = 4
#HID_EVENT_SET      = 5
#HID_EVENT_CLEAR    = 6
"""
typedef struct _SECURITY_ATTRIBUTES {
  DWORD  nLength;
  LPVOID lpSecurityDescriptor;
  BOOL   bInheritHandle;
} SECURITY_ATTRIBUTES, *PSECURITY_ATTRIBUTES, *LPSECURITY_ATTRIBUTES;
"""
class SECURITY_ATTRIBUTES(Structure):
    _fields_ = [\
               ("nLength"               , DWORD),
               ("lpSecurityDescriptor"  , LPVOID),
               ("bInheritHandle"        , BOOL)
               ]
LPSECURITY_ATTRIBUTES = POINTER(SECURITY_ATTRIBUTES)