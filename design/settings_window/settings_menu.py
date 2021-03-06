from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout,\
    QHBoxLayout, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
import sys
import json
import design.settings_window.localize as settings_localize
import design.settings_window.styles as settings_styles
import os


class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Container
        self.body = QWidget()
        self.bodyQVBoxLayout = QVBoxLayout()
        self.bodyQVBoxLayout.setSpacing(50)

        # Header
        self.header = QWidget()
        self.headerQHBoxLayout = QHBoxLayout()
        self.headerQHBoxLayout.setSpacing(100)

        # Back Button
        self.backQButton = QPushButton()
        self.backQButton.setIcon(QIcon('design/images/back.png'))
        self.backQButton.setIconSize(QSize(32, 32))
        self.backQButton.setFocusPolicy(Qt.NoFocus)

        # Settings Label
        self.settingsLabel = QLabel()

        # Container
        self.container = QWidget()
        self.containerQVBoxLayout = QVBoxLayout()

        # Language Box
        self.languageBox = QWidget()
        self.languageQHBoxLayout = QHBoxLayout()
        self.languageQHBoxLayout.setSpacing(20)

        # Language Label
        self.languageLabel = QLabel()

        # Language buttons
        self.ENButton = QPushButton()
        self.ENButton.setObjectName('EN')
        self.ENButton.setIcon(QIcon('design/images/united-kingdom.png'))
        self.ENButton.setIconSize(QSize(32, 32))

        self.UAButton = QPushButton()
        self.UAButton.setObjectName('UA')
        self.UAButton.setIcon(QIcon('design/images/ukraine.png'))
        self.UAButton.setIconSize(QSize(32, 32))

        self.buttons = [self.ENButton, self.UAButton]
        self.ENButton.clicked.connect(self.language_button_clicked)
        self.UAButton.clicked.connect(self.language_button_clicked)

        settings_localize.set_settings_localization(self)
        settings_styles.Styles.set_settings_styles(self)
        self.init_body()

        # Main window
        self.main_window = None

    def init_header(self):
        self.headerQHBoxLayout.addWidget(self.backQButton)
        self.headerQHBoxLayout.addWidget(self.settingsLabel)
        self.headerQHBoxLayout.addStretch()
        self.header.setLayout(self.headerQHBoxLayout)

    def init_language_box(self):
        self.languageQHBoxLayout.addWidget(self.languageLabel)

        self.languageQHBoxLayout.addWidget(self.ENButton)
        self.languageQHBoxLayout.addWidget(self.UAButton)
        self.languageQHBoxLayout.addStretch()
        self.languageBox.setLayout(self.languageQHBoxLayout)

    def init_container(self):
        self.init_language_box()
        self.containerQVBoxLayout.addWidget(self.languageBox)
        self.container.setLayout(self.containerQVBoxLayout)

    def init_body(self):
        self.init_header()
        self.init_container()
        self.bodyQVBoxLayout.addWidget(self.header)
        self.bodyQVBoxLayout.addWidget(self.container)
        self.bodyQVBoxLayout.addStretch()
        self.body.setLayout(self.bodyQVBoxLayout)
        self.setCentralWidget(self.body)

    def language_button_clicked(self):
        try:
            button = self.sender()
            for lg_button in self.buttons:
                if lg_button == button:
                    button.setIconSize(QSize(56, 56))
                    button.setFocus()
                    with open(os.path.expanduser("~/Documents/LNUReader/settings.json")) as json_file:
                        lg_info = json.load(json_file)
                    lg_info["language"] = button.objectName()
                    with open(os.path.expanduser("~/Documents/LNUReader/settings.json"), 'w') as outfile:
                        json.dump(lg_info, outfile)
                    settings_localize.set_settings_localization(self)
                else:
                    lg_button.setIconSize(QSize(32, 32))
        except Exception as e:
            print(e)
            return

