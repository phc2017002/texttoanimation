from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class ThemeDefinition:
    name: str
    background_color: str
    primary_color: str
    secondary_color: str
    text_color: str
    font: str
    code_style: str
    node_color: str
    edge_color: str
    description: str

THEMES: Dict[str, ThemeDefinition] = {
    "tech": ThemeDefinition(
        name="Tech & System Design",
        background_color="#0F172A",  # Dark Slate
        primary_color="#38BDF8",     # Sky Blue
        secondary_color="#818CF8",   # Indigo
        text_color="#F8FAFC",        # Slate 50
        font="Monospace",            # Monospaced for tech feel
        code_style="monokai",
        node_color="#1E293B",        # Slate 800
        edge_color="#94A3B8",        # Slate 400
        description="Dark mode, neon accents, clean lines, perfect for architecture diagrams."
    ),
    "product": ThemeDefinition(
        name="Product & Startup",
        background_color="#FFFFFF",  # White
        primary_color="#6366F1",     # Indigo 500
        secondary_color="#EC4899",   # Pink 500
        text_color="#1F2937",        # Gray 800
        font="Sans-serif",           # Modern sans-serif
        code_style="friendly",
        node_color="#F3F4F6",        # Gray 100
        edge_color="#D1D5DB",        # Gray 300
        description="Bright, clean, modern UI feel, soft shadows, vibrant colors."
    ),
    "mathematical": ThemeDefinition(
        name="Mathematical & Research",
        background_color="#111111",  # Almost Black (Blackboard)
        primary_color="#FFFFFF",     # White Chalk
        secondary_color="#FFD700",   # Gold
        text_color="#FFFFFF",
        font="Serif",                # LaTeX style
        code_style="default",
        node_color="#333333",
        edge_color="#FFFFFF",
        description="Classic Manim style, high contrast, precise, academic."
    )
}

def get_theme(category: str) -> ThemeDefinition:
    """Get theme definition by category name (case-insensitive)."""
    # Map common aliases
    aliases = {
        "system design": "tech",
        "startup": "product",
        "research": "mathematical",
        "math": "mathematical"
    }
    
    key = category.lower()
    key = aliases.get(key, key)
    
    return THEMES.get(key, THEMES["mathematical"])  # Default to math
