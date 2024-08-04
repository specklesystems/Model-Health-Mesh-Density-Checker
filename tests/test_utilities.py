import pytest
from specklepy.objects.base import Base
from specklepy.objects.geometry import Mesh

from src.utilities.utilities import is_displayable_object, try_get_display_value, get_byte_size


@pytest.fixture
def sample_bases():
    base_with_display_value = Base()
    base_with_display_value.displayValue = [Mesh()]

    base_without_display_value = Base()

    return base_with_display_value, base_without_display_value


def test_is_displayable_object(sample_bases):
    base_with_display_value, base_without_display_value = sample_bases

    assert is_displayable_object(base_with_display_value)
    assert not is_displayable_object(base_without_display_value)

    # assert that teh count of the sample_bases that is displayable is 1
    assert sum(1 for b in sample_bases if is_displayable_object(b)) == 1


def test_try_get_display_value(sample_bases):
    base_with_display_value, base_without_display_value = sample_bases

    print(try_get_display_value(base_with_display_value)[0])

    assert try_get_display_value(base_with_display_value) is not None
    assert try_get_display_value(base_without_display_value) is None


def test_get_byte_size(sample_bases):
    base_with_display_value, base_without_display_value = sample_bases

    print(base_with_display_value.displayValue)

    assert get_byte_size(base_with_display_value) > 0
    assert get_byte_size(base_without_display_value) == 0
