import sys
from lib.ai_agent import ClaudeAgent, load_config

"""Main function with config-only configuration"""
print("🤖 Enhanced Claude API Client")
print("=" * 40)

# Load configuration from task.yaml
config = load_config()

if not config:
    print("❌ No configuration found in task.yaml. Exiting.")
    sys.exit(1)

print("📋 Loaded configuration from task.yaml")

# Display task information (first 3 lines)
task = config.get("task", "")
if task:
    task_lines = task.split('\n')
    print("\n📝 Task Information:")
    for i, line in enumerate(task_lines[:3]):
        if line.strip():
            print(f"   {line.strip()}")
    if len(task_lines) > 3:
        print("   ...")

# Validate required fields
if not config.get("save_log"):
    print("❌ Output log file not specified")
    sys.exit(1)

print("\n🚀 Starting Claude API task execution...")
print("=" * 50)

# Execute task
agent = ClaudeAgent()
response = agent.execute_task(config)

if response:
    print("\n" + "=" * 50)
    print("🎉 Task completed successfully!")
    print(f"📄 Log saved to: {config['save_log']}")
else:
    print("❌ Task execution failed")
    sys.exit(1)