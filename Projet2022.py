import sys
from PyQt5.QtCore import pyqtSlot
from paramiko import client
from PyQt5.QtGui import QIntValidator, QPixmap, QFont
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

class PagePrincipale:
    class PPView(QWidget):
        def __init__(self):
            
            super().__init__()
            self.myCtrl = PagePrincipale.Controller()
            
            self.labelImage = QLabel(self)
            self.pixmap = QPixmap('logo.png')
            self.labelImage.setPixmap(self.pixmap)
            self.labelImage.resize(self.pixmap.width(),self.pixmap.height())
            
            self.label = QLabel("Medi'doc")
            self.label2 = QLabel("Bienvenue sur la page d'acceuil")
            self.b1 = QPushButton("Créer un dossier")
            self.b2 = QPushButton("Importer un dossier")
            
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label2.setAlignment(QtCore.Qt.AlignCenter)
            
            self.init_ui()
            
            self.show()
            
        def init_ui(self):
             
             h_box_image = QHBoxLayout()
             h_box_image.addWidget(self.labelImage)
             u_box = QFormLayout()
             h_box = QVBoxLayout()
             
             h_box.addWidget(self.label)
             h_box.addWidget(self.label2)
             h_box.addWidget(self.b1)
             h_box.addWidget(self.b2)
             
            
             v_box = QVBoxLayout()
             v_box.addLayout(h_box_image)
             v_box.addLayout(h_box)
             v_box.addLayout(u_box)
             
             
             self.setWindowTitle("page d'acceuil")
            
             self.b1.clicked.connect(self.btn1_click)
             self.b2.clicked.connect(self.btn2_click)
             self.setLayout(v_box)
             
        def btn1_click(self):
            print("bouton 1 marche bien")
            self.cams = FenetrePatient.FView()
            self.close()
            
        def btn2_click(self):
            print("bouton 2 marche bien")
            
    class Controller:
        def __init__(self):
            self.myModel = model
            
    class Model:
        def __init__(self):
            print("dddd")
            
            
class FenetrePatient:
    class FView(QWidget):
        def __init__(self):
            super().__init__()

            self.myCtrl = FenetrePatient.Controller()

            self.labelNom = QLabel(self)
            self.labelNom.setText('Nom :')
            self.Nom = QLineEdit(self)

            self.labelPrenom = QLabel(self)
            self.labelPrenom.setText('Prenom :')
            self.Prenom = QLineEdit(self)

            self.labelAge = QLabel(self)
            self.labelAge.setText('Age :')
            self.Age = QLineEdit(self)


            self.labelSexe = QLabel('Sexe')
            self.sexeM = QRadioButton('M')
            self.sexeF = QRadioButton('F')
            
 
            self.historique = QPushButton('Historique')

            self.symptome = QPlainTextEdit('Veuillez entrer les symptômes et ordonnances ici')
            self.medoc = QPlainTextEdit('Propositions de médicaments')

            self.sauvegarder = QPushButton('Sauvegarder')

            self.fermer = QPushButton('Fermer')


            self.init_ui()
            self.show()
        
        def init_ui(self):

            h_box = QHBoxLayout()
            h_box.addWidget(self.labelNom)
            h_box.addWidget(self.Nom)
            
            h_box.addWidget(self.labelPrenom)
            h_box.addWidget(self.Prenom)

        
            h_box_age = QHBoxLayout()
            h_box_age.addWidget(self.labelAge)
            h_box_age.addWidget(self.Age)

            
            h_box_sexe = QHBoxLayout()
            h_box_sexe.addWidget(self.labelSexe)
            h_box_sexe.addWidget(self.sexeM)
            h_box_sexe.addWidget(self.sexeF)

            
            h_box_btn_history = QHBoxLayout()
            h_box_btn_history.addWidget(self.historique)

           
            v_box_top_left = QVBoxLayout()
            v_box_top_left.addLayout(h_box)
            v_box_top_left.addLayout(h_box_age)
            v_box_top_left.addLayout(h_box_sexe)

            h_box_top_right = QHBoxLayout()
            h_box_top_right.addLayout(h_box_btn_history)

           
            h_box_top = QHBoxLayout()
            h_box_top.addLayout(v_box_top_left)
            h_box_top.addLayout(h_box_top_right)

            
            h_box_mid = QHBoxLayout()
            h_box_mid.addWidget(self.symptome)
            h_box_mid.addWidget(self.medoc)

            
            h_box_button = QHBoxLayout()
            h_box_button.addWidget(self.sauvegarder)
            h_box_button.addWidget(self.fermer)

            
            v_box = QVBoxLayout()
            v_box.addLayout(h_box_top)
            v_box.addLayout(h_box_mid)
            v_box.addLayout(h_box_button)

            self.setLayout(v_box)
            self.setWindowTitle('Dossier')

            self.sauvegarder.clicked.connect(self.sauvegarde)
            self.fermer.clicked.connect(self.fermeture)
            self.historique.clicked.connect(self.Historique)
            self.medoc.setReadOnly(True)
            
        def sauvegarde(self):
            print("save marche bien")
            
        def fermeture(self):
            print("fermture marche bien")
            self.cams = PagePrincipale.PPView()
            self.close()
            
        def Historique(self):
            print("histo work")
            self.cams = PageHistorique.Phistorique()
            self.close()
            
    class Controller:
        def __init__(self):
            self.myModel = model
            
    class Model:
        def __init__(self):
            print("bon")
            
class PageHistorique:
    class Phistorique(QWidget):    
        def __init__(self):

            super().__init__()

            self.myCtrl = ctrl

            self.labelNom = QLabel(self)
            self.labelNom.setText('Nom')

            self.labelPrenom = QLabel(self)
            self.labelPrenom.setText('Prénom')

            self.labelAge = QLabel(self)
            self.labelAge.setText('Age')
        
            self.inputNom = QLineEdit('')
            self.inputPrenom = QLineEdit('')
            self.inputAge = QLineEdit('')
        
            self.inputText1 = QPlainTextEdit('Historique des symptômes et ordonnances du patient')
            self.buttonClose = QPushButton('Fermer')
        
            self.init_ui()
            self.show()

        def init_ui(self):
        
            v_box1 = QVBoxLayout()
            v_box1.addWidget(self.labelNom)
            v_box1.addWidget(self.labelPrenom)
            v_box1.addWidget(self.labelAge)
            
            v_box2 = QVBoxLayout()
            v_box2.addWidget(self.inputNom)
            v_box2.addWidget(self.inputPrenom)
            v_box2.addWidget(self.inputAge)
        
            h_box = QHBoxLayout()
            h_box.addLayout(v_box1)
            h_box.addLayout(v_box2)

        
            v_box = QVBoxLayout()
            v_box.addWidget(self.inputText1)
            v_box.addWidget(self.buttonClose)


            box = QVBoxLayout()
            box.addLayout(h_box)
            box.addLayout(v_box)

            self.setLayout(box)
            self.setWindowTitle("Historique")
            self.inputText1.setDisabled(True)
            self.inputNom.setDisabled(True)
            self.inputPrenom.setDisabled(True)
            self.inputAge.setDisabled(True)
        
            self.buttonClose.setToolTip('revenir à la fenêtre dossier')
            self.buttonClose.clicked.connect(self.fermeture)
            
    
        def fermeture(self):
            print("fermture marche bien")
            self.cams = FenetrePatient.FView
            self.close()
            
print(__name__)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = PagePrincipale.Model()
    ctrl = PagePrincipale.Controller()
    view = PagePrincipale.PPView()
    sys.exit(app.exec_())

        
        