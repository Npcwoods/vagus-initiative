# Contributing to The Vagus Initiative

Thank you for your interest in contributing! This is experimental software, and we're learning as we go.

## Code of Conduct

- Be respectful and constructive
- Assume good intent
- Focus on the ideas, not the person
- Help others learn

## How to Contribute

### Reporting Issues

Before opening an issue:
1. Search existing issues to avoid duplicates
2. Include Python version and OS
3. Provide minimal reproducible example
4. Describe expected vs actual behavior

### Suggesting Features

Open an issue with:
- Clear description of the problem/need
- Proposed solution
- Use cases and examples
- Willingness to implement (optional but appreciated)

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Update documentation
6. Commit with clear messages
7. Push and open a PR

## Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/vagus-initiative.git
cd vagus-initiative

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install in development mode
pip install -e .

# Run tests
python -m pytest tests/
```

## Areas for Contribution

### High Priority

- [ ] Test coverage for core modules
- [ ] Integration examples for popular AI frameworks
- [ ] Documentation improvements
- [ ] Error handling and edge cases

### Medium Priority

- [ ] Additional analysis in Dream Cycle
- [ ] Visualization tools for state evolution
- [ ] Migration tools for version updates
- [ ] Performance optimizations

### Experimental

- [ ] Multi-user support
- [ ] Distributed state sync
- [ ] Vector memory integration
- [ ] Web dashboard for state inspection

## Coding Standards

### Python Style

- Follow PEP 8
- Use type hints where helpful
- Docstrings for public functions
- Keep functions focused and small

### Documentation

- Update README.md for user-facing changes
- Update docs/ for architectural changes
- Add comments for complex logic
- Keep examples runnable

### Testing

- Add tests for new features
- Ensure existing tests pass
- Test edge cases
- Document test rationale

## Commit Message Format

```
type: Brief description

Longer explanation if needed.

- Bullet points for details
- References to issues/PRs
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Formatting, no code change
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

Example:
```
feat: Add emotional echo tracking

Implements emotional echo persistence across sessions.
Echoes decay over time based on intensity and recency.

Closes #42
```

## Release Process

1. Update version in `core/__init__.py`
2. Update CHANGELOG.md
3. Tag release: `git tag v0.2.0`
4. Push tags: `git push origin v0.2.0`
5. Create GitHub release with notes

## Questions?

- Open a discussion for general questions
- Open an issue for bugs
- Reach out on Twitter: @NPCWoods

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make AI relationships more meaningful!
