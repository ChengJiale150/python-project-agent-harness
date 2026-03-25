from pytest_archon import archrule


def test_api_layer_dependencies():
    """Ensure API layer only depends on allowed layers."""
    (
        archrule("API layer dependencies")
        .match("python_harness.api.*")
        .should_not_import("python_harness.db.*")
        .should_not_import("python_harness.models.*")
        .check("python_harness")
    )


def test_service_layer_dependencies():
    """Ensure Service layer does not depend on API."""
    (
        archrule("Service layer dependencies")
        .match("python_harness.services.*")
        .should_not_import("python_harness.api.*")
        .check("python_harness")
    )


def test_db_layer_dependencies():
    """Ensure DB layer only depends on models and core."""
    (
        archrule("DB layer dependencies")
        .match("python_harness.db*")
        .should_not_import("python_harness.api.*")
        .should_not_import("python_harness.services.*")
        .check("python_harness")
    )


def test_models_layer_dependencies():
    """Ensure Models layer is independent of services and api."""
    (
        archrule("Models layer dependencies")
        .match("python_harness.models*")
        .should_not_import("python_harness.api.*")
        .should_not_import("python_harness.services.*")
        .check("python_harness")
    )


def test_core_layer_dependencies():
    """Ensure Core layer is independent of all other project layers."""
    (
        archrule("Core layer dependencies")
        .match("python_harness.core*")
        .should_not_import("python_harness.api.*")
        .should_not_import("python_harness.services.*")
        .should_not_import("python_harness.db.*")
        .should_not_import("python_harness.models.*")
        .check("python_harness")
    )


def test_no_test_imports_in_production():
    """Ensure production code does not import from tests."""
    (
        archrule("No test imports in production")
        .match("python_harness.*")
        .should_not_import("tests.*")
        .check("python_harness")
    )
