# FastAPI Project with uv Package Manager

## Prerequisites

- Python 3.10+
- Docker (optional)
- uv package manager

## Installation Methods

### 1. Using pyproject.toml (Recommended)

#### Setup with uv

```bash
# Install uv package manager
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate  # On Unix/macOS
.venv\Scripts\activate     # On Windows

# Install dependencies
uv pip install -e .
```

### 2. Using requirements.txt

#### Setup with uv

```bash
# Install uv package manager
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate  # On Unix/macOS
.venv\Scripts\activate     # On Windows

# Install dependencies
uv pip install -r requirements.txt
```

#### Alternative: Using pip

```bash
# Create virtual environment (traditional method)
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # On Unix/macOS
.venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```

### Generating requirements.txt

```bash
# Generate requirements.txt, excluding editable installations
uv pip freeze --exclude-editable > requirements.txt
```

## Running the Application

### Local Development

```bash
# Activate virtual environment
source .venv/bin/activate  # On Unix/macOS

# Run with uvicorn
uvicorn app.main:app --reload
```

## Docker Deployment

### Build and Run

```bash
# Build the Docker image
docker build -t fastapi-uv-app .

# Run the Docker container
docker run -d -p 8000:8000 fastapi-uv-app
```

## Project Structure

```
fastapi-uv-project/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── requirements.txt      # Optional: for pip/uv dependency management
├── pyproject.toml        # Recommended: for modern dependency management
├── Dockerfile
└── README.md
```

## Endpoints

- `GET /`: Root endpoint
- `GET /health`: Health check endpoint

## Development Tips

- Use `uv` for faster dependency management
- Prefer `pyproject.toml` for new projects
- Keep `requirements.txt` for legacy compatibility
- Always activate your virtual environment before working

## Troubleshooting

- Ensure Python version compatibility (3.10+)
- Check that uv is properly installed
- Verify virtual environment activation
- Restart your terminal/IDE if encountering issues

## Contributing

1. Fork the repository
2. Create a virtual environment
3. Install development dependencies
4. Make your changes
5. Submit a pull request
