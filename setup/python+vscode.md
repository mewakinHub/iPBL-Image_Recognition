# Image Processing Environment for iPBL

## Objectives
- This page explains how to install both Python and VSCode to constitute our image processing environment.
- It is not affecting the PC environment (like the registry) even if this environment is installed. <br>
  
    > **Note** All you have to do is delete the folder when this environment is no longer needed.
  
  <br>

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

### :o:Checkpoint(Start the environment 1)
- Start the environment from "py23_start" icon on the Desktop (or C:\oit\py23_ipbl\py23i_start.bat).
- **If the following warning pops up...**
  - **CHECK** the "Trust the authors..." box out
  - CLICK the **"YES"** button <br>
    <image src="../image/trust_vsws.png" width="50%" height="50%">

### :o:Checkpoint(Start the environment 2)
- **If the location of the EXPLORER does not be the SouceCode folder(SOURCECODE), you have to open the "C:\oit\py23_ipbl\SourceCode" from the [File]-[Open Folder] menu.** <br>
  <image src="../image/vsws_explorer.png" width="50%" height="50%">
- **If the terminal window has not shown, please open it from the [Terminal]-[New Terminal] menu.** <br>
  <image src="../image/vsws_tmenu.png" width="50%" height="50%">
- Please confirm Python modules by pip list command.<br>
  <image src="../image/vsws_piplist.png" width="50%" height="50%">

### :o:Checkpoint(Run python code with VSCode)
- Please confirm how to execute the sample Python code with VSCode.
  - Open the "hello_python.py" file with Double Click in [SOURCECODE]-[samples] folder of the explorer menu.<br>
    <image src="../image/vs_sample1.png" width="100%" height="100%">
  - Open the terminal window if it's not appeared.<br>
    <br>
    > **Note** The current Working directory shown in the terminal window has to be the same as the file's location to execute. <br>
    >   In the following case, you have to change the directory to "C:\oit\py23_ipbl\SourceCode\samples\" with the "cd" command. <br>
    >   <image src="../image/vs_cdcommand.png" width="100%" height="100%"><br>
    <br>
  - Please confirm that the Python code is able to execute in the terminal window.
    ```sh
    C:\oit\py23_ipbl\SourceCode\samples> python hello_python.py
    ```
    <br>
    
    > **Note** The program is executable with the run button, but **we suggest executing with the command line**. <br>
    > <image src="../image/vs_runbutton.png"><br>
    <br>

  - The following are running results successfully.<br>
    <image src="../image/vs_runsample1.png"><br>

### :o: Practice
- Give it a try to run the ”show_image.py”.
  - It is the sample of reading and showing an image file with the cv2 library.
  - The window is closed if any button is pressed.
- Give it a try to run the "show_video.py"
  - It is the sample of capturing from the camera and showing frames with the cv2 library.
  - The window is closed if \'q\' button is pressed.
- Give it a try to run the "test_mediapipe.py"
  - This program is written in the old usage of the Mediapipe, but you can experiment with the following methods defined in the Mediapipe.<br>
    - All methods simultaneously with \'a\' button
    - FACE with \'f\' button
    - FACE MESH with \'m\' button
    - HANDS with \'h\' button
    - POSE with \'p\' button <br>
  
  <br>
  
  > **Note** The latest usage of the Mediapipe is able to be learned in another section.

  <br>
