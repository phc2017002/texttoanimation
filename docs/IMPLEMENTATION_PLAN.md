# Implementation Plan: Enhanced Video Generation System

## Phase 1: Unified Input Processor

### 1.1 Create Web Content Scraper
**File**: `manimator/utils/web_scraper.py`
- Use `requests` + `beautifulsoup4` for HTML parsing
- Extract main content, remove navigation/ads
- Support: blogs, documentation sites, Medium, Dev.to, etc.
- Handle authentication-required pages (return error with clear message)
- Extract text content and structure (headings, paragraphs, code blocks)
- Convert to structured format similar to PDF processing

**Dependencies to add**:
```python
beautifulsoup4>=4.12.0
requests>=2.31.0
readability-lxml>=0.8.1  # For cleaner content extraction
```

### 1.2 Unified Input Handler
**File**: `manimator/api/input_processor.py`
- Single entry point: `process_input(input_type, input_data, category)`
- Input types: `text`, `pdf`, `url`
- Route to appropriate processor:
  - Text → `process_prompt_scene()`
  - PDF → `process_pdf_prompt()`
  - URL → new `process_url_content()`
- Return standardized scene description format

### 1.3 URL Content Processor
**File**: `manimator/api/scene_description.py` (extend existing)
- Function: `process_url_content(url: str) -> str`
- Scrape web content
- Extract main text (similar to PDF processing)
- Generate scene description using LLM with web content context
- Handle errors: invalid URLs, access denied, parsing failures

---

## Phase 2: Category-Specific Visual Themes

### 2.1 Theme Configuration System
**File**: `manimator/utils/visual_themes.py`
- Define theme configs for each category:
  ```python
  TECH_THEME = {
      "background_color": "#0a0e27",  # Dark blue
      "accent_colors": [BLUE, GREEN, ORANGE, RED, PURPLE],
      "text_color": WHITE,
      "component_style": "rounded_rectangles",
      "animation_style": "professional",
      "voice_id": "Adam"
  }
  
  PRODUCT_THEME = {
      "background_color": "#ffffff",  # White/light
      "accent_colors": [ORANGE, BLUE, PURPLE, GREEN],
      "text_color": "#1a1a1a",
      "component_style": "modern_gradients",
      "animation_style": "engaging",
      "voice_id": "Bella"
  }
  
  RESEARCH_THEME = {
      "background_color": "#1e1e1e",  # Dark
      "accent_colors": [BLUE, GREEN, YELLOW, RED],
      "text_color": WHITE,
      "component_style": "mathematical",
      "animation_style": "educational",
      "voice_id": "Rachel"
  }
  ```

### 2.2 Theme Injection into System Prompts
**File**: `manimator/utils/system_prompts.py` (modify)
- Update `get_system_prompt(category)` to include theme instructions
- Add theme-specific code snippets to each prompt:
  - Tech: Dark background setup, component colors
  - Product: Light background, gradient examples
  - Research: Dark background, equation styling
- Include background setup code in each prompt template

### 2.3 Background Setup Code Generator
**File**: `manimator/utils/theme_injector.py`
- Function: `inject_theme_setup(code: str, category: str) -> str`
- Parse generated code
- Insert background setup at start of `construct()` method:
  ```python
  # Tech theme
  self.camera.background_color = "#0a0e27"
  
  # Product theme  
  self.camera.background_color = "#ffffff"
  
  # Research theme
  self.camera.background_color = "#1e1e1e"
  ```
- Ensure theme colors are used consistently

---

## Phase 3: Enhanced Code Validation & Error Handling

### 3.1 Pre-Render Code Validator
**File**: `manimator/utils/code_validator.py`
- Function: `validate_code(code: str) -> Tuple[bool, List[str]]`
- Checks:
  - Valid Python syntax (use `ast.parse()`)
  - Required imports present (`from manim import *`, `VoiceoverScene`, `ElevenLabsService`)
  - Scene class inherits from `VoiceoverScene`
  - `construct()` method exists
  - Voiceover service initialized
  - No undefined variables/colors
  - No overlapping object warnings (spatial analysis)
- Return: (is_valid, list_of_errors)

### 3.2 Code Fixer
**File**: `manimator/utils/code_fixer.py`
- Function: `auto_fix_code(code: str, errors: List[str]) -> str`
- Auto-fixes:
  - Missing imports (add if not present)
  - Undefined colors (use existing `fix_undefined_colors()`)
  - Missing voiceover setup (inject if missing)
  - Syntax errors (try to fix common issues)
- Use existing `code_postprocessor.py` functions
- Chain fixes until valid or max attempts

