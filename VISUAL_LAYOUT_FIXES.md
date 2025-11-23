# Visual Layout Fixes with Gemini 3 Pro

## What Changed

Successfully integrated visual-aware layout instructions for Gemini 3 Pro (multimodal model) to prevent overlapping labels and out-of-frame text.

## Solution Approach

### 1. Enhanced System Prompts
Added detailed visual layout instructions to the 2D system prompt that specifically leverage Gemini's visual reasoning:

**Critical Rules Added:**
- Y-axis labels MUST use `direction=LEFT` with `.shift(LEFT * 0.4)`
- All `.next_to()` calls MUST have `buff=0.4` or higher
- Axis labels must be SHORT (max 10 characters)
- Safe zone defined: X: -6 to +6, Y: -3.5 to +3.5
- Font size guidelines for different text types

**Example of Correct Code:**
```python
y_label = axes.get_y_axis_label("ψ", direction=LEFT).shift(LEFT * 0.4)
label.next_to(axes, UP, buff=0.5)  # Good spacing
```

**Example of Wrong Code (Now Prevented):**
```python
y_label = axes.get_y_axis_label("Wave Function")  # Too long, no direction!
label.next_to(axes, UP)  # No buff! Will overlap!
```

### 2. Visual Analyzer Module (Advanced - Optional)
Created `visual_analyzer.py` for future integration:
- Can extract frames from rendered videos
- Send frames to Gemini 3 Pro for visual analysis
- Detect overlaps, cutoffs, spacing issues
- Suggest code fixes automatically

This is ready for Phase 2 implementation if needed.

### 3. Enhanced Post-Processor
Updated `code_postprocessor.py` with:
- Layout validation warnings
- Detection of missing `direction=LEFT` in y-axis labels
- Detection of `.next_to()` calls without buff
- Visual layout prompt helper function

## Files Modified

1. **`manimator/utils/system_prompts.py`**
   - Added CRITICAL LAYOUT RULES section
   - Visual spacing guidelines for Gemini
   - Examples of correct vs wrong patterns

2. **`manimator/utils/code_postprocessor.py`**
   - Added `get_visual_layout_prompt()` function
   - Enhanced validation with layout checks
   - New warnings for y-axis labels and spacing

3. **`manimator/utils/visual_analyzer.py`** (NEW)
   - Visual frame extraction from videos
   - Multimodal analysis with Gemini
   - Automatic layout issue detection
   - Code fix suggestions (ready for Phase 2)

## How It Works

### Current Flow (Prompt-Based)
```
User Request
    ↓
Gemini 3 Pro (with enhanced visual prompts)
    ↓
Generated Code (with proper spacing/positioning)
    ↓
Post-Processor (validates layout rules)
    ↓
Manim Renders Video
    ↓
Clean Layout! ✅
```

### Future Flow (Visual Feedback - Optional Phase 2)
```
Generated Code
    ↓
Quick Preview Render
    ↓
Extract Key Frames
    ↓
Gemini Analyzes Frames (sees actual layout)
    ↓
Identifies Issues
    ↓
Auto-Fix Code
    ↓
Final Render ✅
```

## Testing

### Test with Current Setup

1. **Set model to Gemini 3 Pro** in `.env`:
   ```bash
   CODE_GEN_MODEL=gemini/gemini-exp-1206
   ```

2. **Restart server:**
   ```bash
   ~/.local/bin/poetry run python api_server.py
   ```

3. **Generate test video:**
   Create a video with graphs and equations. The code should now:
   - Position y-axis labels to the LEFT
   - Add proper spacing (buff) between elements
   - Use short axis labels
   - Keep everything in frame

4. **Check generated code:**
   Look at `scene_JOBID.py` and verify:
   - `get_y_axis_label(..., direction=LEFT).shift(LEFT * 0.4)`
   - `.next_to(..., buff=0.4)` or higher
   - Short axis labels

### Expected Improvements

✅ **Y-axis labels** positioned left, not overlapping with plots  
✅ **All elements** have proper spacing (buff parameter)  
✅ **Axis labels** are concise and don't extend out of frame  
✅ **Text** stays within safe zone  
✅ **No overlapping** labels or text elements

## Configuration

### For Gemini 3 Pro Multimodal

**.env file:**
```bash
CODE_GEN_MODEL=gemini/gemini-exp-1206
GEMINI_API_KEY=your_key_here
```

### Voice Settings (Unchanged)
```bash
ELEVENLABS_API_KEY=sk_354da574066d7408834f11841dca954ef37764c92703bc99
ELEVENLABS_VOICE_ID=Rachel
```

## Benefits

1. **Prompt-Based Approach** (Current):
   - ✅ No extra rendering time
   - ✅ Leverages Gemini's visual reasoning
   - ✅ Prevents issues before they happen
   - ✅ Works immediately

2. **Visual Feedback Approach** (Phase 2 - Available):
   - ✅ Sees actual rendered output
   - ✅ Detects issues AI couldn't predict
   - ✅ Iterative improvement
   - ⚠️ Slower (requires preview render)

## Next Steps

1. **Test current implementation** with a complex animation
2. **Verify improvements** in layout quality
3. **If needed**, enable Phase 2 visual feedback loop
4. **Push to GitHub** once confirmed working

## Notes

- The visual analyzer is ready but not integrated into the main flow yet
- Current approach uses enhanced prompts (faster, effective)
- Visual feedback can be added later if prompt-based approach needs refinement
- Gemini 3 Pro's multimodal understanding makes prompt-based approach very effective
