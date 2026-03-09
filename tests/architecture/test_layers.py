from pytest_archon import archrule


def test_api_layer_dependencies():
    """Ensure API layer only depends on allowed layers."""
    (
        archrule("API layer dependencies")
        .match("{project}.api.*")
        .should_not_import("{project}.db.*")
        .should_not_import("{project}.models.*")
        .check("{project}")
    )


def test_service_layer_dependencies():
    """Ensure Service layer does not depend on API."""
    (
        archrule("Service layer dependencies")
        .match("{project}.services.*")
        .should_not_import("{project}.api.*")
        .check("{project}")
    )


def test_db_layer_dependencies():
    """Ensure DB layer only depends on models and core."""
    (
        archrule("DB layer dependencies")
        .match("{project}.db.*")
        .should_not_import("{project}.api.*")
        .should_not_import("{project}.services.*")
        .check("{project}")
    )


def test_models_layer_dependencies():
    """Ensure Models layer is independent of services and api."""
    (
        archrule("Models layer dependencies")
        .match("{project}.models.*")
        .should_not_import("{project}.api.*")
        .should_not_import("{project}.services.*")
        .check("{project}")
    )


def test_core_layer_dependencies():
    """Ensure Core layer is independent of all other project layers."""
    (
        archrule("Core layer dependencies")
        .match("{project}.core.*")
        .should_not_import("{project}.api.*")
        .should_not_import("{project}.services.*")
        .should_not_import("{project}.db.*")
        .should_not_import("{project}.models.*")
        .check("{project}")
    )


def test_no_circular_dependencies():
    """Ensure there are no circular dependencies between major packages."""
    (
        archrule("No circular dependencies")
        .match("{project}.*")
        .should_not_import_itself()
        .check("{project}")
    )
