import os
import tempfile

import pytest


@pytest.fixture
def temp_cwd():
    """
    Change the current working directory to a temporary directory, reverting
    back to the real current working directory afterwards.
    """
    real_cwd = os.getcwd()

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            os.chdir(temp_dir)
            yield temp_dir

    finally:
        os.chdir(real_cwd)
