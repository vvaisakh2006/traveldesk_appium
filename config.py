from fixture.application import Application
import pytest


@pytest.fixture()
def app():
    fixture = Application()
    return fixture


