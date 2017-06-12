<h1> Ksuid </h1>

<h1> What is a ksuid? </h1>

A ksuid is a K sorted UID. In other words, a KSUID also stores a date component, so that ksuids can be approximately 
sorted based on the time they were created. 


<h1> Quick overview </h1>

A ksuid is composed of two components: the date time, which is stored as the first four bytes of the uid, along with a randomly
generated payload of 16, for a total of 20 bytes. 

<h2> A few advantages </h2>

1. The potential number of IDs available is greater than even that of UUID4 (which accepts 122 bits). KSUIDs are about 64 times larger than that. Coupled with the timestamp, the likelihood of getting 2 identical Ksuids is exceedingly low

2. Enables sorting of UIDs in a sensible fashion, based on their timestamp.


<h2> Installation </h2>

The ksuid library can be installed via pip:
<code>pip install ksuid</code>

<h3> Note: currently only tested for Python 3.x </h3>
<h2> Documentation </h2>
Sample usage:

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


<h1> Credit, where credit is due </h1>

This library is largely inspired by the go version, found here:
https://github.com/segmentio/ksuid
