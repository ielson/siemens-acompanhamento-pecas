from PyQt5 import QtWidgets
from designer.mainDesign import Ui_MainWindow  # importing our generated file
import sys
import logging
import mailSender


class myApp(QtWidgets.QMainWindow):
    historicoPath = ''

    def __init__(self):
        super(myApp, self).__init__()
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.path_button.clicked.connect(self.selectFile)
        self.ui.run_button.clicked.connect(self.run)
        self.ui.stop_button.clicked.connect(self.stop)
        self.ui.path_button.setShortcut('Ctrl+O')
        self.ui.path_button.setStatusTip('Escolher arquivo de Histórico')
        self.ui.run_button.setStatusTip('Rodar código para envio dos e-mails')
        self.ui.radio1.setChecked(True)


        logTextBox = mailSender.QTextEditLogger(self)
        logTextBox.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
        mailSender.basic_logger.addHandler(logTextBox)
        mailSender.basic_logger.setLevel(logging.INFO)
        self.ui.verticalLayout.addWidget(logTextBox.widget)



    def selectFile(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Escolher Histórico de Peças', '',"Arquivos do Excel (*.xlsx)")
        self.historicoPath = fname[0]
        mailSender.basic_logger.info("Arquivo Selecionado com sucesso ")
        mailSender.basic_logger.info("Caminho do arquivo: {}".format(self.historicoPath))
        #indexOfChecked = [self.ButtonGroup.buttons()[x].isChecked() for x in range(len(self.ButtonGroup.buttons()))].index(True)




    def run(self):
        # Vê qual a regional selecionada
        botoes = [getattr(self.ui, 'radio' + str(i)) for i in range(1, 7)]
        selecionado = [botao.isChecked() for botao in botoes].index(True)
        print(botoes[selecionado].text())

        simulacao = self.ui.simulacaoCB.isChecked()
        print(simulacao)

        mailSender.main(self.historicoPath, simulacao)

    def stop(self):
        mailSender.basic_logger.info("Parando o programa")
        sys.exit()

app = QtWidgets.QApplication([])
application = myApp()
application.show()
sys.exit(app.exec())
