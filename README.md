## How to Setup and other detail
[Image Processing Environment for iPBL](https://github.com/ipbl-oit-siit/portal/blob/main/setup/python%2Bvscode.md#details-of-the-installed-environment)

Note:  MediaPipe or other libraries may not be supported with the latest version of Python

#### Details of the installed environment
- Python3.10.11.amd64 (WPy64-310111)
  - dlib 19.24.2
  - matplotlib 3.7.1
  - mediapipe 0.10.0
  - numpy 1.23.4
  - opencv-contrib-python 4.7.0.72
  - opencv-python 4.7.0.72
  - openpyxl 3.1.2
  - Pillow 9.5.0
  - pip 23.1.2
  - PyAutoGUI 0.9.54
  - PyDirectInput 1.0.4
  - PyQt5 5.15.9
  - pyqtgraph 0.13.3
  - pywin32 306
  - scikit-learn 1.2.2
  - scipy 1.10.1 <br>
  and more...
- Visual Studio Code 1.78.2 (Portable)

## prerequisite
- Windows 10 or 11
- Built-in camera or USB-camera
- Uninstalling or stopping antivirus software
  - They may remove our installer and batch files.

## Setup both Python and VSCode with our installer
### procedure
- Download our installer file (405MB) by clicking the following URL.
  - https://oskit-my.sharepoint.com/:u:/g/personal/yoshiyuki_kamakura_oit_ac_jp/EWfz3jSUWchLlrW9HwD-bnYBdxiQvslxluGfz3aksTZePw?e=Ru4z3G
    - **PW is written on XXXX.**
    - If you have installed some antivirus software, this executable file and other batch files may not work properly.
- Execute "py23i_instl.exe" file.
  - This installer is safe.
  - **If the following warning pops up (The background color is red in some cases.), Please choose "run anyway" after clicking the "more info" link. **<br>
    <image src="../image/warning01.png" width="40%" height="40%"><br>
    <image src="../image/warning02.png" width="40%" height="40%"><br>
    - Please select `More info` and `Run anyway`.
- Choose "はい(Y)".<br>
  <image src="../image/py23i_instll.jpg" width="20%" height="20%">
- This installer setup the image processing environment (Python3 + VSCode) into "C:\oit\py23_ipbl", and creates the following link on your Desktop.<br>
  <image src="../image/icon.png" width="10%" height="10%">

> **Note**
> Creating a link on the Desktop often fails. In that case, please run "C:\oit\py23_ipbl\py23i_start.bat" directly. It is possible to create the link manually, but DO NOT move anything in the py23_ipbl folder!)

#### Installed folder structure
- This environment is installed to "C:\oit\py23_ipbl", and its inside is included the following.
  - **SourceCode**: the working directory for saving the source code
  - **usedfiles**: NEED NOT touch
  - **VSCode**: NEED NOT touch, Visual Studio Code 1.78.2
  - **WPy64-310111**: NEED NOT touch, Python3.10.11.amd64 (WPy64-310111)
  - **fig_pbl.ico**: icon file
  - **py23i_start.bat**: bat file to start this environment up 
