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