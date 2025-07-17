# Claude AI Agent for Geoscience Research

A Python-based AI agent specialized for geoscience research, satellite data analysis, and scientific publication writing. Built with Anthropic's Claude models for geophysics, geology, and earth observation workflows.

## 🚀 Quick Start

### 1. Prerequisites
```bash
pip install -r requirements.txt
```

### 2. API Key Setup
1. Create account at [Anthropic Console](https://console.anthropic.com/)
2. Generate API key
3. Update `lib/ai_agent.py` line 43:
```python
# Replace this line in lib/ai_agent.py:
self.api_key = "change here"

# With your actual API key:
self.api_key = "sk-your-api-key-here"
```

### 3. First Execution
```bash
python 01_api_claude.py
```

## ⚙️ Configuration Guide

### Basic `task.yaml` Template
```yaml
model: claude-3-5-sonnet-20241022
model_type: coding
system_prompt: "You are a geophysics expert specializing in satellite data analysis."
save_log: output.md
task: |
  Analyze seismic data from the recent earthquake event:
  - Process time-series data
  - Calculate magnitude and depth
  - Generate visualization plots
```

### Model Selection Guide for Geoscience
| Model                      | Best For                  | Geoscience Use Cases      | Cost |
|----------------------------|---------------------------|---------------------------|------|
| `claude-3-5-sonnet-20241022` | Coding & complex analysis | Seismic processing, GIS analysis | ★★★☆☆ |
| `claude-3-opus-20240229`   | Research & publications   | Journal writing, data interpretation | ★☆☆☆☆ |
| `claude-3-haiku-20240307`  | Quick data tasks          | Data cleaning, simple plots | ★★★★★ |
| `claude-3-sonnet-20240229` | Balanced workflows        | General geoscience tasks | ★★★★☆ |

## 🔧 Geoscience Configuration Levels

### Beginner Level - Satellite Data Analysis
```yaml
model: claude-3-5-sonnet-20241022
model_type: coding
system_prompt: "You are a remote sensing expert specializing in satellite imagery analysis."
save_log: satellite_analysis.md
task: |
  Process Landsat 8 imagery for vegetation index calculation:
  - Load and preprocess bands 4 and 5
  - Calculate NDVI
  - Create visualization with matplotlib
```

### Intermediate Level - Geophysical Modeling
```yaml
model: claude-3-opus-20240229
model_type: analytical
system_prompt: |
  You are a geophysics expert with expertise in:
  - Seismic wave propagation
  - Gravity and magnetic field analysis
  - Subsurface imaging techniques
  - Python scientific computing (NumPy, SciPy, ObsPy)
save_log: geophysics_model.md
task: |
  Create a 1D seismic wave propagation model:
  - Define velocity structure
  - Implement finite difference scheme
  - Generate synthetic seismograms
```

### Advanced Level - Scientific Publication
```yaml
model: claude-3-opus-20240229
model_type: creative
system_prompt: |
  You are a senior geoscientist writing for peer-reviewed journals:
  - Follow standard scientific writing conventions
  - Use precise geological terminology
  - Include proper citations and references
  - Structure: Abstract, Introduction, Methods, Results, Discussion
  - Target journals: Nature Geoscience, JGR, Geophysics
save_log: manuscript_draft.md
task: |
  Write a research paper on machine learning applications in earthquake prediction:
  - Literature review of recent advances
  - Methodology using neural networks
  - Results from case study analysis
  - Discussion of implications and limitations
```

**Model Types for Geoscience:**
- **coding**: Temperature 0.1, Max tokens 4000 - Python scripts, data processing
- **analytical**: Temperature 0.3, Max tokens 4000 - Data interpretation, modeling
- **creative**: Temperature 0.7, Max tokens 4000 - Scientific writing, proposals
- **fast**: Temperature 0.5, Max tokens 2000 - Quick calculations, simple plots

### Expert Level - Custom Model Configurations

For advanced users, modify the model configurations in `lib/ai_agent.py`:

```python
# In lib/ai_agent.py, modify the model_types dictionary
self.model_types = {
    "fast": {
        "default_model": "claude-3-haiku-20240307",
        "temperature": 0.5,
        "max_tokens": 2000,
        "description": "Quick responses for simple tasks"
    },
    "custom_research": {
        "default_model": "claude-3-opus-20240229",
        "temperature": 0.2,
        "max_tokens": 6000,
        "description": "Deep research and analysis"
    }
}
```

## Understanding Temperature and Max Tokens

### Temperature (0.0 - 1.0)
Controls response randomness and creativity:
- **Low (0.0-0.3)**: More deterministic, focused, consistent
  - Best for: Code generation, factual answers, technical documentation
- **Medium (0.4-0.6)**: Balanced creativity and consistency
  - Best for: General tasks, explanations, problem-solving
- **High (0.7-1.0)**: More creative, varied, unpredictable
  - Best for: Creative writing, brainstorming, artistic tasks

### Max Tokens
Controls response length and complexity:
- **Small (1000-2000)**: Short, concise responses
  - Best for: Quick answers, simple tasks, cost optimization
- **Medium (2000-4000)**: Standard responses with detail
  - Best for: Most general tasks, tutorials, explanations
- **Large (4000+)**: Long, comprehensive responses
  - Best for: Complex analysis, detailed documentation, research

### Relationship Between Temperature and Max Tokens
- **Higher temperature + More tokens**: More creative, longer responses
- **Lower temperature + Fewer tokens**: Focused, concise responses
- **Balance**: Medium temperature (0.3-0.5) + Medium tokens (2000-4000) for most tasks

## Optimization Guide

### Model Selection Strategy

**Cost vs Performance Trade-offs:**

1. **Budget-Friendly (Haiku)**
   - Use for: Simple tasks, quick responses, high-volume operations
   - Cost: Lowest
   - Speed: Fastest

2. **Balanced (Sonnet)**
   - Use for: General tasks, moderate complexity
   - Cost: Medium
   - Speed: Moderate

3. **Premium (Opus/Sonnet-3.5)**
   - Use for: Complex analysis, coding, critical tasks
   - Cost: Higher (requires paid credits)
   - Speed: Slower but higher quality

### Temperature Optimization

**Task-Specific Recommendations:**

```python
# Code generation
"coding": {"temperature": 0.1, "max_tokens": 4000}

# Data analysis
"analytical": {"temperature": 0.3, "max_tokens": 4000}

# Creative writing
"creative": {"temperature": 0.7, "max_tokens": 4000}

# Quick responses
"fast": {"temperature": 0.5, "max_tokens": 2000}
```

### Token Optimization

**Strategies to reduce costs:**
1. Start with lower token limits and increase if needed
2. Use concise prompts and system messages
3. Break complex tasks into smaller chunks
4. Monitor token usage in output logs

### Model Upgrade Strategy

**When to use advanced models:**
- Complex reasoning tasks → Claude-3-Opus
- Advanced coding → Claude-3.5-Sonnet
- Production applications → Premium models
- High-stakes analysis → Premium models with low temperature

**Credit Management:**
- Premium models (Opus, Sonnet-3.5) require paid credits
- Monitor usage through Anthropic console
- Set up billing alerts for cost control
- Use Haiku for development/testing

## File Structure

```
02_ai_agent/
├── 01_api_claude.py      # Main execution script
├── lib/
│   └── ai_agent.py       # Core ClaudeAgent class
├── task.yaml             # Configuration file
├── README.md             # This tutorial
└── prompt.md             # Task instructions
```

## Key Features

### ClaudeAgent Class (`lib/ai_agent.py`)

**Core Methods:**
- `create_response()` - Generate AI responses with specified model and prompts
- `execute_task()` - Execute tasks based on configuration
- `load_config()` - Load YAML configuration files

**Configuration Options:**
- Model selection from available Claude models
- Temperature and token limits per model type
- Custom system prompts for domain-specific tasks
- Metadata logging and execution tracking

### Main Script (`01_api_claude.py`)

**Features:**
- Loads configuration from `task.yaml`
- Validates required fields
- Displays task information and execution progress
- Saves responses with metadata to specified output file

## Complete Example

1. **Create task.yaml:**
   ```yaml
   model: claude-3-5-sonnet-20241022
   model_type: coding
   system_prompt: "You are an expert Python developer."
   save_log: coding_output.md
   include_metadata: true
   task: |
     Create a Python class for a simple banking system with:
     1. Account creation
     2. Deposit and withdrawal methods
     3. Balance inquiry
     4. Transaction history
   ```

2. **Run the agent:**
   ```bash
   python 01_api_claude.py
   ```

3. **Output:** The response will be saved to `coding_output.md` with execution metadata.

## Advanced Customization

### Adding New Model Types

To add a new model type, modify the `model_types` dictionary in `lib/ai_agent.py`:

```python
"specialized_task": {
    "default_model": "claude-3-5-sonnet-20241022",
    "temperature": 0.4,
    "max_tokens": 3000,
    "description": "Specialized for specific domain tasks"
}
```

### Custom System Prompts

Add domain-specific system prompts to the `system_prompts` dictionary:

```python
"geophysics_expert": """You are a geophysics expert.
1. Provide accurate scientific explanations
2. Use appropriate mathematical formulations
3. Include practical applications
4. Reference relevant literature when appropriate
5. Explain complex concepts clearly
"""
```

## Error Handling

The agent includes comprehensive error handling:
- Configuration validation
- API error management
- Progress indicators during processing
- Detailed logging and metadata tracking

## Tips for Effective Usage

1. **Start Simple:** Begin with basic configurations and gradually add complexity
2. **Test Prompts:** Experiment with different system prompts for your use case
3. **Monitor Costs:** Use Haiku for testing, premium models for production
4. **Optimize Parameters:** Adjust temperature and tokens based on task requirements
5. **Track Usage:** Enable metadata logging to monitor token consumption and costs
6. **Iterate:** Refine your prompts based on output quality and cost efficiency

This tutorial provides a complete guide to using the AI agent effectively across different skill levels and use cases while managing costs and optimizing performance.