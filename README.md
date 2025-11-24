# Text to Animation

Transform any text prompt into stunning mathematical and educational animations powered by AI and the [Manim](https://github.com/ManimCommunity/manim) engine.

## 🎯 Overview

This tool converts natural language descriptions into beautiful, professional-quality animations. Simply describe what you want to visualize - whether it's a mathematical concept, scientific principle, or educational explanation - and the system generates an animated video using the powerful Manim library.

### ✨ Key Features

- **AI-Powered Animation Generation**: Converts text prompts into Manim code automatically
- **2D & 3D Animations**: Support for both 2D and 3D visualizations
- **Voiceover Support**: Generates animations with synchronized AI voiceovers
- **Mathematical Equations**: Renders beautiful LaTeX equations and mathematical visualizations
- **Multiple API Servers**: RESTful APIs for programmatic access
- **Gradio Interface**: User-friendly web interface for easy interaction
- **Flexible LLM Support**: Works with various AI models (Gemini, DeepSeek, Claude, etc.)

## 📋 System Requirements

### System Dependencies

This project is built on the [Manim](https://github.com/ManimCommunity/manim) engine, which requires the following system dependencies:

#### macOS
```bash
# Install basic dependencies
brew install cairo ffmpeg pango pkg-config

# Install LaTeX (required for mathematical equations and MathTex)
brew install --cask basictex

# After installation, update PATH in your current terminal:
eval "$(/usr/libexec/path_helper)"

# Install additional LaTeX packages that Manim needs
sudo tlmgr update --self
sudo tlmgr install latex-bin amsmath amsfonts amssymb babel-english cbfonts-fd cm-super ctex dvipng environ filehook float fontspec frcursive fundus-calligra jknapltx latexmk metalogo microtype ms physics rsfs scheme-infraonly setspace standalone tools unicode-math xcolor
```

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install build-essential python3-dev libcairo2-dev libpango1.0-dev ffmpeg
```

#### Windows
Install the following:
- [FFmpeg](https://ffmpeg.org/download.html)
- [Cairo](https://www.cairographics.org/download/)
- [Pango](https://pango.gnome.org/)

For detailed Manim installation instructions, see the [official documentation](https://docs.manim.community/en/stable/installation.html).

### Python Dependencies

This project uses [Poetry](https://python-poetry.org/) for dependency management. The key dependencies include:

**Core Dependencies:**
- `python` >= 3.11, < 3.13
- `manim` ^0.18.1 - Animation engine
- `manim-voiceover[gtts]` ^0.3.7 - Voiceover support with Google Text-to-Speech

**API & Web Framework:**
- `fastapi` ^0.115.6 - REST API framework
- `uvicorn` ^0.34.0 - ASGI server
- `gradio` ^5.9.1 - Web interface

**AI & LLM Integration:**
- `litellm` ^1.56.10 - Unified LLM API interface
- `google-genai` ^1.51.0 - Google Gemini integration

**Utilities:**
- `python-dotenv` 0.21.0 - Environment variable management
- `python-multipart` ^0.0.20 - File upload support
- `tenacity` ^9.0.0 - Retry logic
- `pypdf2` ^3.0.1 - PDF processing
- `setuptools` ^80.9.0 - Build tools

## 🚀 Installation

### 1. Install Poetry

Download and install Poetry from [here](https://python-poetry.org/docs/#installing-with-the-official-installer):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 2. Clone the Repository

```bash
git clone <repository-url>
cd texttoanimation
```

### 3. Install Dependencies

```bash
poetry install
```

### 4. Activate the Virtual Environment

For Poetry 2.0+:
```bash
poetry env activate
```

For older versions:
```bash
poetry shell
```

### 5. Set Up Environment Variables

Create a `.env` file in the root directory with your API keys:

```env
# Required: At least one LLM API key
GEMINI_API_KEY=your_gemini_api_key_here
# Or use other providers:
# OPENAI_API_KEY=your_openai_api_key
# ANTHROPIC_API_KEY=your_anthropic_api_key
# DEEPSEEK_API_KEY=your_deepseek_api_key

# Optional: Model configuration (defaults to Gemini)
# LLM_MODEL=gemini/gemini-1.5-flash
```

## 💻 Usage

### Running the API Server

The unified server supports all input types (text, PDF, URL) and all categories:

```bash
python api_server.py
```

Visit `http://localhost:8000/docs` for interactive API documentation.

### Using the Python Client

The `api_client.py` provides a Python client library for interacting with the API server:

```python
from api_client import ManimVideoClient, QualityLevel

client = ManimVideoClient(base_url="http://localhost:8000")

# Create a video
job = client.create_video(
    prompt="Explain the Pythagorean theorem with a visual proof",
    quality=QualityLevel.MEDIUM
)

# Check status
status = client.get_status(job['job_id'])

# Download video when complete
if status['status'] == 'completed':
    client.download_video(job['job_id'], 'output.mp4')
```

### API Examples

#### Create Video from Text

```bash
curl -X POST http://localhost:8000/api/videos \
  -H "Content-Type: application/json" \
  -d '{
    "input_type": "text",
    "input_data": "Explain how a distributed system handles requests",
    "quality": "high",
    "category": "tech_system"
  }'
```

#### Create Video from URL

```bash
curl -X POST http://localhost:8000/api/videos \
  -H "Content-Type: application/json" \
  -d '{
    "input_type": "url",
    "input_data": "https://example.com/blog/architecture",
    "quality": "medium",
    "category": "tech_system"
  }'
```

#### Check Job Status

```bash
curl http://localhost:8000/api/jobs/{job_id}
```

#### Download Video

```bash
curl http://localhost:8000/api/videos/{job_id} --output animation.mp4
```

## 🔧 Configuration

### Changing AI Models

The system supports multiple LLM providers through [LiteLLM](https://docs.litellm.ai/docs/providers). Set your preferred model in the `.env` file:

```env
CODE_GEN_MODEL=gemini/gemini-2.0-flash-exp
# or
CODE_GEN_MODEL=anthropic/claude-3-5-sonnet-20241022
```

### Customizing System Prompts

To modify how the AI generates animations, edit the system prompts in:
- `manimator/utils/system_prompts.py`

## 📚 API Documentation

- **POST** `/api/videos` - Create a new video generation job (supports text, PDF, URL)
- **GET** `/api/jobs/{job_id}` - Get job status
- **GET** `/api/videos/{job_id}` - Download generated video
- **GET** `/api/jobs` - List all jobs
- **GET** `/health` - Health check

**Input Types:**
- `text` - Plain text prompt
- `pdf` - Base64 encoded PDF file
- `url` - URL to scrape content from

**Categories:**
- `tech_system` - System design, architecture, technical concepts
- `product_startup` - Product demos, startup pitches, feature showcases
- `mathematical` - Mathematical concepts, research papers, educational content

## 🐳 Docker

Build and run the application using Docker:

### Build the Docker Image

```bash
docker build -t texttoanimation .
```

### Run API Server

```bash
docker run -p 8000:8000 texttoanimation
```

## 📁 Project Structure

```
texttoanimation/
├── api_server.py          # Unified API Server (Port 8000)
├── api_client.py          # Python client library
├── manimator/             # Core package
│   ├── api/               # Animation generation logic
│   ├── inputs/            # Input processing (Text, PDF, URL)
│   ├── scene/             # Scene base classes
│   ├── services/          # External services (ElevenLabs)
│   ├── themes/            # Visual theme definitions
│   └── utils/             # Utilities (Code fixing, validation)
├── assets/                # Static assets
├── generated_scenes/      # Generated Manim code files
├── docs/                  # Documentation
├── pyproject.toml         # Poetry configuration
├── requirements.txt       # Alternative dependency file
└── README.md              # This file
```

## 🎨 Example Prompts

Try these example prompts to see what the system can create:

- "Create an animation explaining how neural networks learn"
- "Visualize the Fourier transform with examples"
- "Show how gradient descent works in machine learning"
- "Explain quantum entanglement with visual demonstrations"
- "Demonstrate the concept of limits in calculus"
- "Create a 3D visualization of a rotating cube"
- "Show the relationship between sine and cosine waves in 3D"

## 🙏 Acknowledgements

This project builds upon the incredible work of:
- [Manim Community](https://www.manim.community/) and [3Blue1Brown](https://github.com/3b1b/manim) for the animation engine
- Original [manimator](https://github.com/HyperCluster-Tech/manimator) project developers: [Samarth P](https://github.com/samarth777), [Vyoman Jain](https://github.com/VyoJ), [Shiva Golugula](https://github.com/Shiva4113), and [M Sai Sathvik](https://github.com/User-LazySloth)

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for more information.

The project uses the [Manim engine](https://github.com/ManimCommunity/manim), which is double-licensed under the MIT license, with copyright by 3blue1brown LLC and Manim Community Developers.

## 📧 Contact

For inquiries, please open an issue on GitHub.
