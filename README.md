# 🤖 AI Coding Assistant

A powerful, local AI coding assistant with a sleek JARVIS-inspired interface that helps you write code, manage projects, and solve programming challenges - all running completely offline on your machine.

![AI Coding Assistant](https://i.imgur.com/placeholder.png)

## 🌟 Features

### Core Features
- **Local AI Processing**: Runs completely offline using Ollama and local models
- **Multiple AI Models**: Support for CodeLlama, Llama2, and Mistral
- **Context-Aware**: Maintains conversation history for better responses
- **Free to Use**: No API costs or subscriptions required

### User Interface
- **JARVIS-Inspired Design**: Sleek dark theme with green accents
- **Modern GUI**: Professional and intuitive interface
- **Real-time Responses**: Instant feedback with typing indicators
- **Code Highlighting**: Syntax-highlighted code display
- **Responsive Layout**: Adapts to different screen sizes

### Technical Capabilities
- **Code Generation**: Write and modify code based on your requirements
- **Project Management**: Get help with project structure and organization
- **Code Explanation**: Understand complex code with detailed explanations
- **Debugging Assistance**: Help identify and fix code issues
- **Best Practices**: Suggestions for code optimization and standards

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed on your system
- 8GB+ RAM recommended for optimal performance

### Installation

1. **Install Ollama**
   - Visit [Ollama's website](https://ollama.ai/)
   - Download and install for your operating system
   - Follow the installation instructions

2. **Pull Required Models**
   ```bash
   ollama pull codellama
   ```

3. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **GUI Version (Recommended)**
   ```bash
   python agent_gui.py
   ```

2. **CLI Version**
   ```bash
   python agent.py
   ```

## 💻 Usage

### Basic Commands
- Ask for code examples: "Write a Python function to sort a list"
- Get project help: "Help me structure a new web application"
- Debug code: "Help me fix this error in my code"
- Learn concepts: "Explain how async/await works in JavaScript"

### Tips for Best Results
1. Be specific in your requests
2. Provide context when needed
3. Break complex tasks into smaller steps
4. Use the model selector to switch between different AI models

## 🛠️ Customization

### GUI Customization
- Adjust window size
- Change font sizes
- Modify color scheme
- Customize layout

### Model Selection
- Choose between different AI models:
  - CodeLlama (default): Best for coding tasks
  - Llama2: General purpose
  - Mistral: Balanced performance

## 🔧 Technical Details

### Architecture
- Built with Python and PyQt6
- Uses Ollama for local AI processing
- Modular design for easy extension
- Thread-safe implementation

### Dependencies
- PyQt6: Modern GUI framework
- Ollama: Local AI model runner
- Rich: Terminal formatting
- Typer: CLI interface

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by JARVIS from Iron Man
- Built with open-source tools and libraries
- Community-driven development

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/ai-coding-assistant/issues) page
2. Create a new issue if needed
3. Join our community discussions

---

Made with ❤️ for developers everywhere 