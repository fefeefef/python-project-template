# Template assumptions

- This is an optional starting point for a new repository. Existing organization rules take precedence.
- Python 3.11 is a starting value, not an inferred organization minimum. Change requires-python, Ruff target, and CI together when the project needs another version.
- uv and a committed uv.lock are starting choices for reproducible development and CI; select a different dependency workflow when project requirements call for it.
- pyproject.toml holds project metadata. setuptools is used for the minimal src-layout package.
- Ruff and pytest are template defaults. The E, F, I, and UP Ruff rules are a proposed baseline, not an established organization-wide ruleset. Pre-Commit runs Ruff and basic file hygiene checks.
- GitHub Actions validates pushes and pull requests, including a package build. No deployment, publication, or release automation is included.
- Project name, description, responsible team, and license are unresolved TODOs. No license is assumed.
- Ignore patterns are only a guardrail; they cannot prove that a commit contains no secrets or customer data.
- CLA policy is separate and is not activated by this template.
