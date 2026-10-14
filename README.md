# TODO: Project name

TODO: Describe what this project does.

## Use this template

Copy this directory as the starting point for a new repository. Complete the TODOs below, then run uv lock to refresh uv.lock after changing project metadata or dependencies. Python 3.11, uv with a committed lockfile, and the Ruff rules are starting choices for this template; align the Python requirement, Ruff target, CI version, and dependency workflow with the actual project. Follow existing organization rules when they prescribe different settings.

## Before first use

- [ ] TODO: Replace the project name in this README and pyproject.toml.
- [ ] TODO: Rename src/project_name and update the import in tests/test_package.py.
- [ ] TODO: Replace the project description.
- [ ] TODO: Choose a license and add its approved license file or metadata.
- [ ] TODO: Name the responsible team or maintainers.
- [ ] Check current organization rules before adopting this optional template.

## Local setup

Install uv, then run:

    uv sync --locked --group dev
    uv run --locked pytest
    uv run --locked ruff check .
    uv run --locked ruff format --check .

After initializing Git, enable the local hooks:

    uv run --locked pre-commit install
    uv run --locked pre-commit run --all-files

The Pre-Commit hook set follows the supplied TiRex-2 configuration: file hygiene and structure checks, a 1,000 KB limit for newly added files, Python syntax modernization with pyupgrade, Ruff linting and automatic formatting, and Conventional Commit messages. Hook versions are pinned in `.pre-commit-config.yaml`. The template's Ruff rule selection and `fixable` allowlist remain in `pyproject.toml`; only available safe Ruff lint fixes from that allowlist are applied. pyupgrade, the formatter, and file hygiene hooks perform their own corrections independently of Ruff's `fixable` setting. If a hook modifies files, review `git diff`, stage the changes, and retry the commit.

The install command enables both `pre-commit` and `commit-msg` stages. Commit messages require a type and scope, for example `fix(notebooks): correct data loading`. Allowed types are `chore`, `ci`, `docs`, `feat`, `fix`, and `test`. `pre-commit run --all-files` checks files; the message hook runs when committing. To check a message manually:

    uv run --locked pre-commit run --hook-stage commit-msg --commit-msg-filename /path/to/message.txt

CI runs the file hooks; it does not validate commit messages. Automatic corrections in CI fail the check so the corrected files must be committed locally.

The GitHub workflow checks code quality, file hygiene, tests, and package building on pushes and pull requests. It does not deploy or publish anything. Pre-Commit checks common file hygiene and private-key patterns locally and in CI; these checks do not replace reviewing changes for sensitive material.

Keep credentials, customer data, and generated artifacts out of Git. The ignore rules prevent common accidental additions but cannot identify every confidential value; review changes before committing. If the project needs approved, synthetic test fixtures, narrow the relevant .gitignore rules explicitly so those fixtures can be tracked without admitting customer data.

See ASSUMPTIONS.md for decisions and limits inherited from the template proposal.
