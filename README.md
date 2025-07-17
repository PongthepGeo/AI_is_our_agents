# 🌎 Claude AI Agent for Geoscience Research

A Python-based AI agent specialized in geoscience research, satellite data analysis, and scientific publication writing. Built with Anthropic's Claude models tailored specifically for geophysics (including mineral and petroleum exploration), geology, and earth observation workflows.

## 📊 Overview

<img src="overview.svg" alt="Overview" width="100%" />

*Interactive workflow diagram available at: https://boardmix.com/app/share/CAE.CKqMjAEgASoQK-glKOYYTmbWISTukdYbhTAGQAE/Yx6Vou*

---

## 🚀 Quick Start

### 1. Installation

```bash
git clone https://github.com/PongthepGeo/AI_is_our_agents.git
cd AI_is_our_agents/02_ai_agent
pip install -r requirements.txt
```

### 2. API Key Setup

1. Create an account at [Anthropic Console](https://console.anthropic.com/)
2. Generate your API key
3. Update `lib/ai_agent.py` (line 43):

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

---

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

### ⚖️ Model Selection Guide for Geoscience

| Model                        | Best For                  | Geoscience Use Cases                     | Cost  | Speed |
| ---------------------------- | ------------------------- | ---------------------------------------- | ----- | ----- |
| `claude-3-5-sonnet-20241022` | Coding & complex analysis | Seismic processing, GIS, modeling        | ★★★☆☆ | ⚡⚡⚡⚡  |
| `claude-3-opus-20240229`     | Research & publications   | Journal writing, complex interpretations | ★☆☆☆☆ | ⚡⚡    |
| `claude-3-haiku-20240307`    | Quick tasks               | Data cleaning, basic plotting            | ★★★★★ | ⚡⚡⚡⚡⚡ |
| `claude-3-sonnet-20240229`   | Balanced workflows        | General geoscience analyses              | ★★★★☆ | ⚡⚡⚡⚡  |

---

## 🔧 Geoscience Configuration Levels

### Beginner Level – Satellite Data Analysis

```yaml
model: claude-3-5-sonnet-20241022
model_type: coding
system_prompt: "You are a remote sensing expert specializing in satellite imagery analysis."
save_log: satellite_analysis.md
task: |
  Process Landsat 8 imagery for vegetation index calculation:
  - Load and preprocess bands 4 and 5
  - Calculate NDVI
  - Visualize results with matplotlib
```

### Intermediate Level – Geophysical Modeling

```yaml
model: claude-3-opus-20240229
model_type: analytical
system_prompt: |
  You are a geophysics expert specialized in:
  - Seismic wave propagation
  - Gravity & magnetic field analyses
  - Subsurface imaging (minerals, petroleum)
  - Python scientific computing (NumPy, SciPy, ObsPy)
save_log: geophysics_model.md
task: |
  Create a 1D seismic wave propagation model:
  - Define velocity structure
  - Implement finite difference scheme
  - Generate synthetic seismograms
```

### Advanced Level – Scientific Publication

```yaml
model: claude-3-opus-20240229
model_type: creative
system_prompt: |
  You are a senior geoscientist writing for peer-reviewed journals:
  - Follow standard scientific writing conventions
  - Use precise geological terminology
  - Include proper citations
  - Structure: Abstract, Introduction, Methods, Results, Discussion
  - Target journals: Nature Geoscience, JGR, Geophysics
save_log: manuscript_draft.md
task: |
  Write a research paper on machine learning applications in earthquake prediction:
  - Literature review
  - Neural network methodology
  - Case study analysis
  - Discussion of implications and limitations
```

---

## 🔥 Optimization Guide

### Model Selection Strategy

| Strategy        | Use for                             | Cost   | Speed |
| --------------- | ----------------------------------- | ------ | ----- |
| Budget-Friendly | Simple tasks, high-volume           | Lowest | ⚡⚡⚡⚡⚡ |
| Balanced        | General workflows                   | Medium | ⚡⚡⚡⚡  |
| Premium         | Critical, complex analyses & coding | Higher | ⚡⚡    |

### Temperature & Max Tokens

**Temperature:**

* **Low (0.0-0.3)**: Coding, technical documentation
* **Medium (0.4-0.6)**: General analysis, explanations
* **High (0.7-1.0)**: Creative writing, research ideation

**Max Tokens:**

* **Small (1000-2000)**: Quick tasks, concise responses
* **Medium (2000-4000)**: Most analyses, tutorials
* **Large (4000+)**: Detailed research and documentation

---

## 📂 Project File Structure

```
02_ai_agent/
├── 01_api_claude.py      # Main execution script
├── lib/
│   └── ai_agent.py       # Core ClaudeAgent class
├── task.yaml             # Task configuration
├── README.md             # Project documentation
└── prompt.md             # Task instructions
```

---

## ⚙️ Advanced Customization

### Add Custom Model Types (`lib/ai_agent.py`)

```python
"mineral_exploration": {
    "default_model": "claude-3-5-sonnet-20241022",
    "temperature": 0.2,
    "max_tokens": 5000,
    "description": "Specialized for mineral & petroleum exploration"
}
```

### Custom System Prompts

```python
"geophysics_expert": """You are a geophysics expert specializing in mineral and petroleum exploration:
1. Provide scientific explanations
2. Use geological and geophysical terminology
3. Reference relevant studies
4. Clearly explain complex methods"""
```

---

## ✅ Error Handling

* Configuration validation
* API error management
* Progress indicators during processing
* Detailed logging and metadata tracking

---

## 🎯 Tips for Effective Usage

1. **Iterate prompts:** Refine prompts based on output
2. **Monitor usage:** Track tokens and manage costs
3. **Optimize models:** Start small, scale as needed
4. **Temperature control:** Adjust based on task complexity
