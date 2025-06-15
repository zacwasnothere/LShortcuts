LShortcuts

LShortcuts is a free and open source Linux utility that helps you to create and remove .desktop files. These are what make applications and executables show up in your apps menu.

No installation required. Just download and run the file.


## ✨ Features

- Easy of use GUI to create and remove .desktop shortcuts to your applications menu.
- Portable — run directly without installation.
- Works on most Linux distributions and desktop environments.
###### ![image](https://github.com/user-attachments/assets/b0be8765-48ad-43bf-90c9-ad71cb7240a7)

## 📦 Download

1. Navigate to the Releases page.
2. Select the release of your choice (the latest release is recommended).
3. Click on LShortcuts.
4. Locate the executable in your files manager.
5. Right click on the executable and select `properties`
6. Enable `Executable as Program`

###### Alternative Option Using The Command Line
1. Type the following commands.
`cd ~/Downloads` (Or wherever you saved the executable)
`chmod +x LShortcuts
./LShortcuts`
2. Press enter.

###### Optional: Add it to your PATH
1. Type the following commands.
`mkdir -p ~/.local/bin
mv ~/Downloads/LShortcuts ~/.local/bin/lshortcuts
chmod +x ~/.local/bin/lshortcuts`
2. Press enter.

#### 🛠️ Troubleshooting
A: Nothing happens when I run it?
→ Try launching from the python terminal to see errors:
`python3 LShortcuts`

B: My shortcut doesn’t appear in the apps menu?
→ Make sure:
The .desktop file is saved in ~/.local/share/applications/
The file has a valid Executable and Name field
You’ve refreshed your applications cache (log out or restart the shell.

## License

This project is licensed under the [Apache License 2.0](https://github.com/zacwasnothere/LShortcuts/blob/main/LICENSE).
