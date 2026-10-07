# Template assumptions

- This is an optional starting point for a new repository. Existing organization rules take precedence.
- Python 3.11 is a starting value, not an inferred organization minimum. Change requires-python, Ruff target, and CI together when the project needs another version.
- uv and a committed uv.lock are starting choices for reproducible development and CI; select a different dependency workflow when project requirements call for it.
- pyproject.toml holds project metadata. setuptools is used for the minimal src-layout package.
- Ruff and pytest are template defaults, not an established organization-wide ruleset. The lint selection explicitly lists all current stable Pyflakes (F) rules and selected import, whitespace, bug prevention, pytest, suppression, Ruff-specific, and type modernization rules. The Python template additionally checks E501 with a 120-character line limit. Each rule is documented in pyproject.toml; review the selection when upgrading Ruff.
- The local Ruff lint hook uses --fix, but automatic corrections are limited to safe fixes for I001, W291, W292, W293, F401, RUF100, UP006, and UP007. Other selected violations fail the hook. Unsafe fixes are not enabled. Review and stage hook changes before retrying a commit.
- Ruff formatting is checked rather than automatically applied. Pre-Commit also checks basic file hygiene. The same hooks run in CI; corrections made during a CI run cause the hook check to fail rather than being committed automatically.
- GitHub Actions validates pushes and pull requests, including a package build. No deployment, publication, or release automation is included.
- Project name, description, responsible team, and license are unresolved TODOs. No license is assumed.
- Ignore patterns are only a guardrail; they cannot prove that a commit contains no secrets or customer data.
- CLA policy is separate and is not activated by this template.
