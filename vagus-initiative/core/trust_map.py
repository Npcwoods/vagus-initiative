"""
The Vagus Initiative - Trust Map Module

Tracks relationship depth and interaction quality between AI and user.
Like the vagus nerve mediates social connection, this module tracks
the evolving relationship over time.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional


class TrustMap:
    """
    Manages relationship depth and trust metrics.
    
    Attributes:
        depth (float): 0.0-1.0, relationship depth
        last_interaction_quality (str): Quality of last exchange
        interaction_count (int): Total interactions
        trigger_phrases (list): Words/phrases that activate patterns
    """
    
    DEFAULT_MAP = {
        "depth": 0.5,
        "last_interaction_quality": "neutral",
        "interaction_count": 0,
        "established_date": None,
        "trigger_phrases": [],
        "last_updated": None
    }
    
    def __init__(self, storage_path: Optional[str] = None):
        self.storage_path = Path(storage_path or
            os.getenv("VAGUS_DATA_DIR", "./data") + "/trust_map.json"
        )
        self._map = self._load_or_create()
    
    def _load_or_create(self) -> Dict[str, Any]:
        if self.storage_path.exists():
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        
        default = self.DEFAULT_MAP.copy()
        default["established_date"] = datetime.now().isoformat()
        default["last_updated"] = datetime.now().isoformat()
        self._save(default)
        return default
    
    def _save(self, data: Dict[str, Any]):
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.storage_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def record_interaction(self, quality: str, depth_change: float = 0):
        """
        Record an interaction and update trust metrics.
        
        Args:
            quality: Description of interaction quality
            depth_change: Amount to adjust trust depth (+/-)
        """
        self._map["last_interaction_quality"] = quality
        self._map["interaction_count"] += 1
        self._map["depth"] = max(0.0, min(1.0, 
            self._map["depth"] + depth_change))
        self._map["last_updated"] = datetime.now().isoformat()
        self._save(self._map)
    
    def add_trigger(self, phrase: str):
        """Add a trigger phrase that activates patterns."""
        if phrase not in self._map["trigger_phrases"]:
            self._map["trigger_phrases"].append(phrase)
            self._save(self._map)
    
    def get_depth(self) -> float:
        """Get current relationship depth."""
        return self._map["depth"]
    
    def to_dict(self) -> Dict[str, Any]:
        return self._map.copy()
