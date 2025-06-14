import sys
import os
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QFileDialog, QListWidget, QMessageBox, QSizePolicy
)
from PyQt5.QtCore import Qt

APPDIR = os.path.expanduser("~/.local/share/applications")

DARK_STYLE = """
QWidget {
    background-color: #232629;
    color: #f0f0f0;
    font-size: 15px;
}
QLineEdit, QListWidget {
    background-color: #31363b;
    color: #f0f0f0;
    border: 1px solid #444;
    border-radius: 4px;
}
QPushButton {
    background-color: #3daee9;
    color: #232629;
    border: none;
    padding: 6px 12px;
    border-radius: 4px;
    min-width: 100px;
    min-height: 32px;
    max-height: 32px;
}
QPushButton:hover {
    background-color: #6cc7f7;
}
QLabel {
    color: #bfc9d5;
}
QListWidget::item:selected {
    background: #3daee9;
    color: #232629;
}
"""

class LShortcuts(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LShortcuts")
        self.resize(760, 600)
        self.setMinimumSize(760, 600)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setup_ui()
        self.refresh_list()

    def setup_ui(self):
        self.main = QVBoxLayout()

        self.name = QLineEdit()
        self.exec = QLineEdit()
        self.icon = QLineEdit()
        self.desc = QLineEdit()
        self.exebtn = QPushButton("Browse")
        self.exebtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.exebtn.setFixedHeight(32)
        self.exebtn.clicked.connect(self.pick_exec)
        self.iconbtn = QPushButton("Browse")
        self.iconbtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.iconbtn.setFixedHeight(32)
        self.iconbtn.clicked.connect(self.pick_icon)

        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Shortcut Name"))
        form_layout.addWidget(self.name)
        form_layout.addWidget(QLabel("Executable Path"))
        exelayout = QHBoxLayout()
        exelayout.addWidget(self.exec)
        exelayout.addWidget(self.exebtn)
        form_layout.addLayout(exelayout)
        form_layout.addWidget(QLabel("Icon Path"))
        iconlayout = QHBoxLayout()
        iconlayout.addWidget(self.icon)
        iconlayout.addWidget(self.iconbtn)
        form_layout.addLayout(iconlayout)
        form_layout.addWidget(QLabel("Description (optional)"))
        form_layout.addWidget(self.desc)

        form_widget = QWidget()
        form_widget.setLayout(form_layout)
        self.main.addWidget(form_widget)

        self.addbtn = QPushButton("Create Shortcut")
        self.addbtn.clicked.connect(self.make_shortcut)
        self.main.addWidget(self.addbtn)

        self.main.addWidget(QLabel("Your Shortcuts"))
        self.list = QListWidget()
        self.main.addWidget(self.list)
        self.delbtn = QPushButton("Delete Selected Shortcut")
        self.delbtn.clicked.connect(self.delete_selected)
        self.main.addWidget(self.delbtn)

        self.setLayout(self.main)

    def pick_exec(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Executable")
        if path:
            self.exec.setText(path)

    def pick_icon(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Icon", filter="Images (*.png *.xpm *.jpg *.svg)")
        if path:
            self.icon.setText(path)

    def make_shortcut(self):
        n = self.name.text().strip()
        e = self.exec.text().strip()
        i = self.icon.text().strip()
        d = self.desc.text().strip()
        if not n:
            QMessageBox.warning(self, "Missing Information", "Please enter a shortcut name.")
            return
        if not e:
            QMessageBox.warning(self, "Missing Information", "Please select an executable path.")
            return
        fname = f"{n.replace(' ', '_')}.desktop"
        fpath = os.path.join(APPDIR, fname)
        lines = [
            "[Desktop Entry]",
            f"Name={n}",
            f"Exec={e}",
            f"Icon={i}",
            "Type=Application",
            "Terminal=false"
        ]
        if d:
            lines.append(f"Comment={d}")
        content = "\n".join(lines)
        try:
            os.makedirs(APPDIR, exist_ok=True)
            with open(fpath, "w") as f:
                f.write(content)
            os.chmod(fpath, 0o755)
            self.update_db()
            self.refresh_list()
            QMessageBox.information(self, "Shortcut Created", f"Shortcut '{n}' added to your applications menu.")
        except Exception as ex:
            QMessageBox.critical(self, "Error", str(ex))

    def refresh_list(self):
        self.list.clear()
        if not os.path.isdir(APPDIR):
            return
        for f in sorted(os.listdir(APPDIR)):
            if f.endswith(".desktop"):
                self.list.addItem(f)

    def delete_selected(self):
        item = self.list.currentItem()
        if not item:
            return
        fname = item.text()
        fpath = os.path.join(APPDIR, fname)
        if QMessageBox.question(self, "Delete Shortcut", f"Delete '{fname}'?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            try:
                os.remove(fpath)
                self.update_db()
                self.refresh_list()
                QMessageBox.information(self, "Shortcut Deleted", f"Shortcut '{fname}' removed.")
            except Exception as ex:
                QMessageBox.critical(self, "Error", str(ex))

    def update_db(self):
        try:
            subprocess.run(
                ["update-desktop-database", APPDIR],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except Exception:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(DARK_STYLE)
    w = LShortcuts()
    w.show()
    sys.exit(app.exec_())