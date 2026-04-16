from task4 import app

import pytest
from dash.testing.composite import DashComposite


@pytest.fixture
def dash_duo():
    """Fixture to create a Dash test client"""
    with DashComposite(app) as dc:
        yield dc


def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=10)


def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#visualization", timeout=10)


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=10)
