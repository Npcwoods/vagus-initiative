"""
Example: Basic Setup

Minimal example showing The Vagus Initiative initialization
and basic state tracking across two sessions.
"""

import sys
sys.path.insert(0, '../')

from vagus import EmotionalBaseline, TrustMap, SessionBridge
from datetime import datetime

def simulate_first_session():
    """Simulate an initial user session."""
    print("=" * 60)
    print("SESSION 1: Project Planning")
    print("=" * 60)
    
    # Initialize (creates default state)
    baseline = EmotionalBaseline(storage_path="./data/baseline.json")
    trust = TrustMap(storage_path="./data/trust.json")
    bridge = SessionBridge(storage_path="./data/bridge.json")
    
    print(f"\n🌅 Initial State:")
    print(f"   Energy: {baseline.get('energy')}")
    print(f"   Trust Depth: {trust.get_depth():.2f}")
    
    # Simulate conversation
    print(f"\n💬 Conversation:")
    print("   User: 'Let's plan our Q2 roadmap'")
    print("   AI: 'Great! I've been thinking about priorities...'")
    print("   [Discussion continues for 45 minutes]")
    
    # Update emotional state
    baseline.update({
        "energy": 0.80,
        "warmth": 0.75,
        "focus": 0.90,
        "dominant_tone": "focused_collaboration"
    })
    
    # Record positive interaction
    trust.record_interaction(
        quality="productive_and_engaged",
        depth_change=0.08
    )
    
    # Mark session end with context
    bridge.update_session_end(
        topics=["q2_roadmap", "priorities", "resource_allocation"],
        unfinished=[
            "Define Q2 milestones",
            "Schedule stakeholder review",
            "Draft budget proposal"
        ],
        tone="focused_collaboration",
        energy=0.75,
        mood="accomplished"
    )
    
    print(f"\n📊 Session 1 Complete:")
    print(f"   Energy at end: {baseline.get('energy')}")
    print(f"   Trust depth: {trust.get_depth():.2f}")
    print(f"   Unfinished items: 3")
    print(f"   Session quality: High")
    
    print(f"\n💾 State saved to ./data/")
    print("   [Session ends, user logs off]")


def simulate_second_session():
    """Simulate returning for next session."""
    print("\n" + "=" * 60)
    print("SESSION 2: Next Day")
    print("=" * 60)
    
    # Components automatically load previous state
    baseline = EmotionalBaseline(storage_path="./data/baseline.json")
    trust = TrustMap(storage_path="./data/trust.json")
    bridge = SessionBridge(storage_path="./data/bridge.json")
    
    print(f"\n🌅 Resumed State:")
    print(f"   Energy: {baseline.get('energy')} (from yesterday)")
    print(f"   Trust Depth: {trust.get_depth():.2f} (increased)")
    
    print(f"\n🌉 Loading Context from Previous Session:")
    print(bridge.get_bridge_summary())
    
    print(f"\n💬 AI Greeting:")
    print(f"   'Good morning! Welcome back.'")
    print(f"   'Yesterday we were planning your Q2 roadmap.'")
    print(f"   'You mentioned wanting to define milestones and schedule')
    print(f"    a stakeholder review. Want to pick up there?'")
    
    print(f"\n💬 User Response:")
    print("   'Yes, let's start with the milestones. I have some ideas.'")
    
    print(f"\n✨ Notice:")
    print("   - AI remembered specific unfinished items")
    print("   - Trust depth persisted (relationship evolved)")
    print("   - Energy level carried over (mood continuity)")
    print("   - No need to re-explain context")


if __name__ == "__main__":
    import os
    
    # Create data directory
    os.makedirs("./data", exist_ok=True)
    
    print("\n🧠 THE VAGUS INITIATIVE - Basic Demo")
    print("   Demonstrating continuity across sessions\n")
    
    simulate_first_session()
    simulate_second_session()
    
    print("\n" + "=" * 60)
    print("✅ Demo Complete!")
    print("=" * 60)
    print("\nCheck ./data/ for generated state files.")
    print("These JSON files contain the persistent state that enables")
    print("continuity between disconnected sessions.")
