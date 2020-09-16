from typing import List

from _pytest.nodes import Item
from pytest_pyppeteer.models import Pyppeteer


async def pytest_pyppeteer_targets_setup(item: Item):
    """Called to setup target before execute a test item."""


async def pytest_pyppeteer_targets_teardown(item: Item):
    """Called to teardown target after execute a test item."""


async def pytest_pyppeteer_all_targets_teardown(targets: List[Pyppeteer]):
    """Called to teardown all targets after execute all test items. e.g. make sure to close all targets."""


async def pytest_pyppeteer_all_targets_setup(targets: List[Pyppeteer]):
    """Called to setup all targets before execute all test items."""