### 3.3 Retry Logic with Model Fallback
**File**: `manimator/api/animation_generation.py` (modify)
- Enhanced `generate_animation_response()`:
  - Try generation with primary model
  - Validate code
  - If invalid, try auto-fix
  - If still invalid, retry with different model (fallback)
  - Max 3 attempts total
  - Return best valid code or raise clear error

### 3.4 Render Error Handler
**File**: `manimator/utils/schema.py` (modify `ManimProcessor`)
- Enhanced `render_scene()`:
  - Capture full error output
  - Parse common Manim errors:
    - LaTeX errors → suggest fixes
    - Import errors → auto-add imports
    - Scene not found → validate class name
  - Return detailed error messages
  - Attempt auto-fix and re-render if possible

---

## Phase 4: Unified API Server

### 4.1 New Unified API Server
**File**: `api_server_unified.py`
- Single server handling all input types and categories
- Endpoints:
  - `POST /api/videos` - Create video (text/PDF/URL)
  - `GET /api/jobs/{job_id}` - Check status
  - `GET /api/videos/{job_id}` - Download video
  - `GET /api/jobs` - List jobs
- Request model:
  ```python
  class VideoRequest(BaseModel):
      input_type: Literal["text", "pdf", "url"]
      input_data: str  # text prompt, PDF bytes (base64), or URL
      category: Literal["tech_system", "product_startup", "mathematical"]
      quality: QualityLevel
      scene_name: Optional[str] = None
  ```

### 4.2 Input Router
**File**: `manimator/api/input_router.py`
- Route based on `input_type`:
  - `text` → `process_prompt_scene()`
  - `pdf` → `process_pdf_prompt()` (decode base64)
  - `url` → `process_url_content()`
- All return scene description → pass to `generate_animation_response()`

### 4.3 Job Manager Enhancement
**File**: `api_server_unified.py` (extend existing JobManager)
- Track input type and category
- Store theme used
- Better error messages with category context

---

## Phase 5: System Prompts Enhancement

### 5.1 Category-Specific Prompt Templates
**File**: `manimator/utils/system_prompts.py` (enhance existing)
- **Tech System Prompt**: 
  - Emphasize architecture diagrams
  - Component-based visuals
  - Dark background setup
  - Professional color scheme
  - Data flow animations
  
- **Product Startup Prompt**:
  - Modern UI elements
  - Gradient backgrounds
  - Light/colorful theme
  - Feature showcases
  - Statistics displays
  
- **Research/Mathematical Prompt**:
  - Equation-heavy
  - Dark background
  - Step-by-step proofs
  - Graph visualizations
  - Educational pacing

### 5.2 Few-Shot Examples Update
**File**: `manimator/few_shot/few_shot_prompts.py`
- Add category-specific examples:
  - Tech: System architecture example
  - Product: Feature demo example
  - Research: Mathematical proof example
- Include theme setup in examples

---

## Phase 6: Testing & Validation Pipeline

### 6.1 Code Validation Pipeline
**File**: `manimator/utils/validation_pipeline.py`
- Pre-render checks:
  1. Syntax validation
  2. Import validation
  3. Structure validation
  4. Theme compliance
  5. Auto-fix attempts
- Post-render checks:
  1. Video file exists
  2. Video duration > 0
  3. Video is playable

### 6.2 Error Recovery
- If validation fails → auto-fix → re-validate
- If auto-fix fails → retry generation with different model
- If all fails → return detailed error to user

---

## Implementation Order

1. **Week 1**: Phase 1 (Input Processor) + Phase 2 (Themes)
2. **Week 2**: Phase 3 (Validation) + Phase 5 (Prompts)
3. **Week 3**: Phase 4 (Unified API) + Phase 6 (Testing)

---

## File Structure Changes

```
manimator/
├── api/
│   ├── animation_generation.py (existing, enhance)
│   ├── scene_description.py (existing, extend)
│   ├── input_processor.py (NEW)
│   └── input_router.py (NEW)
├── utils/
│   ├── code_postprocessor.py (existing)
│   ├── code_validator.py (NEW)
│   ├── code_fixer.py (NEW)
│   ├── visual_themes.py (NEW)
│   ├── theme_injector.py (NEW)
│   └── validation_pipeline.py (NEW)
└── services/
    └── web_scraper.py (NEW)

api_server_unified.py (NEW - main server)
```

---

## Dependencies to Add

```toml
beautifulsoup4 = "^4.12.0"
requests = "^2.31.0"
readability-lxml = "^0.8.1"
```

---

## Key Success Metrics

1. **Reliability**: < 5% code generation failures
2. **Visual Differentiation**: Clear visual distinction between categories
3. **Error Recovery**: 80%+ of errors auto-fixed
4. **Input Support**: All 3 input types working (text/PDF/URL)

