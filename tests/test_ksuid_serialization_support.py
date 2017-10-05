import string
import time

from ksuid import ksuid


def test_converts_to_base62_and_returns_value_with_numbers_and_letters():
    valid_symbols = string.digits + string.ascii_letters

    uid = ksuid()
    value = uid.toBase62()

    assert value is not None
    assert len(value) > 0

    for v in value:
        assert v in valid_symbols


def test_successfully_converts_to_base62_and_vice_versa():
    uid1 = ksuid()
    serialized = uid1.toBase62()

    uid2 = ksuid.fromBase62(serialized)

    assert str(uid1) == str(uid2)
    assert uid1.bytes() == uid2.bytes()
    assert uid1.toBytes() == uid2.toBytes()
    assert uid1.toBase62() == uid2.toBase62()


def test_successfully_converts_to_bytes_and_vice_versa():
    uid1 = ksuid()
    serialized = uid1.toBytes()

    uid2 = ksuid.fromBytes(serialized)

    assert str(uid1) == str(uid2)
    assert uid1.bytes() == uid2.bytes()
    assert uid1.toBytes() == uid2.toBytes()
    assert uid1.toBase62() == uid2.toBase62()


def test_base62_orderable():
    list = []
    for _ in range(1000):
        list.append(ksuid())

    sorted_list = sorted(list, key=lambda x: x.toBase62(), reverse=True)

    for index in range(len(list) - 1):
        assert sorted_list[index].getTimestamp() >= sorted_list[index + 1].getTimestamp()


def test_measure_1s_and_compare_ksuids():
    DELAY_INTERVAL_SECS = 1

    u1 = ksuid()
    time.sleep(DELAY_INTERVAL_SECS)
    u2 = ksuid()

    assert u1.toBase62() < u2.toBase62()

    assert u2.getTimestamp() > u1.getTimestamp()
    assert (u2.getTimestamp() - u1.getTimestamp()) >= 1

    d2 = u2.getDatetime()
    d1 = u1.getDatetime()
    assert d2 > d1
    assert (d2 - d1).total_seconds() >= 1

    assert u1.getPayload() != u2.getPayload()


def test_integration_test():
    uid1 = ksuid()
    bu = uid1.toBytes()

    assert bu is not None

    uid2 = ksuid.fromBytes(bu)

    assert str(uid1) == str(uid2)
    assert uid1.bytes() == uid2.bytes()
    assert uid1.toBytes() == uid2.toBytes()
    assert uid1.toBase62() == uid2.toBase62()

    b62 = uid1.toBase62()
    uid3 = ksuid.fromBase62(b62)

    assert str(uid1) == str(uid3)
    assert uid1.bytes() == uid2.bytes()
    assert uid1.toBytes() == uid3.toBytes()
    assert uid1.toBase62() == uid3.toBase62()

    bs = uid1.bytes()
    assert bs is not None


def test_bulk_test_for_base62_with_delays():
    list = []
    for _ in range(100):
        list.append(ksuid())
        time.sleep(0.01)

    sorted_list = sorted(list, key=lambda x: x.toBase62(), reverse=True)

    for index in range(len(list) - 1):
        assert sorted_list[index].getTimestamp() >= sorted_list[index + 1].getTimestamp()
