# Repository Guidelines

## Project Structure & Module Organization
- Site: Jekyll sources in `_posts/<lang>/`, `_layouts/`, `_includes/`, `_sass/`, `_plugins/`, `assets/`, and language homepages like `index-zh.html`.
- Automation: Python tools in `scripts/` (e.g., `scripts/audio/`, `scripts/pdf/`, `scripts/translation/`).
- Tests: Python tests in `tests/` (plus `tests/llm/` for pytest-based LLM tests).
- Content sources: `original/` and `notes/` hold draft/long-form material.
- Documents: LaTeX resumes in `latex/` with Makefile targets.

## Build, Test, and Development Commands
- Jekyll dev: `bundle install` then `bundle exec jekyll serve --draft --incremental`
- Jekyll build: `bundle exec jekyll build`
- Audio pipeline: `python scripts/audio/audio_pipeline.py --task posts --n 10`
- PDF pipeline: `python scripts/pdf/pdf_pipeline.py --task posts --n 10`
- LaTeX resumes: `make easy-resume` (or `make latex && make copy`)
- Unittest suite: `python -m unittest discover -s tests -p 'test_*.py'`
- LLM tests (pytest): `python -m pytest tests/llm -v -m "not slow and not network"`

## Coding Style & Naming Conventions
- Python: 4-space indent, type hints encouraged. Format with Black: `black .`; lint with Ruff: `ruff .`
- Posts: dated filenames inside language folders (e.g., `_posts/en/2025-02-02-archlinux-en.md`).
- Tests: files start with `test_*.py`; classes `Test*`, functions `test_*`.
- Scripts: group by domain under `scripts/<area>/` (e.g., `scripts/audio/azure_speech.py`).

## Testing Guidelines
- Prefer fast unit tests under `tests/`. Use `unittest` style by default.
- LLM-specific tests under `tests/llm/` use pytest markers: `unit`, `integration`, `slow`, `network`.
- Integration tests require API keys via environment variables and are skipped if missing.

## Commit & Pull Request Guidelines
- Conventional Commits: `feat(scope): …`, `fix(scope): …`, `docs: …`, `refactor: …`, `chore: …`
  - Example: `feat(i18n): add multilingual support for post counts`
- PRs: include clear description, linked issues, and screenshots for UI/CSS changes. Ensure `black`, `ruff`, and tests pass locally.

## Security & Configuration Tips
- Keep secrets in env vars (e.g., GCP/Azure TTS keys). Never commit keys or tokens.
- Local config: Jekyll settings in `_config.yml`; Ruby gems in `Gemfile`; Python deps in `requirements/`.
- If Docker is preferred: `docker build -t blog .` then run with your preferred command to serve/build.
