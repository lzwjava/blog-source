# Repository Guidelines

This guide helps contributors work efficiently in this repository.

## Project Structure & Module Organization
- Site: Jekyll sources in `_posts/<lang>/`, `_layouts/`, `_includes/`, `_sass/`, `_plugins/`, `assets/`, and language homepages like `index-zh.html`.
- Automation: Python tools in `scripts/` (e.g., `scripts/audio/`, `scripts/pdf/`, `scripts/translation/`).
- Tests: Python tests in `tests/` and LLM pytest suites in `tests/llm/`.
- Content sources: drafts/long-form in `original/` and `notes/`.
- Documents: LaTeX resumes in `latex/` with Makefile targets.

## Build, Test, and Development Commands
- Jekyll dev: `bundle install` then `bundle exec jekyll serve --draft --incremental` — run local server with drafts.
- Jekyll build: `bundle exec jekyll build` — produce static site in `_site/`.
- Audio pipeline: `python scripts/audio/audio_pipeline.py --task posts --n 10` — batch-generate audio.
- PDF pipeline: `python scripts/pdf/pdf_pipeline.py --task posts --n 10` — export PDFs.
- LaTeX resumes: `make easy-resume` (or `make latex && make copy`).
- Unit tests: `python -m unittest discover -s tests -p 'test_*.py'`.
- LLM tests: `python -m pytest tests/llm -v -m "not slow and not network"`.

## Coding Style & Naming Conventions
- Python: 4-space indent; prefer type hints.
- Format: `black .`; Lint: `ruff .`.
- Posts: dated filenames inside language folders, e.g., `_posts/en/2025-02-02-archlinux-en.md`.
- Tests: files `test_*.py`; classes `Test*`; functions `test_*`.
- Scripts: group by domain under `scripts/<area>/` (e.g., `scripts/audio/azure_speech.py`).

## Testing Guidelines
- Prefer fast unit tests in `tests/` (unittest style).
- LLM tests in `tests/llm/` use markers: `unit`, `integration`, `slow`, `network`; integration tests skip without required env keys.
- Keep tests deterministic; avoid network unless marked.

## Commit & Pull Request Guidelines
- Conventional Commits: `feat(scope): …`, `fix(scope): …`, `docs: …`, `refactor: …`, `chore: …` (e.g., `feat(i18n): add multilingual support for post counts`).
- PRs: include clear description, linked issues, and screenshots for UI/CSS changes. Ensure `black`, `ruff`, and tests pass locally.

## Security & Configuration Tips
- Store secrets in env vars (e.g., GCP/Azure TTS keys). Never commit keys or tokens.
- Local config: Jekyll in `_config.yml`; Ruby gems in `Gemfile`; Python deps in `requirements/`.
- Docker: `docker build -t blog .` then run with your preferred serve/build command.

