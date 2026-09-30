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

The GitHub workflow checks code quality, file hygiene, tests, and package building on pushes and pull requests. It does not deploy or publish anything. Pre-Commit checks common file hygiene and private-key patterns locally and in CI; these checks do not replace reviewing changes for sensitive material.

Keep credentials, customer data, and generated artifacts out of Git. The ignore rules prevent common accidental additions but cannot identify every confidential value; review changes before committing. If the project needs approved, synthetic test fixtures, narrow the relevant .gitignore rules explicitly so those fixtures can be tracked without admitting customer data.

See ASSUMPTIONS.md for decisions and limits inherited from the template proposal.
