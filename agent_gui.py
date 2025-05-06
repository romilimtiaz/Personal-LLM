import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QTextEdit, QLineEdit, QPushButton, 
                            QLabel, QComboBox, QMessageBox, QFrame)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QIcon, QPalette, QColor
import ollama

class ResponseWorker(QThread):
    response_ready = pyqtSignal(str)
    error_occurred = pyqtSignal(str)

    def __init__(self, model_name, prompt):
        super().__init__()
        self.model_name = model_name
        self.prompt = prompt

    def run(self):
        try:
            response = ollama.generate(
                model=self.model_name,
                prompt=self.prompt,
                stream=False
            )
            self.response_ready.emit(response['response'])
        except Exception as e:
            self.error_occurred.emit(str(e))

class CodingAgentGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Coding Assistant")
        self.setMinimumSize(1000, 700)
        self.conversation_history = []
        self.model_name = "codellama"
        
        # Set dark theme
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a1a1a;
            }
            QWidget {
                background-color: #1a1a1a;
                color: #ffffff;
            }
            QTextEdit {
                background-color: #2d2d2d;
                color: #00ff00;
                border: 2px solid #3d3d3d;
                border-radius: 8px;
                padding: 12px;
                font-family: 'Consolas', monospace;
                font-size: 12px;
            }
            QLineEdit {
                background-color: #2d2d2d;
                color: #ffffff;
                border: 2px solid #3d3d3d;
                border-radius: 8px;
                padding: 12px;
                font-size: 12px;
            }
            QLineEdit:focus {
                border: 2px solid #00ff00;
            }
            QPushButton {
                background-color: #00ff00;
                color: #000000;
                border: none;
                border-radius: 8px;
                padding: 12px 24px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #00cc00;
            }
            QComboBox {
                background-color: #2d2d2d;
                color: #ffffff;
                border: 2px solid #3d3d3d;
                border-radius: 8px;
                padding: 8px;
                min-width: 150px;
            }
            QComboBox:hover {
                border: 2px solid #00ff00;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                image: none;
                border: none;
            }
            QLabel {
                color: #ffffff;
                font-size: 14px;
            }
        """)
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Create header with glowing effect
        header_frame = QFrame()
        header_frame.setStyleSheet("""
            QFrame {
                background-color: #2d2d2d;
                border-radius: 10px;
                border: 2px solid #3d3d3d;
            }
        """)
        header_layout = QVBoxLayout(header_frame)
        
        header = QLabel("🤖 AI Coding Assistant")
        header.setFont(QFont('Arial', 24, QFont.Weight.Bold))
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet("color: #00ff00;")
        header_layout.addWidget(header)
        
        layout.addWidget(header_frame)
        
        # Create model selector with custom styling
        model_frame = QFrame()
        model_frame.setStyleSheet("""
            QFrame {
                background-color: #2d2d2d;
                border-radius: 10px;
                border: 2px solid #3d3d3d;
                padding: 10px;
            }
        """)
        model_layout = QHBoxLayout(model_frame)
        
        model_label = QLabel("Model:")
        model_label.setFont(QFont('Arial', 12))
        self.model_combo = QComboBox()
        self.model_combo.addItem("codellama")
        self.model_combo.addItem("llama2")
        self.model_combo.addItem("mistral")
        self.model_combo.currentTextChanged.connect(self.change_model)
        model_layout.addWidget(model_label)
        model_layout.addWidget(self.model_combo)
        model_layout.addStretch()
        
        layout.addWidget(model_frame)
        
        # Create chat display with custom styling
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont('Consolas', 12))
        self.chat_display.setStyleSheet("""
            QTextEdit {
                background-color: #2d2d2d;
                color: #00ff00;
                border: 2px solid #3d3d3d;
                border-radius: 10px;
                padding: 15px;
            }
        """)
        layout.addWidget(self.chat_display)
        
        # Create input area with custom styling
        input_frame = QFrame()
        input_frame.setStyleSheet("""
            QFrame {
                background-color: #2d2d2d;
                border-radius: 10px;
                border: 2px solid #3d3d3d;
                padding: 10px;
            }
        """)
        input_layout = QHBoxLayout(input_frame)
        
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your request here...")
        self.input_field.returnPressed.connect(self.send_message)
        self.input_field.setMinimumHeight(40)
        
        send_button = QPushButton("Send")
        send_button.setMinimumHeight(40)
        send_button.clicked.connect(self.send_message)
        
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(send_button)
        
        layout.addWidget(input_frame)
        
        # Add welcome message
        self.add_message("Assistant", "Welcome! I'm your AI coding assistant. How can I help you today?")
        
    def change_model(self, model_name):
        self.model_name = model_name
        
    def add_message(self, sender, message):
        if sender == "User":
            self.chat_display.append(f'<p style="color: #00ff00;"><b>You:</b> {message}</p>')
        else:
            self.chat_display.append(f'<p style="color: #00ff00;"><b>Assistant:</b> {message}</p>')
        self.chat_display.verticalScrollBar().setValue(
            self.chat_display.verticalScrollBar().maximum()
        )
        
    def send_message(self):
        message = self.input_field.text().strip()
        if not message:
            return
            
        self.input_field.clear()
        self.add_message("User", message)
        
        # Add to conversation history
        self.conversation_history.append(f"User: {message}")
        
        # Create context-aware prompt
        context = "\n".join(self.conversation_history[-5:])
        prompt = f"""You are a helpful coding assistant. Previous conversation:
{context}

Current request: {message}

Please provide a helpful response focusing on coding and project management tasks."""
        
        # Create and start worker thread
        self.worker = ResponseWorker(self.model_name, prompt)
        self.worker.response_ready.connect(self.handle_response)
        self.worker.error_occurred.connect(self.handle_error)
        self.worker.start()
        
    def handle_response(self, response):
        self.conversation_history.append(f"Assistant: {response}")
        self.add_message("Assistant", response)
        
    def handle_error(self, error_message):
        QMessageBox.critical(self, "Error", f"An error occurred: {error_message}")

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    window = CodingAgentGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 