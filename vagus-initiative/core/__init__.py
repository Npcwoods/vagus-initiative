"""
The Vagus Initiative

A continuity framework for AI systems that provides pseudo-emotional
memory and relationship persistence across sessions.

Like the vagus nerve maintains autonomic regulation in the human body,
The Vagus Initiative maintains consistent emotional baselines, trust maps,
and session continuity for AI assistants.

Core Modules:
- EmotionalBaseline: Tracks energy, warmth, focus, and tone
- TrustMap: Manages relationship depth and interaction quality
- SessionBridge: Bridges context between sessions

Usage:
    from vagus import EmotionalBaseline, TrustMap, SessionBridge
    
    baseline = EmotionalBaseline()
    baseline.update({"energy": 0.8, "dominant_tone": "focused"})
"""

from .emotional_baseline import EmotionalBaseline
from .trust_map import TrustMap
from .session_bridge import SessionBridge

__version__ = "0.1.0"
__author__ = "Chris Woods"
__license__ = "MIT"

__all__ = [
    "EmotionalBaseline",
    "TrustMap", 
    "SessionBridge"
]
