# Dual Model Configuration Guide

## Overview

The system now uses **two specialized models**:

1. **Claude 4.5 Sonnet** - Code generation (best at Python/Manim)
2. **Gemini 3 Pro Preview** - Visual validation (multimodal, optional)

## Current Setup

### For Code Generation
Model: **Claude 4.5 Sonnet** (`anthropic/claude-sonnet-4`)
- Best at generating complex Python code
- Excellent at Manim animations
- Strong at mathematical content
- Reliable 5+ minute content generation

### For Visual Validation (Future)
Model: **Gemini 3 Pro Preview** (`gemini/gemini-exp-1206`)
- Multimodal (can see images)
- Can analyze rendered frames
- Detect layout issues visually
- Currently enhanced with visual-aware prompts

## Configuration

### Option 1: Using OpenRouter (Easiest)

Update your `.env`:
```bash
# Use Claude via OpenRouter for code generation
CODE_GEN_MODEL=anthropic/claude-sonnet-4
OPENROUTER_API_KEY=your_key_here

# Optional: Gemini for visual validation
VISUAL_MODEL=gemini/gemini-exp-1206

# Voice
ELEVENLABS_API_KEY=sk_354da574066d7408834f11841dca954ef37764c92703bc99
ELEVENLABS_VOICE_ID=Rachel
```

### Option 2: Direct APIs

```bash
# Claude via Anthropic
CODE_GEN_MODEL=anthropic/claude-sonnet-4
ANTHROPIC_API_KEY=your_claude_key

# Gemini via Google
VISUAL_MODEL=gemini/gemini-exp-1206
GEMINI_API_KEY=your_gemini_key

# Voice
ELEVENLABS_API_KEY=sk_354da574066d7408834f11841dca954ef37764c92703bc99
```

## Duration Fix

Enhanced the system prompt to ensure 5+ minute videos:

**New Requirements:**
- MUST create 8-12 separate method functions
- Each method covers a different aspect (intro, context, equation, examples, etc.)
- Each voiceover block: 15-30 seconds
- Total duration: 300+ seconds (5+ minutes)

**Example Structure:**
```python
def construct(self):
    self.intro()                 # 30s
    self.historical_context()    # 40s
    self.main_equation()         # 45s
    self.term_by_term_analysis() # 50s
    self.example_1()             # 40s
    self.example_2()             # 40s
    self.applications()          # 35s
    self.summary()               # 30s
    # Total: ~310 seconds (5+ minutes)
```

## Testing

1. **Update `.env`:**
   ```bash
   CODE_GEN_MODEL=anthropic/claude-sonnet-4
   ```

2. **Restart server:**
   ```bash
   ~/.local/bin/poetry run python api_server.py
   ```

3. **Generate video:**
   ```json
   {
     "prompt": "Create a 5-minute animation explaining the Schrödinger equation",
     "quality": "high"
   }
   ```

4. **Verify:**
   - Video should be 5+ minutes
   - 8-12 separate sections
   - Detailed explanations
   - Natural ElevenLabs voice

## Why Two Models?

### Claude 4.5 Sonnet
✅ **Best for**: Complex code generation  
✅ **Strengths**: Python, Manim, mathematical content  
✅ **Result**: Longer, more detailed animations  

### Gemini 3 Pro Preview  
✅ **Best for**: Visual understanding  
✅ **Strengths**: Layout analysis, multimodal reasoning  
✅ **Result**: Better positioned elements (via enhanced prompts)  

## Current Implementation

**Active Now:**
- ✅ Claude generates all code
- ✅ Enhanced prompts with visual layout rules
- ✅ Post-processor fixes common issues
- ✅ ElevenLabs for natural voice

**Ready for Phase 2:**
- ⏸️ Visual frame analysis with Gemini
- ⏸️ Iterative layout refinement
- ⏸️ Automatic fix generation

## Model Costs (Approximate)

**Claude 4.5 Sonnet:**
- Input: $3 / 1M tokens
- Output: $15 / 1M tokens
- ~$0.10-0.30 per 5-min animation

**Gemini 3 Pro:**
- Input: Free (during preview)
- Output: Free (during preview)
- Visual: Free (during preview)

**ElevenLabs:**
- ~3,000-5,000 characters per 5-min animation
- Cached after first generation
- ~$0.05-0.15 per animation (with caching)

## Troubleshooting

### Short Videos (< 5 minutes)
**Cause:** Model not following duration requirements  
**Fix:** The new prompts are more explicit about structure

### Layout Issues
**Current:** Enhanced visual prompts for Claude  
**Future:** Enable Gemini visual validation

### API Errors
Check your API keys and model names in `.env`

---

**System is now configured for Claude + Gemini dual model approach!**
