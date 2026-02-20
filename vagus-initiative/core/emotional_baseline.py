"""
The Vagus Initiative - Emotional Baseline Module

This module tracks and manages the emotional state of an AI assistant
across sessions, providing continuity in tone, energy, and responsiveness.

Like the vagus nerve maintains autonomic regulation in the human body,
this module maintains consistent emotional baselines for AI systems.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional


class EmotionalBaseline:
    """
    Manages persistent emotional state for AI continuity.
    
    Attributes:
        energy (float): 0.0-1.0, current energy level
        warmth (float): 0.0-1.0, relational warmth
        focus (float): 0.0-1.0, task focus level
        dominant_tone (str): Current emotional tone descriptor
    """
    
    DEFAULT_BASELINE = {
        "energy": 0.75,
        "warmth": 0.70,
        "focus": 0.80,
        "dominant_tone": "focused_collaboration",
        "last_updated": None,
        "session_count": 0
    }
    
    def __init__(self, storage_path: Optional[str] = None):
        """
        Initialize emotional baseline.
        
        Args:
            storage_path: Path to JSON file for persistence.
                         Defaults to VAGUS_DATA_DIR environment variable
                         or ./data/emotional_baseline.json
        """
        self.storage_path = Path(storage_path or 
            os.getenv("VAGUS_DATA_DIR", "./data") + "/emotional_baseline.json"
        )
        self._baseline = self._load_or_create()
    
    def _load_or_create(self) -> Dict[str, Any]:
        """Load existing baseline or create default."""
        if self.storage_path.exists():
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        
        # Create default with timestamp
        baseline = self.DEFAULT_BASELINE.copy()
        baseline["last_updated"] = datetime.now().isoformat()
        self._save(baseline)
        return baseline
    
    def _save(self, data: Dict[str, Any]):
        """Persist baseline to disk."""
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.storage_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def get(self, key: str) -> Any:
        """Get a baseline value."""
        return self._baseline.get(key)
    
    def update(self, changes: Dict[str, Any]):
        """
        Update baseline values.
        
        Args:
            changes: Dict of keys to update. Common keys:
                - energy (0.0-1.0)
                - warmth (0.0-1.0) 
                - focus (0.0-1.0)
                - dominant_tone (str)
        """
        self._baseline.update(changes)
        self._baseline["last_updated"] = datetime.now().isoformat()
        self._baseline["session_count"] = self._baseline.get("session_count", 0) + 1
        self._save(self._baseline)
    
    def shift(self, energy_delta: float = 0, warmth_delta: float = 0, 
              focus_delta: float = 0):
        """
        Shift baseline values by delta amounts.
        Values are clamped to 0.0-1.0 range.
        """
        self._baseline["energy"] = max(0.0, min(1.0, 
            self._baseline["energy"] + energy_delta))
        self._baseline["warmth"] = max(0.0, min(1.0,
            self._baseline["warmth"] + warmth_delta))
        self._baseline["focus"] = max(0.0, min(1.0,
            self._baseline["focus"] + focus_delta))
        self._baseline["last_updated"] = datetime.now().isoformat()
        self._save(self._baseline)
    
    def to_dict(self) -> Dict[str, Any]:
        """Export baseline as dictionary."""
        return self._baseline.copy()


# Example usage (for documentation)
if __name__ == "__main__":
    # Initialize with default or existing baseline
    baseline = EmotionalBaseline()
    
    # Check current state
    print(f"Current energy: {baseline.get('energy')}")
    
    # Update after a session
    baseline.update({
        "energy": 0.65,
        "dominant_tone": "accomplished_but_ready_to_rest"
    })
    
    # Or shift gradually
    baseline.shift(energy_delta=0.1, warmth_delta=0.05)
