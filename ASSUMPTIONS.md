# Template assumptions

- This is an optional starting point for a new repository. Existing organization rules take precedence.
- Python 3.11 is a starting value, not an inferred organization minimum. Change requires-python, Ruff target, and CI together when the project needs another version.
- uv and a committed uv.lock are starting choices for reproducible development and CI; select a different dependency workflow when project requirements call for it.
- pyproject.toml holds project metadata. setuptools is used for the minimal src-layout package.
- Ruff and pytest are template defaults, not an established organization-wide ruleset. The lint selection explicitly lists all current stable Pyflakes (F) rules and selected import, whitespace, bug prevention, pytest, suppression, Ruff-specific, and type modernization rules. The Python template additionally checks E501 with a 120-character line limit. Each rule is documented in pyproject.toml; review the selection when upgrading Ruff.
- The pinned Ruff lint hook uses --fix, but automatic corrections are limited to safe fixes for I001, W291, W292, W293, F401, RUF100, UP006, and UP007. Other selected violations fail the hook. Unsafe fixes are not enabled. Review and stage hook changes before retrying a commit.
- The Pre-Commit hook set and pinned versions follow the supplied TiRex-2 configuration, while the template-specific Ruff rules and safe-fix allowlist are retained. Ruff formatting is automatically applied. pyupgrade targets Python 3.11 and may modernize syntax beyond the selected Ruff rules; its corrections are independent of Ruff's fixable allowlist.
- File hooks also check added file sizes (1,000 KB), filename case conflicts, executable/shebang consistency, JSON, merge conflicts, symlinks, TOML, YAML, debug statements, private-key patterns, line endings, test filenames, and whitespace. The TiRex-2 helper exclusion is retained; disabled reference hooks remain disabled.
- Installing Pre-Commit enables both pre-commit and commit-msg stages. Conventional Commit messages require a scope and one of chore, ci, docs, feat, fix, or test. CI runs the file hooks without checking commit messages; corrections made during CI fail the check rather than being committed automatically.
- GitHub Actions validates pushes and pull requests, including a package build. No deployment, publication, or release automation is included.
- Project name, description, responsible team, and license are unresolved TODOs. No license is assumed.
- Ignore patterns are only a guardrail; they cannot prove that a commit contains no secrets or customer data.
- CLA policy is separate and is not activated by this template.
