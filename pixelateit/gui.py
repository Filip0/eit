import sys, os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PIL.ImageQt import ImageQt
import time

class PictureBox(QWidget):

    def __init__(self, pos):
        super(PictureBox, self).__init__()
        self.hbox = QHBoxLayout(self)
        self.setLayout(self.hbox)
        self.move(pos[0], pos[1])

    def openPicture(self, picture):
        for i in range(self.hbox.count()): self.hbox.itemAt(i).widget().close()
        pixmap = QPixmap(picture)
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        self.hbox.addWidget(lbl)


        self.setWindowTitle('Pixelateit')
        self.show()

    def openPIL_Image(self, image):
        for i in range(self.hbox.count()): self.hbox.itemAt(i).widget().close()
        qti = ImageQt(image)
        pixmap = QPixmap().fromImage(qti)
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        self.hbox.addWidget(lbl)
        self.move(300, 200)
        self.setWindowTitle('Pixelateit')
        self.show()

class Window(QWidget):
    def __init__(self, pixelateit, parent=None):
        self.app = QApplication(sys.argv)
        super(Window, self).__init__(parent)
        self.px = pixelateit
        self.setWindowTitle("Pixelateit")
        self.resize(200, 500)
        self.move(800, 100)
        self.original_picBox = PictureBox((30, 30))
        self.picBox = PictureBox((500, 30))

        self.running = False
        self.completed = 0

        self.iterations = 200
        self.organisms = 200
        self.home()

    def run(self):
        sys.exit(self.app.exec_())

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

        self.mover_widget_label = QLabel("Movers")
        self.layout.addWidget(self.mover_widget_label)
        self.mover_widget = QListWidget()
        self.mover_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.mover_widget.addItems(["SimpleMover", "ZagMover", "CircleMover", "RandomMover"])
        self.layout.addWidget(self.mover_widget)

        self.eater_widget_label = QLabel("Eater")
        self.layout.addWidget(self.eater_widget_label)
        self.eater_widget = QListWidget()
        self.eater_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.eater_widget.addItems(["SimpleEater", "SimpleEater2", "SuperSimpleEater", "CalcEater", "AvgEater"])
        self.layout.addWidget(self.eater_widget)


        # PROGRESSBAR
        self.progress = QProgressBar(self)
        #self.progress.setGeometry(0,0,50, self.height() - 140)
        self.progress.setMaximum(100)
        self.layout.addWidget(self.progress)

        self.setLayout(self.layout)
        self.show()

    #CONTROL METHODS FOR WIDGETS
    def start(self):
        if not self.px.image_loaded:
            msg = QMessageBox()
            msg.setText("No image loaded")
            msg.exec_()
            return
        print("starting...")
        self.completed = 0
        self.running = True
        while self.completed < self.iterations and self.running:
            self.px.update()
            self.completed += 1
            if self.completed % 10 == 0:
                self.picBox.openPicture(self.px.save_image("out/out{}.png".format(self.completed)))

            QApplication.processEvents()
            self.progress.setValue(self.completed/self.iterations*100)
        self.px.save_image("out/{}.png".format(time.time()))


    def resume(self):
        print("starting...")
        self.running = True
        while self.completed < self.iterations and self.running:
            self.px.update()
            self.completed += 1
            if self.completed % 10 == 0:
                self.picBox.openPicture(self.px.save_image("out/out{}.png".format(self.completed)))

            QApplication.processEvents()
            self.progress.setValue(self.completed/self.iterations*100)

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
        movers = [x.text() for x in self.mover_widget.selectedItems()]
        eaters = [x.text() for x in self.eater_widget.selectedItems()]
        self.px.load_image(name, movers, eaters)
        self.original_picBox.openPicture(name)
        self.picBox.openPicture(name)

    def file_open_without_dialog(self):
        filename = "grass.png"
        self.picBox.openPicture(filename)

