import sys, os
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class PictureBox(QWidget):

    def __init__(self):
        super(PictureBox, self).__init__()
        self.hbox = QHBoxLayout(self)
        self.setLayout(self.hbox)

    def openPicture(self, picture):
        for i in range(self.hbox.count()): self.hbox.itemAt(i).widget().close()
        pixmap = QPixmap(picture)
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        self.hbox.addWidget(lbl)


        self.move(300, 200)
        self.setWindowTitle('Pixelateit')
        self.show()

class Window(QWidget):
    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("Pixelateit")
        self.resize(200, 500)
        self.move(1200, 400)
        self.picBox = PictureBox()

        self.running = False
        self.completed = 0

        self.iterations = 200
        self.organisms = 200
        self.home()

    # WIDGETS WITHIN WINDOW
    def home(self):

        self.layout = QVBoxLayout()

        #BUTTONS
        self.btn = QPushButton("Start", self)
        self.btn.clicked.connect(self.start)
        self.btn.move(self.width() - 100,self.height() - 280)
        self.layout.addWidget(self.btn)

        self.btn1 = QPushButton("Resume", self)
        self.btn1.clicked.connect(self.resume)
        self.btn1.move(self.width() - 100,self.height() - 260)
        self.layout.addWidget(self.btn1)

        self.btn2 = QPushButton("Stop", self)
        self.btn2.clicked.connect(self.stop)
        self.btn2.move(self.width() - 100, 240  )
        self.layout.addWidget(self.btn2)

        self.btn3 = QPushButton("Load", self)
        self.btn3.clicked.connect(self.file_open)
        self.btn3.move(self.width() - 100,self.height() - 220)
        self.layout.addWidget(self.btn3)

        self.btn4 = QPushButton("Save", self)
        self.btn4.clicked.connect(self.file_open_without_dialog)
        self.btn4.move(self.width() - 100,self.height() - 200)
        self.layout.addWidget(self.btn4)

        # SLIDERS
        self.sliderLabel = QLabel("Iterations: " + str(self.iterations))
        #self.sliderLabel.move(self.width() - 100, self.height() - 200)
        self.layout.addWidget(self.sliderLabel)
        self.sl = QSlider(Qt.Horizontal)
        self.sl.setMinimum(0)
        self.sl.setMaximum(2000)
        self.sl.setValue(self.iterations)
        self.sl.setTickPosition(QSlider.TicksBelow)
        self.sl.setTickInterval(100)
        #self.sl.move(self.width()-100, self.height() - 180)
        self.layout.addWidget(self.sl)
        self.sl.valueChanged.connect(self.iterationschange)

        self.sliderLabel2 = QLabel("Organisms: " + str(self.organisms))
        #self.sliderLabel.move(self.width() - 100,self.height() - 180)
        self.layout.addWidget(self.sliderLabel2)
        self.sl2 = QSlider(Qt.Horizontal)
        self.sl2.setMinimum(0)
        self.sl2.setMaximum(1000)
        self.sl2.setValue(self.organisms)
        self.sl2.setTickPosition(QSlider.TicksBelow)
        self.sl2.setTickInterval(100)
        #self.sl2.move(self.width()-100, self.height() - 160)
        self.layout.addWidget(self.sl2)
        self.sl2.valueChanged.connect(self.organismschange)

        # PROGRESSBAR
        self.progress = QProgressBar(self)
        #self.progress.setGeometry(0,0,50, self.height() - 140)
        self.progress.setMaximum(100)
        self.layout.addWidget(self.progress)

        self.setLayout(self.layout)
        self.show()

    #CONTROL METHODS FOR WIDGETS
    def start(self):
        print("starting...")
        self.completed = 0
        self.running = True
        while self.completed < 100 and self.running:
            self.completed += 0.001
            QApplication.processEvents()
            self.progress.setValue(self.completed)

    def resume(self):
        print("starting...")
        self.running = True
        while self.completed < 100 and self.running:
            self.completed += 0.001
            QApplication.processEvents()
            self.progress.setValue(self.completed)

    def stop(self):
        print("stopping")
        self.running = False

    def iterationschange(self):
        self.iterations = self.sl.value()
        self.sliderLabel.setText("Iterations: " + str(self.iterations))

    def organismschange(self):
        self.organisms = self.sl2.value()
        self.sliderLabel2.setText("Organisms: " + str(self.organisms))

    def close_application(self):
        sys.exit()

    def file_open(self):
        name = QFileDialog.getOpenFileName(self, 'Open File')
        self.picBox.openPicture(name)

    def file_open_without_dialog(self):
        filename = "grass.png"
        self.picBox.openPicture(filename)

def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()