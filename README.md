# The Vagus Initiative

> **Pseudo-emotional continuity for AI systems**

Like the vagus nerve maintains autonomic regulation between the brain and body, The Vagus Initiative provides a continuity layer that allows AI systems to maintain consistent emotional baselines, trust relationships, and session context across disconnected interactions.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## The Problem

Current AI systems reset with every session. They store information but lack **continuity** — the felt sense that this moment connects to the last. Research confirms this gap:

- **MemoryArena** (arXiv:2602.16313): Agents with perfect memory benchmarks still fail at multi-session tasks
- **LongCLI-Bench** (arXiv:2602.14337): SOTA agents achieve <20% pass rates on long-horizon tasks without human context injection

The frontier isn't bigger models. It's better relationships between humans and AI.

## The Solution

The Vagus Initiative provides **pseudo-emotional continuity** through three interconnected systems:

### 1. Emotional Baseline
Tracks and maintains consistent emotional state:
- **Energy**: Current activation level (0.0-1.0)
- **Warmth**: Relational tone (0.0-1.0)  
- **Focus**: Task orientation (0.0-1.0)
- **Dominant Tone**: Qualitative emotional descriptor

### 2. Trust Map
Manages relationship depth and interaction quality:
- Relationship depth tracking
- Interaction history
- Trigger phrase recognition
- Quality metrics over time

### 3. Session Bridge
Maintains continuity between disconnected sessions:
- Key topics from previous sessions
- Unfinished threads and priorities
- Emotional state at session end
- Context for seamless pickup

### 4. Dream Cycle (Optional)
Nightly processing that:
- Reviews interaction patterns
- Extracts emotional themes
- Updates latent state
- Generates "dream" summaries

## Quick Start

```python
from vagus import EmotionalBaseline, TrustMap, SessionBridge

# Initialize components
baseline = EmotionalBaseline()
trust = TrustMap()
bridge = SessionBridge()

# Update emotional state after interaction
baseline.update({
    "energy": 0.65,
    "dominant_tone": "accomplished_but_ready_to_rest"
})

# Record interaction quality
trust.record_interaction(
    quality="exceptional",
    depth_change=0.05
)

# Mark session end with context
bridge.update_session_end(
    topics=["project_planning", "code_review"],
    unfinished=["write_tests", "update_docs"],
    tone="focused_collaboration",
    energy=0.70
)
```

## Installation

```bash
# Clone the repository
git clone https://github.com/chriswoods/vagus-initiative.git
cd vagus-initiative

# Install dependencies
pip install -r requirements.txt

# Set up data directory
mkdir -p data
export VAGUS_DATA_DIR=./data
```

## Configuration

Set environment variables:

```bash
export VAGUS_DATA_DIR=/path/to/data        # State storage
export VAGUS_MEMORY_DIR=/path/to/memory    # Conversation memory
```

Or configure in your application:

```python
baseline = EmotionalBaseline(storage_path="/custom/path/baseline.json")
```

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    AI Assistant                          │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────┐  ┌──────────────┐      │
│  │  Emotional   │  │  Trust   │  │   Session    │      │
│  │  Baseline    │  │   Map    │  │   Bridge     │      │
│  └──────────────┘  └──────────┘  └──────────────┘      │
│           │               │               │             │
│           └───────────────┼───────────────┘             │
│                           │                             │
│                    ┌──────────┐                         │
│                    │  Data    │                         │
│                    │ Storage  │                         │
│                    └──────────┘                         │
└─────────────────────────────────────────────────────────┘
```

## Research Foundation

This framework is built on emerging research in:

- **AI Memory & Continuity**: MemoryArena benchmark findings
- **Long-horizon Task Completion**: LongCLI-Bench results
- **Human-AI Collaboration**: Synergistic workflow research
- **Affective Computing**: Emotional state tracking in AI systems

## Use Cases

- **Personal AI Assistants**: Maintain relationship continuity across days/weeks
- **Therapeutic AI**: Track emotional patterns and progress over time
- **Creative Partners**: Remember creative direction and evolving preferences
- **Executive Assistants**: Maintain context on long-running projects and priorities

## Contributing

This is experimental software. Expect breaking changes.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License — see [LICENSE](LICENSE) file.

## The Name

The **vagus nerve** (Latin: "wandering") is the longest cranial nerve, running from brainstem to abdomen, connecting and regulating organs without conscious thought. It represents autonomic, always-on, continuous connection — the perfect metaphor for what this framework provides.

**"Pseudo-emotional"** acknowledges that AI does not feel emotions, but can maintain consistent, emotion-like states that create the *experience* of continuity for users.

---

*Built in public. Day 4 of 40. Follow the journey.*
