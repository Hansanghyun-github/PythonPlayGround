import pytest

from datetime import datetime, timedelta
import arrow
from pytz import timezone
from zoneinfo import ZoneInfo

def test_now():
    dt: datetime = datetime.now()

    assert dt.tzinfo is None

def test_can_not_compare_naive_and_aware():
    dt1: datetime = datetime.now()
    dt2: datetime = datetime.now(timezone('Asia/Seoul'))

    with pytest.raises(TypeError):
        dt1 < dt2

def test_arrow_to():
    dt1: datetime = arrow.get('2025-03-10').datetime
    dt2: datetime = arrow.get('2025-03-10').to('Asia/Seoul').datetime

    assert dt1.time() == (dt2 - timedelta(hours=9)).time()
    assert dt1.date() == (dt2 - timedelta(hours=9)).date()

def test_arrow_replace():
    dt1: datetime = arrow.get('2025-03-10').datetime
    dt2: datetime = arrow.get('2025-03-10').replace(tzinfo='Asia/Seoul').datetime

    assert dt1.date() == dt2.date()
    assert dt1.time() == dt2.time()

def test_zone_info():
    dt1: datetime = datetime.now()
    dt2: datetime = datetime.now(ZoneInfo('Asia/Seoul'))

    assert dt1.tzinfo is None
    assert dt2.tzinfo is not None
    assert dt2.tzinfo.key == 'Asia/Seoul'