rm -f COMPortVerify.exe
..\..\..\work\RD_Project\RHINO\SW\PyInstaller-2.1\pyinstaller.py -F -w -p . main.py
cp dist\main.exe COMPortVerify.exe