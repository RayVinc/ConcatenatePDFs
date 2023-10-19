## Merge PDFs with Python

This tool allows the user to select PDFs using an input GUI created with the tkinter library and merges them with tools from the PyPDF2 library.

NOTE: The script has to be placed in the Windows system and will **NOT RUN** properly on the Ubuntu sub-system. The tkinter library uses the ``Display`` variable to display the input GUI. Ubuntu can not properly reference this variable, unless the properly set by manual user input.

In the GUI, select the desired output directory and add files from the file explorer in the desired order of merging.
![Screenshot](PDFMergeTool_Screenshot.png)
