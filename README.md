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

to use, import: <br>
<code>from ksuid import KSUID</code>

To create a new ksuid, just call: <br> <code>KSUID()</code>


To get the timestamp:
<code> 
