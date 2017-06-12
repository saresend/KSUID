<h1> Ksuid </h1>

<h3> What is a ksuid? </h3>

A ksuid is a K sorted UID. In other words, a KSUID also stores a date component, so that ksuids can be approximately 
sorted based on the time they were created. 


<h3> Quick overview </h3>

A ksuid is composed of two components: the date time, which is stored as the first four bytes of the uid, along with a randomly
generated payload of 16, for a total of 20 bytes. 


<h3> Installation </h3>

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


