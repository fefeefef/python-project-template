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
- GitHub Actions validates pushes and pull requests, including a package build. No active deployment, publication, or release automation is included; inactive preparation examples are outside the workflows directory.
- Project name, description, responsible team, and license are unresolved TODOs. No license is assumed.
- Ignore patterns are only a guardrail; they cannot prove that a commit contains no secrets or customer data.
- CLA policy is separate and is not activated by this template.

- The user-facing README follows the TiRex-2 structure with optional, commented badge placeholders. It does not claim an existing publication or hosted documentation.
- Sphinx follows the tool explicitly named in the feedback. MyST parses Markdown notes; documentation builds but is not deployed.
- LICENSE is an intentionally empty placeholder. Maintainers must choose the license, security contact, supported releases, and any response expectations.
- Dependabot uses the uv ecosystem to update the manifest and lockfile, plus GitHub Actions updates. This adapts the reference to the existing dependency workflow.
- Line and branch coverage of the package and own scripts was explicitly approved for reporting only. There is no minimum percentage, warning threshold, or merge gate; Codecov upload is an explicit opt-in through the repository Actions variable CODECOV_ENABLED; it defaults to off in a newly created repository.
- The workflow is named testing. Package metadata and installation of the built wheel are checked without publishing. The starter wheel has no runtime dependencies; adapt its isolated smoke check when adding dependencies.
- No additional lint rules, automatic corrections, scientific methods, or notebook failure conditions are introduced by this update. Coverage collection follows the explicit reporting-only decision.

- GitHub Actions references are pinned to verified commit SHAs. CI installs uv 0.13.5; dependency versions remain locked in uv.lock.

- The Setuptools build backend is pinned to the version verified for this starter.
  This controls the backend version without promising byte-identical builds or
  locked transitive dependencies in Pre-Commit's separate hook environments.
