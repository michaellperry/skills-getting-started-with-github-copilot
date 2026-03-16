import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture(scope="session")
def baseline_activities():
    return copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities_state(baseline_activities):
    app_module.activities = copy.deepcopy(baseline_activities)


@pytest.fixture
def client():
    return TestClient(app_module.app)
