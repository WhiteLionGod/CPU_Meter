# CPU_Meter

Want to track how much load is on your CPU. Well, using this CPU Meter, you can easily do it by lancuhing this program.
*Please note that the data given may sometimes be incorrect.
*Also note that the files indivuail, no executable, require a enviorment named env.

Please note that is you want this in a execuatble file format, please check the v1-exe release on the right side in the releases section.
If you want to view the code on github pages, in app.py, remove  the comment from line 28 and comment line 30.

Pyinstaller Code to Create Executable: pyinstaller --name="CPU_Meter" --onefile --paths=env\Lib\site-packages --add-data="static;static" --add-data="templates;templates" app.py --icon=static\favicon.ico --noconsole
