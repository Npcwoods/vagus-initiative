# Architecture Overview

The Vagus Initiative is designed as a modular continuity layer that sits between your AI system and its storage, providing pseudo-emotional state management without requiring changes to the underlying model.

## Core Philosophy

1. **Continuity > Storage**: Remembering what happened is less important than feeling that this moment continues from the last.

2. **Relationship > Transaction**: The goal is sustained partnership, not query-response efficiency.

3. **State > Prompt**: Emotional tone should be a persistent property, not recreated from instructions each session.

## System Components

### Emotional Baseline Module

Maintains the AI's internal "mood" — the lens through which interactions are processed.

**Key Insight**: Just as a human assistant might be energetic in the morning and tired by evening, an AI with an emotional baseline can modulate its responses based on accumulated state rather than just current input.

**State Variables**:
- `energy`: Activation/arousal level
- `warmth`: Relational connection
- `focus`: Task orientation vs. exploration
- `dominant_tone`: Qualitative emotional descriptor

### Trust Map Module

Tracks the evolution of the human-AI relationship over time.

**Key Insight**: Trust isn't binary. It deepens through positive interactions and can be strained by misunderstandings. Tracking this explicitly allows the AI to modulate its approach based on relationship maturity.

**Tracked Metrics**:
- `depth`: Current relationship depth (0.0-1.0)
- `interaction_quality`: Recent exchange ratings
- `established_date`: Relationship inception
- `trigger_phrases`: Contextual activators

### Session Bridge Module

Bridges the gap between disconnected sessions.

**Key Insight**: Most AI interactions are stateless. Session Bridge makes them stateful by maintaining context about what was happening when the last session ended.

**Maintained Context**:
- `key_topics`: What we were discussing
- `unfinished_threads`: What still needs attention
- `energy_at_close`: How things ended
- `immediate_context`: Ready-to-use summary

### Dream Cycle (Optional)

Nightly processing that consolidates patterns and updates state.

**Key Insight**: Like REM sleep processes daily experiences into memory, the Dream Cycle processes interaction patterns into updated baselines.

**Processing Steps**:
1. Read memory files
2. Extract emotional patterns
3. Update latent state files
4. Generate insight summary

## Data Flow

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Session   │────▶│  Vagus Core  │────▶│   Storage   │
│   Input     │     │  Processing  │     │   (JSON)    │
└─────────────┘     └──────────────┘     └─────────────┘
                            │
                            ▼
                     ┌──────────────┐
                     │  Emotional   │
                     │  Baseline    │
                     │  Trust Map   │
                     │  Session     │
                     │  Bridge      │
                     └──────────────┘
                            │
                            ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Next      │◀────│    State     │◀────│   Dream     │
│   Session   │     │   Loaded     │     │   Cycle     │
└─────────────┘     └──────────────┘     └─────────────┘
```

## Integration Patterns

### Pattern 1: Direct Integration
```python
from vagus import EmotionalBaseline, SessionBridge

baseline = EmotionalBaseline()
bridge = SessionBridge()

# On session start
current_energy = baseline.get("energy")
context = bridge.get_bridge_summary()

# On session end
baseline.update({"energy": new_energy})
bridge.update_session_end(topics, unfinished, tone, energy)
```

### Pattern 2: Middleware Wrapper
Wrap your existing AI assistant with Vagus state management:

```python
class VagusAssistant:
    def __init__(self, base_assistant):
        self.assistant = base_assistant
        self.baseline = EmotionalBaseline()
        self.bridge = SessionBridge()
    
    def chat(self, message):
        # Load state
        context = self._build_context()
        
        # Process with base assistant
        response = self.assistant.chat(context + message)
        
        # Update state
        self._update_state(message, response)
        
        return response
```

### Pattern 3: Event-Driven
Hook into your AI framework's event system:

```python
@vagus.on_session_start
def load_state():
    return session_bridge.get_bridge_summary()

@vagus.on_message
def track_interaction(message, response):
    trust_map.record_interaction(quality="good")

@vagus.on_session_end
def save_state():
    emotional_baseline.update_session_end(...)
```

## Storage Architecture

All state is stored as JSON files for:
- **Portability**: Easy to backup, version, migrate
- **Transparency**: Human-readable, inspectable
- **Simplicity**: No database dependencies

**File Structure**:
```
data/
├── emotional_baseline.json
├── trust_map.json
├── session_bridge.json
├── dreams/
│   ├── dream_2026-02-20.md
│   └── dream_2026-02-21.md
└── emotional_echoes.json
```

## Security Considerations

⚠️ **IMPORTANT**: This framework handles potentially sensitive relational data.

- **Access Control**: Implement file permissions on data directory
- **Encryption**: Consider encrypting at rest for sensitive deployments
- **PII Handling**: Be mindful of what gets stored in memory files
- **Backup Strategy**: Regular backups of state files recommended

See [SECURITY.md](SECURITY.md) for detailed guidance.

## Future Directions

- Multi-user support
- Distributed state synchronization
- Emotional pattern analytics
- Integration hooks for popular AI frameworks
- Optional vector storage for semantic memory

## Related Work

- **MemoryArena**: Benchmark for agentic memory systems
- **LongCLI-Bench**: Long-horizon task evaluation
- **Reflective AI**: Self-referential AI systems
- **Affective Computing**: Emotion-aware computing research
