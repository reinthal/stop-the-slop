FROM python:3.13-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Change the working directory to `/app`
WORKDIR /app

# Copy the lockfile and pyproject.toml
COPY uv.lock pyproject.toml ./

# Install dependencies
RUN uv sync --frozen --no-cache --no-group dev --no-group test

# Copy application code
COPY src /app/src

# Set environment variables
ENV PYTHONPATH=/app

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI server with modern fastapi CLI (production-ready)
CMD ["uv", "run", "--no-group", "dev", "--no-group", "test", "fastapi", "run", "src/main.py", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "--proxy-headers"]
