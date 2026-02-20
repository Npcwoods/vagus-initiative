# Quick Start Guide

Get The Vagus Initiative running in 5 minutes.

## Prerequisites

- Python 3.8+
- pip

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/chriswoods/vagus-initiative.git
cd vagus-initiative
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or for development:

```bash
pip install -e .
```

### 3. Set Up Data Directory

```bash
mkdir -p data
export VAGUS_DATA_DIR=./data
```

## Your First Session

Create a file called `demo.py`:

```python
from vagus import EmotionalBaseline, TrustMap, SessionBridge
from datetime import datetime

# Initialize components
print("🌙 Initializing The Vagus Initiative...")
baseline = EmotionalBaseline()
trust = TrustMap()
bridge = SessionBridge()

# Check initial state
print(f"\n📊 Initial State:")
print(f"   Energy: {baseline.get('energy')}")
print(f"   Trust Depth: {trust.get_depth()}")

# Simulate an interaction
print(f"\n💬 Simulating session...")
print("   User: 'Let's plan the project roadmap'")
print("   AI: 'Great! I've been thinking about our priorities...'")

# Update state based on interaction
baseline.update({
    "energy": 0.85,
    "dominant_tone": "focused_collaboration",
    "focus": 0.90
})

trust.record_interaction(
    quality="exceptional",
    depth_change=0.05
)

# Mark session end with context
bridge.update_session_end(
    topics=["project_roadmap", "priorities", "timeline"],
    unfinished=[
        "Define Q2 milestones",
        "Review resource allocation",
        "Schedule stakeholder meeting"
    ],
    tone="focused_collaboration",
    energy=0.80,
    mood="energized"
)

print(f"\n📈 Updated State:")
print(f"   Energy: {baseline.get('energy')}")
print(f"   Tone: {baseline.get('dominant_tone')}")
print(f"   Trust Depth: {trust.get_depth()}")
print(f"   Unfinished: {len(bridge.to_dict()['unfinished_threads'])} items")

print(f"\n🌉 Session Bridge Summary:")
print(bridge.get_bridge_summary())

print("\n✅ Demo complete! Check ./data/ for generated state files.")
```

Run it:

```bash
python demo.py
```

## Next Session: Loading Context

Create `next_session.py`:

```python
from vagus import EmotionalBaseline, TrustMap, SessionBridge

# Components automatically load previous state
baseline = EmotionalBaseline()
trust = TrustMap()
bridge = SessionBridge()

print("🌅 New Session Started")
print(f"\n📊 Resumed State:")
print(f"   Energy: {baseline.get('energy')}")
print(f"   Tone: {baseline.get('dominant_tone')}")

print(f"\n🌉 Loading Context from Last Session:")
print(bridge.get_bridge_summary())

print(f"\n💬 AI: 'Good morning! Last time we were planning the project roadmap.")
print(f"      You still have {len(bridge.to_dict()["unfinished_threads"])} items on your list.")
print(f"      Want to pick up where we left off?'")
```

## Understanding the Output

### Emotional Baseline
Shows the AI's current "mood":
- **Energy**: How activated/aroused (0.0-1.0)
- **Warmth**: How relational/connected (0.0-1.0)
- **Focus**: How task-oriented (0.0-1.0)
- **Tone**: Qualitative description

### Trust Map
Tracks relationship evolution:
- **Depth**: Overall relationship strength (0.0-1.0)
- **Interaction Count**: Total exchanges
- **Quality**: Recent interaction ratings

### Session Bridge
Provides session continuity:
- **Key Topics**: What was being discussed
- **Unfinished Threads**: Pending items
- **Energy at Close**: How the last session ended

## Configuration Options

### Environment Variables

```bash
# Data storage location
export VAGUS_DATA_DIR=/path/to/data

# Memory/conversation storage
export VAGUS_MEMORY_DIR=/path/to/memory

# Dream cycle output
export VAGUS_DREAM_DIR=/path/to/dreams
```

### Direct Path Configuration

```python
from vagus import EmotionalBaseline

# Specify exact paths
baseline = EmotionalBaseline(
    storage_path="/custom/path/my_baseline.json"
)
```

## Template Files

Copy from `templates/` to create fresh state:

```bash
cp templates/emotional_baseline_template.json data/emotional_baseline.json
cp templates/trust_map_template.json data/trust_map.json
cp templates/session_bridge_template.json data/session_bridge.json
```

## Running the Dream Cycle

The Dream Cycle processes daily interactions:

```python
from vagus.dream_cycle import DreamCycle

cycle = DreamCycle()
results = cycle.run()

print(f"Processed {results['memories_processed']} memories")
print(f"Dream saved to: {results['dream_path']}")
```

Or from command line:

```bash
python -m vagus.dream_cycle
```

## Common Patterns

### Pattern 1: Energy-Based Response Modulation

```python
energy = baseline.get("energy")

if energy > 0.8:
    response_style = "energetic and fast-paced"
elif energy > 0.5:
    response_style = "measured and thoughtful"
else:
    response_style = "gentle and supportive"
```

### Pattern 2: Trust-Based Familiarity

```python
depth = trust.get_depth()

if depth > 0.8:
    greeting = "Hey! Good to see you again."
elif depth > 0.5:
    greeting = "Hello! Welcome back."
else:
    greeting = "Hello. How can I help you today?"
```

### Pattern 3: Contextual Session Pickup

```python
unfinished = bridge.to_dict()["unfinished_threads"]

if unfinished:
    print(f"Last time you mentioned wanting to work on: {unfinished[0]}")
    print("Should we start there?")
else:
    print("What would you like to work on today?")
```

## Troubleshooting

### State Not Persisting

Check that `VAGUS_DATA_DIR` is set and the directory exists:

```bash
ls -la $VAGUS_DATA_DIR
```

### Import Errors

Make sure you're in the project root or have installed with `pip install -e .`

### Templates Not Working

Ensure JSON syntax is valid:

```bash
python -m json.tool templates/emotional_baseline_template.json
```

## Next Steps

- Read [Architecture Overview](architecture.md) for deep dive
- Check [examples/](../examples/) for more usage patterns
- See [CONTRIBUTING.md](../CONTRIBUTING.md) to contribute

---

*Questions? Open an issue or join the discussion.*
