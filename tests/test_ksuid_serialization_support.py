import string

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
    assert uid1.toBase62() == uid2.toBase62()


def test_successfully_converts_to_bytes_and_vice_versa():
    uid1 = ksuid()
    serialized = uid1.toBytes()

    uid2 = ksuid.fromBytes(serialized)
    assert str(uid1) == str(uid2)
    assert uid1.bytes() == uid2.bytes()


def test_base62_orderable():
    list = []
    for _ in range(1000):
        list.append(ksuid())

    sorted_list = sorted(list, key=lambda x: x.toBase62(), reverse=False)

    for index in range(len(list) - 1):
        assert sorted_list[index].getTimestamp() >= sorted_list[index + 1].getTimestamp()
