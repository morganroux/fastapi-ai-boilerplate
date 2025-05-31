.PHONY: dev run test install clean help

# Default target
help:
	@echo "Available commands:"
	@echo "  make dev     - Run development server with auto-reload"
	@echo "  make run     - Run production server"
	@echo "  make test    - Run tests"
	@echo "  make install - Install dependencies"
	@echo "  make clean   - Clean up generated files"
	@echo "  make help    - Show this help message"

# Development server with auto-reload
dev:
	uv run uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

# Production server
run:
	uv run uvicorn src.main:app --host 0.0.0.0 --port 8000

# Run tests
test:
	uv run pytest tests/ -v

# Install dependencies
install:
	uv sync

# Clean up generated files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -f test.db