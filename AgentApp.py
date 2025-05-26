from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QSlider, QGroupBox, QTextEdit
)
from PyQt6.QtCore import Qt
import sys

class AgentApp (QWidget):
    def decide(self, environment):
        price = environment['price']
        if price < 30:
            return "Buy"
        elif price > 70:
            return "Sell"
        else :
            return "Hold"
    
class AIAgentSimulation(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Agent Simulator")
        self.setGeometry(100, 100, 400, 300)

        self.environment = {'price': 50}
        self.agent = AgentApp()

        self.createWidget()
        self.createLayout()
    
    def createWidget(self):
        self.priceLabel = QLabel (f"Price: {self.environment['price']}")
        self.priceSlider = QSlider(Qt.Orientation.Horizontal)
        self.priceSlider.setRange(0, 100)
        self.priceSlider.setValue(self.environment['price'])
        self.priceSlider.valueChanged.connect(self.updatePrice)

        self.actionGroup = QGroupBox("Trigger Agent Action")
        self.buyButton = QPushButton("Buy")
        self.sellButton = QPushButton("Sell")
        self.holdButton = QPushButton("Hold")

        self.buyButton.clicked.connect(lambda: self.manualAction("Buy"))
        self.sellButton.clicked.connect(lambda: self.manualAction("Sell"))
        self.holdButton.clicked.connect(lambda: self.manualAction("Hold"))

        self.resultBox = QTextEdit()
        self.resultBox.setReadOnly(True)

        self.autoDecideButton = QPushButton("Auto Decide")
        self.autoDecideButton.clicked.connect(self.Agentdecide)

    def createLayout (self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Price Slider Control")) 
        layout.addWidget(self.priceLabel)
        layout.addWidget(self.priceSlider)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.buyButton)
        h_layout.addWidget(self.sellButton)
        h_layout.addWidget(self.holdButton)
        self.actionGroup.setLayout(h_layout)
        layout.addWidget(self.actionGroup)

        layout.addWidget(self.autoDecideButton)
        layout.addWidget(QLabel("Result"))
        layout.addWidget(self.resultBox)

        self.setLayout(layout)
        
    def updatePrice(self, value):
        self.environment['price'] = value
        self.priceLabel.setText(f"Price: {value}")
    
    def manualAction (self, action ): 
        self.resultBox.append("Manual Action: " + action)

    def Agentdecide(self):
        decide = self.agent.decide(self.environment)
        self.resultBox.append("agent decided based on price: " + decide)

if __name__ == "__main__":
    app =QApplication(sys.argv)
    simulator = AIAgentSimulation()
    simulator.show()
    sys.exit(app.exec())