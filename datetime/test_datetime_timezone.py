import pytest

from datetime import datetime, timedelta
import arrow
from pytz import timezone

def test_now():
    dt: datetime = datetime.now()

    assert dt.tzinfo is None

def test_can_not_compare_naive_and_aware():
    dt1: datetime = datetime.now()
    dt2: datetime = datetime.now(timezone('Asia/Seoul'))

    with pytest.raises(TypeError):
        dt1 < dt2

