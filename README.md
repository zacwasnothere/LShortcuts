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
- `cd ~/file_location` (Replace file_location with the LShortcuts file location)
- `chmod +x file_name
./fle_name` (Replace file_name with the LShortcuts file name)
2. Press enter, the file should now be executable.
3. Type `~/file_location/file_name` (Replace file_name and file_location with the LShortcuts file name and location)

#### 🛠️ Troubleshooting
A: Nothing happens when I run it?
→ Try launching from the python terminal to see errors, it may also launch this way:
- `python3 file_name` (Replace file_name with the LShortcuts file name)

B: My shortcut doesn’t appear in the apps menu?
→ Make sure:
- The .desktop file is saved in ~/.local/share/applications/
- The file has a valid Executable and Name field.
- You’ve refreshed your applications cache (log out or restart the shell).

#### Notes
- It may require extra setup to get working.
- Created in python.
- For Linux only.

## License

This project is licensed under the [Apache License 2.0](https://github.com/zacwasnothere/LShortcuts/blob/main/LICENSE).
