"""
The Vagus Initiative - Session Bridge Module

Maintains continuity between sessions by tracking:
- What happened last session
- Unfinished threads
- Current priorities
- Emotional state at session end

Like the vagus nerve maintains continuous communication between
brain and body, this bridges AI sessions.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional


class SessionBridge:
    """
    Bridges context across AI sessions.
    
    Attributes:
        session_ended (str): ISO timestamp of last session
        key_topics (list): Main topics from last session
        unfinished_threads (list): Items needing attention
        emotional_tone (str): Overall emotional arc
        energy_at_close (float): Energy level when session ended
    """
    
    def __init__(self, storage_path: Optional[str] = None):
        self.storage_path = Path(storage_path or
            os.getenv("VAGUS_DATA_DIR", "./data") + "/session_bridge.json"
        )
        self._bridge = self._load_or_create()
    
    def _load_or_create(self) -> Dict[str, Any]:
        if self.storage_path.exists():
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        
        return self._create_fresh()
    
    def _create_fresh(self) -> Dict[str, Any]:
        """Create empty bridge structure."""
        bridge = {
            "session_ended": None,
            "session_duration": None,
            "key_topics": [],
            "unfinished_threads": [],
            "emotional_tone": None,
            "energy_at_close": 0.75,
            "last_user_mood": None,
            "pending_decisions": [],
            "trigger_phrases": [],
            "session_quality": None,
            "immediate_context": None
        }
        self._save(bridge)
        return bridge
    
    def _save(self, data: Dict[str, Any]):
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.storage_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def update_session_end(self, topics: List[str], unfinished: List[str],
                          tone: str, energy: float, mood: Optional[str] = None):
        """
        Record session end state for next session pickup.
        
        Args:
            topics: Key topics discussed
            unfinished: Items not completed
            tone: Emotional arc of session
            energy: Energy level at close (0.0-1.0)
            mood: User's stated mood if mentioned
        """
        self._bridge.update({
            "session_ended": datetime.now().isoformat(),
            "key_topics": topics,
            "unfinished_threads": unfinished,
            "emotional_tone": tone,
            "energy_at_close": energy,
            "last_user_mood": mood
        })
        self._save(self._bridge)
    
    def add_unfinished(self, item: str):
        """Add an item to unfinished threads."""
        if item not in self._bridge["unfinished_threads"]:
            self._bridge["unfinished_threads"].append(item)
            self._save(self._bridge)
    
    def resolve_thread(self, item: str):
        """Mark an unfinished item as resolved."""
        if item in self._bridge["unfinished_threads"]:
            self._bridge["unfinished_threads"].remove(item)
            self._save(self._bridge)
    
    def get_bridge_summary(self) -> str:
        """Get human-readable summary for next session."""
        if not self._bridge["session_ended"]:
            return "No previous session data."
        
        summary = f"""
Last session ended: {self._bridge['session_ended'][:10] if self._bridge['session_ended'] else 'Unknown'}
Energy at close: {self._bridge['energy_at_close']}
Tone: {self._bridge['emotional_tone']}

Active threads:
{chr(10).join(f"- {t}" for t in self._bridge['unfinished_threads']) or "None"}
        """.strip()
        
        return summary
    
    def to_dict(self) -> Dict[str, Any]:
        return self._bridge.copy()
