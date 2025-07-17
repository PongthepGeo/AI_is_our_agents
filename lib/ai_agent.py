import anthropic
import sys
import os
import yaml
import time
import threading
from typing import Optional, Dict, Any
from datetime import datetime

class ProgressIndicator:
    """Simple progress indicator to show the program is working"""
    def __init__(self, message="Processing"):
        self.message = message
        self.is_running = False
        self.thread = None
        self.chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    
    def start(self):
        """Start the progress indicator"""
        self.is_running = True
        self.thread = threading.Thread(target=self._animate)
        self.thread.daemon = True
        self.thread.start()
    
    def stop(self):
        """Stop the progress indicator"""
        self.is_running = False
        if self.thread:
            self.thread.join()
        print("\r", end="")  # Clear the line
    
    def _animate(self):
        """Animate the progress indicator"""
        idx = 0
        while self.is_running:
            print(f"\r{self.chars[idx]} {self.message}...", end="", flush=True)
            idx = (idx + 1) % len(self.chars)
            time.sleep(0.1)

class ClaudeAgent:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize Claude agent with API key"""
        self.api_key = "change here"
        
        self.client = anthropic.Anthropic(api_key=self.api_key)

        ''' 
        1) Claude 3.5 Sonnet - Best for coding and complex tasks
        2) Claude 3 Opus - Best for reasoning and analysis
        3) Claude 3 Haiku - Fast and efficient responses
        4) Claude 3 Sonnet - Balanced performance
        '''
        self.available_models = {
            "claude-3-5-sonnet-20241022",
            "claude-3-opus-20240229",
            "claude-3-haiku-20240307",
            "claude-3-sonnet-20240229"
        }
        
        # Model type configurations
        self.model_types = {
            "coding": {
                "default_model": "claude-3-5-sonnet-20241022",
                "temperature": 0.1,
                "max_tokens": 4000,
                "description": "Optimized for code generation and programming tasks"
            },
            "creative": {
                "default_model": "claude-3-5-sonnet-20241022",
                "temperature": 0.7,
                "max_tokens": 4000,
                "description": "Best for creative writing and brainstorming"
            },
            "analytical": {
                "default_model": "claude-3-opus-20240229",
                "temperature": 0.3,
                "max_tokens": 4000,
                "description": "Ideal for analysis and reasoning tasks"
            },
            "fast": {
                "default_model": "claude-3-haiku-20240307",
                "temperature": 0.5,
                "max_tokens": 2000,
                "description": "Quick responses for simple tasks"
            }
        }
        
        # Re‑organized system prompts (five entries)

        self.system_prompts = {"custom": "You are a helpful AI assistant."}

    def create_response(self, task: str, model: str, model_type: str = "coding", system_prompt: Optional[str] = None) -> str:
        """Create a response using Claude with specified configuration"""
        
        # Get model type configuration
        type_config = self.model_types.get(model_type, self.model_types["coding"])
        
        # Use provided system prompt or default for model type
        if system_prompt is None:
            system_prompt = self.system_prompts.get(model_type, self.system_prompts["general"])
        
        messages = [{"role": "user", "content": task}]
        
        try:
            # Start progress indicator
            progress = ProgressIndicator(f"Generating response with {model}")
            progress.start()
            
            # Create message with system prompt
            kwargs = {
                "model": model,
                "max_tokens": type_config["max_tokens"],
                "temperature": type_config["temperature"],
                "messages": messages,
                "system": system_prompt
            }
            
            message = self.client.messages.create(**kwargs)
            
            # Stop progress indicator
            progress.stop()
            
            return message.content[0].text
            
        except Exception as e:
            progress.stop()
            print(f"❌ Error creating response: {e}")
            return f"Error: {str(e)}"
    
    def execute_task(self, config: Dict[str, Any]) -> Optional[str]:
        """Execute a task based on configuration"""
        try:
            # Get task from config instead of reading from file
            task = config.get("task", "")
            
            if not task:
                print("❌ Task not found in configuration")
                return None
            
            print(f"📝 Task length: {len(task)} characters")
            
            start_time = time.time()
            
            # Generate response
            response = self.create_response(
                task=task,
                model=config["model"],
                model_type=config["model_type"],
                system_prompt=config.get("system_prompt")
            )
            
            execution_time = time.time() - start_time
            
            # Prepare output content
            output_content = []
            
            if config.get("include_metadata", True):
                metadata = {
                    "output_file": config["save_log"],
                    "model_used": config["model"],
                    "model_type": config["model_type"],
                    "execution_time": f"{execution_time:.2f} seconds",
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "temperature": self.model_types[config["model_type"]]["temperature"],
                    "max_tokens": self.model_types[config["model_type"]]["max_tokens"]
                }
                
                output_content.append("# Claude API Execution Log\n\n")
                output_content.append("## Execution Metadata\n\n")
                for key, value in metadata.items():
                    output_content.append(f"- **{key.replace('_', ' ').title()}**: {value}\n")
                output_content.append("\n## Task Response\n\n")
            
            output_content.append(response)
            
            # Write to file
            output_file = config["save_log"]
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(''.join(output_content))
            
            print(f"✅ Task completed successfully!")
            print(f"📁 Output saved to: {output_file}")
            print(f"🤖 Model used: {config['model']}")
            print(f"📋 Model type: {config['model_type']}")
            print(f"⏱️  Execution time: {execution_time:.2f} seconds")
            
            return response
            
        except Exception as e:
            print(f"❌ Error executing task: {e}")
            return None

def load_config(config_file: str = "task.yaml") -> Dict[str, Any]:
    """Load configuration from YAML file"""
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        if config is None:
            config = {}
        
        return config
        
    except FileNotFoundError:
        print(f"📋 Config file '{config_file}' not found.")
        return {}
    except Exception as e:
        print(f"❌ Error parsing config: {e}")
        return {}

def save_config(config: Dict[str, Any], config_file: str = "config.yaml"):
    """Save configuration to YAML file"""
    try:
        with open(config_file, 'w', encoding='utf-8') as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)
        print(f"💾 Configuration saved to: {config_file}")
    except Exception as e:
        print(f"❌ Error saving config: {e}")

def get_user_input(prompt: str, options: Dict[str, str] = None, default: str = None) -> str:
    """Get user input with options display"""
    if options:
        print(f"\n{prompt}")
        for key, value in options.items():
            print(f"  {key}: {value}")
        if default:
            choice = input(f"\nEnter your choice (default: {default}): ").strip()
            return choice if choice else default
        else:
            return input(f"\nEnter your choice: ").strip()
    else:
        if default:
            result = input(f"{prompt} (default: {default}): ").strip()
            return result if result else default
        else:
            return input(f"{prompt}: ").strip()