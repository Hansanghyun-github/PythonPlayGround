from datetime import timedelta
import arrow

def test_now_timezone():
    dt1 = arrow.now().replace(microsecond=0).datetime
    dt2 = arrow.now(tz='Asia/Seoul').replace(microsecond=0).datetime

    assert dt1 == dt2

def test_now_timezone2():
    dt1 = arrow.now().replace(microsecond=0).datetime
    dt2 = arrow.now(tz='UTC').replace(microsecond=0).datetime

    assert dt1.time() == (dt2 + timedelta(hours=9)).time()

def test_span_range():
    datetime = arrow.get('2025-01-01T00:00:00')

    span = arrow.Arrow.span_range('day', datetime, datetime)

    result = list(span)
    assert len(result) == 1
    assert result[0][0] == datetime
    assert result[0][1] == datetime + timedelta(days=1, microseconds=-1)

def test_span_range2():
    datetime = arrow.get('2025-01-01T00:00:00')

    span = arrow.Arrow.span_range('day', datetime, datetime + timedelta(days=1))

    result = list(span)
    assert len(result) == 2

    assert result[0][0] == datetime
    assert result[0][1] == datetime + timedelta(days=1, microseconds=-1)

    assert result[1][0] == datetime + timedelta(days=1)
    assert result[1][1] == datetime + timedelta(days=2, microseconds=-1)
