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
        1. Use `Rectangle` with `rounded_corners=True` for system nodes.
        2. Use `Arrow` with `buff=0` for data flows.
        3. Use `Code` objects for showing snippets.
        4. Layouts should be structured like architecture diagrams (top-down or left-right).
        5. Use `ManimColor('{theme.primary_color}')` for active elements.
        """
        
    elif theme_name == "product":
        return base_instructions + """
        SPECIFIC PRODUCT THEME RULES:
        1. Use `RoundedRectangle` with significant corner radius for "cards".
        2. Use soft colors and gradients if possible.
        3. Animations should be smooth (`run_time=0.8`, `rate_func=smooth`).
        4. Text should be large, bold, and friendly.
        5. Focus on "benefits" and "features" visual metaphors.
        """
        
    else:  # mathematical
        return base_instructions + """
        SPECIFIC MATH THEME RULES:
        1. Use standard Manim `MathTex` for all equations.
        2. Use `NumberPlane` or `Axes` for graphs.
        3. Precision is key. Use `rate_func=linear` for continuous motion.
        4. Keep it clean and high-contrast (Chalkboard style).
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
