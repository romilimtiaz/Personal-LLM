import os
import ollama
import typer
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from typing import Optional

app = typer.Typer()
console = Console()

class CodingAgent:
    def __init__(self, model_name: str = "codellama"):
        self.model_name = model_name
        self.conversation_history = []
        
    def generate_response(self, prompt: str) -> str:
        """Generate a response using the local LLM."""
        try:
            response = ollama.generate(
                model=self.model_name,
                prompt=prompt,
                stream=False
            )
            return response['response']
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def process_command(self, command: str) -> str:
        """Process user commands and generate appropriate responses."""
        # Add command to history
        self.conversation_history.append(f"User: {command}")
        
        # Create a context-aware prompt
        context = "\n".join(self.conversation_history[-5:])  # Keep last 5 interactions
        prompt = f"""You are a helpful coding assistant. Previous conversation:
{context}

Current request: {command}

Please provide a helpful response focusing on coding and project management tasks."""
        
        response = self.generate_response(prompt)
        self.conversation_history.append(f"Assistant: {response}")
        return response

@app.command()
def main(
    model: str = typer.Option("codellama", help="Name of the Ollama model to use"),
    interactive: bool = typer.Option(True, help="Run in interactive mode")
):
    """Run the coding assistant agent."""
    console.print(Panel.fit(
        "[bold green]🤖 Welcome to your Local Coding Assistant![/bold green]\n"
        "I can help you with coding tasks and project management.\n"
        "Type 'exit' to quit.",
        title="Coding Assistant"
    ))
    
    agent = CodingAgent(model_name=model)
    
    if interactive:
        while True:
            command = Prompt.ask("\n[bold blue]What would you like me to do?[/bold blue]")
            
            if command.lower() in ['exit', 'quit']:
                console.print("[yellow]Goodbye! 👋[/yellow]")
                break
                
            with console.status("[bold green]Thinking..."):
                response = agent.process_command(command)
            
            console.print(Panel(response, title="Assistant"))

if __name__ == "__main__":
    app() 