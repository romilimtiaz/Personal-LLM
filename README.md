# Local Coding Assistant

A free, local AI coding assistant that helps you with coding tasks and project management. Available in both CLI and GUI versions.

## Prerequisites

1. Python 3.8 or higher
2. [Ollama](https://ollama.ai/) installed on your system

## Setup

1. Install Ollama:
   - Visit [Ollama's website](https://ollama.ai/) and download the installer for your operating system
   - Follow the installation instructions

2. Pull the CodeLlama model:
   ```bash
   ollama pull codellama
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### GUI Version (Recommended)
Run the GUI version:
```bash
python agent_gui.py
```

Features of the GUI version:
- Modern, user-friendly interface
- Real-time chat-like interaction
- Model selection dropdown
- Syntax-highlighted code display
- Error handling with popup messages

### CLI Version
Run the command-line version:
```bash
python agent.py
```

Both versions support:
- Writing code
- Project management assistance
- Code explanations
- And more!

## Features

- Completely local - no API costs
- Multiple model support (CodeLlama, Llama2, Mistral)
- Maintains conversation context
- Modern GUI interface
- Rich text formatting
- Real-time responses

## Customization

### GUI Version
- Select different models from the dropdown menu
- Modern, customizable interface
- Responsive design

### CLI Version
You can specify a different model when running the agent:
```bash
python agent.py --model modelname
```

Available models can be pulled using `ollama pull modelname`. 