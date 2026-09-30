"""Verify that the package can be imported after installation."""

from importlib import import_module


def test_package_is_importable() -> None:
    assert import_module("project_name").__name__ == "project_name"
