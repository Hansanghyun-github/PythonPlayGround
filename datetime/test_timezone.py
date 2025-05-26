import pytest

from datetime import datetime, timedelta
import arrow
import pytz
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

def test_2():
    dt1 = arrow.now().replace(tzinfo='Asia/Seoul')
    print(dt1.datetime)
    print("replace: ", type(dt1.datetime.tzinfo))
    dt1 = arrow.now().to(tz='Asia/Seoul')
    print("to: ", type(dt1.datetime.tzinfo))

    # Asia/Seoul 타임존 적용
    tz = pytz.timezone('Asia/Seoul')
    dt1 = datetime(2025, 3, 10, 12, 0, 0, tzinfo=tz)

    print("pytz: ", type(dt1.tzinfo))

    dt1 = datetime(2025, 3, 10, 12, 0, 0, tzinfo=ZoneInfo('Asia/Seoul'))

    print("zoneinfo: ", type(dt1.tzinfo))


def test_3():
    dt1 = arrow.now()
    print(dt1.datetime)
    print(dt1)

    dt1 = arrow.now(tz='Asia/Seoul')
    print(dt1.datetime)
    print(dt1)

    dt1 = arrow.now(tz='UTC')
    print(dt1.datetime)
    print(dt1)


def test_timezone_overwrite():
    dt1 = arrow.get('2025-05-26 12:34:56+0900').to('UTC')
    assert dt1.datetime == datetime(2025, 5, 26, 3, 34, 56, tzinfo=ZoneInfo('UTC'))
    dt2 = arrow.get('2025-05-26 12:34:56+0900', tzinfo='UTC')

    assert dt2.datetime == datetime(2025, 5, 26, 12, 34, 56, tzinfo=ZoneInfo('UTC'))