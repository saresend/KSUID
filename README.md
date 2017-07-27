# KSUID

## What is a ksuid?

A ksuid is a K sorted UID. In other words, a KSUID also stores a date component, so that ksuids can be approximately 
sorted based on the time they were created. 


## Quick overview

A ksuid is composed of two components: the date time, which is stored as the first four bytes of the uid, along with a randomly
generated payload of 16, for a total of 20 bytes. 

## A few advantages

1. The potential number of IDs available is greater than even that of UUID4 (which accepts 122 bits). KSUIDs are about 64 times larger than that. Coupled with the timestamp, the likelihood of getting 2 identical Ksuids is exceedingly low;
2. Enables sorting of UIDs in a sensible fashion, based on their timestamp;
3. Supports Base62 encoding - can be serialized to Base62 and vice versa


## Installation

The ksuid library can be installed via pip:

```pip install ksuid```

** Note: currently only tested for Python 3.x </h3>**
## Sample Usage:

```python
>>> from ksuid import ksuid
>>> x = ksuid()
>>> print(x) 
>>> '05cbd3454355fe1e1f11c85bb2c1e3e2f7c93525 '
>>> x.getTimestamp()
>>> 1497243973
>>> x.getDatetime() 
>>> datetime.date(2017, 6, 11)
>>> x 
>>> <ksuid.ksuid object at 0x100784a90> 
>>> x.bytes()
>>> b'\x05\xcb\xd7\xd0\xc6\xcb\x98i\xeb\xa0}\xfa\x0f\x87\xf1\xf1\xe8\xa1\x83\x9e'
```

## Base62 support

```python
>>> import ksuid
>>> uid = ksuid.ksuid()
>>> print(uid)
>>> '0607ac1e7955e3d6a5da87c8dae2e1825c8ddfc9'
>>> v = uid.toBase62()
>>> print(v)
>>> 'rLIliIsDsLNj1b4tN1T3TZGC1B'
```

## Serialization to bytes support

```python
>>> import ksuid
>>> uid = ksuid.ksuid()
>>> print(uid)
>>> '0607ac7351a48bb5e2f63b68094e465010496ff6'
>>> v = uid.toBytes()
>>> print(v)
>>> b'\x06\x07\xacsQ\xa4\x8b\xb5\xe2\xf6;h\tNFP\x10Io\xf6'
```

## Developing

First of all you need `make` utility for a little bit comfortable usage.

You can execute `make help` to view all available commands.

Please, run `make` to install virtual environment for testing and development.

Supported commands:

* `make` - create virtual env and setup dependencies;
* `make tests` - run tests;
* `make coverage` - run tests with coverage report;
* `make lint` - check linting;
* `make flake8` - alias for `make lint`
* `make clean` - remove more or less everything created by make

## Credit, where credit is due

This library is largely inspired by the go version, found here:
https://github.com/segmentio/ksuid

