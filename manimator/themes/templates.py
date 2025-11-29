from .definitions import THEMES

def get_theme_instructions(theme_name: str) -> str:
    """
    Get specific instructions for the LLM based on the theme.
    """
    theme = THEMES.get(theme_name, THEMES["mathematical"])
    
    base_instructions = f"""
    VISUAL STYLE GUIDE ({theme.name}):
    - Background Color: {theme.background_color}
    - Primary Color: {theme.primary_color}
    - Secondary Color: {theme.secondary_color}
    - Text Color: {theme.text_color}
    - Font Style: {theme.font}
    """
    
    if theme_name == "tech":
        return base_instructions + """
        SPECIFIC TECH THEME RULES:
        1. Use `RoundedRectangle(corner_radius=0.2)` for system nodes.
        2. Use `Arrow(buff=0, max_tip_length_to_length_ratio=0.15)` for data flows.
        3. Use `Code` objects for showing snippets (if applicable).
        4. Layouts: Use `VGroup.arrange(DOWN, buff=1)` for clear hierarchy.
        5. Colors: Use high-contrast colors (BLUE, TEAL) against dark background.
        6. Animations: Use `Create` for lines/arrows, `FadeIn(shift=UP)` for boxes.
        """
        
    elif theme_name == "product":
        return base_instructions + """
        SPECIFIC PRODUCT THEME RULES:
        1. Use `RoundedRectangle(corner_radius=0.5)` for "cards" or "screens".
        2. Use `Text(font="Sans", weight=BOLD)` for friendly typography.
        3. Animations: Use `GrowFromCenter` for popping elements, `FadeIn(shift=UP)` for smooth entry.
        4. Focus on "benefits": Use `Indicate` or `Circumscribe` to highlight key features.
        5. Layout: Use `VGroup.arrange(RIGHT, buff=1)` for side-by-side comparisons.
        """
        
    else:  # mathematical
        return base_instructions + """
        SPECIFIC MATH THEME RULES:
        1. Use standard Manim `MathTex` for all equations.
        2. Use `NumberPlane` or `Axes` for graphs.
        3. Precision is key. Use `rate_func=linear` for continuous motion.
        4. Keep it clean: Use `Write` for equations, `Create` for graphs.
        5. Highlight: Use `SurroundingRectangle(color=YELLOW)` to box important results.
        """

def get_scene_template(theme_name: str) -> str:
    """
    Get the base class setup for the scene.
    """
    theme = THEMES.get(theme_name, THEMES["mathematical"])
    
    return f"""
    def construct(self):
        # Theme Setup
        self.camera.background_color = "{theme.background_color}"
        Text.set_default(color="{theme.text_color}", font="{theme.font}")
        MathTex.set_default(color="{theme.text_color}")
        
        # ... rest of the scene
    """
