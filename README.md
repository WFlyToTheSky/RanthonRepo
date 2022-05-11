# Ranthon Guide
##### By: *Walter J Hare*
**Ranthon** is a collection of **Python** packages written by *Walter J Hare*. It also requires the **FileLog** project, which is automatically installed.
## InfSeq
**InfSeq** is a **Python** module that generates numbers in infinite sequences. So far it only includes two modules **CalFib** which generates numbers in the **Fibonacci Sequence** at a for a set number of rounds, and **CalFibLon**  which calculates the **Fibonacci Sequence** forever.
##### CalFib
The first attribute of **CalFib** is the amount of times you want to run the code, the second attribute is if you want to log the numbers or not *(Write True if you want to log it and False if you don't)* this feature uses the **FileLog** project.
###### The Code
&nbsp;

    def calfib(loop, log):
    n = 1
    x = 0
    p = x
    if log == True:
        for i in range(loop):
            x = n
            n = (n + p)
            Writer('current', False) >> n
            p = x
            Writer('previos', False) >> p
    else:
        for i in range(loop):
            x = n
            n = (n + p)
            p = x
    return n
##### CalFibLon
There is only one attribute to **CalFibLon** it is the log attribute which I mentioned on the **CalFib** section of the documentation, but I will state it again here. The checks  if you want to log the numbers or not *(Write True if you want to log it and False if you don't)* this feature uses the **FileLog** project.
###### The Code
&nbsp;

    def calfiblon(log):
    n = 1
    x = 0
    p = x
    if log == True:
        while True:
            x = n
            n = (n + p)
            Writer('current', False) >> n
            p = x
            Writer('previos', False) >> p
    if log == False:
        while True:
            x = n
            n = (n + p)
            p = x

# Conclusion
Thanks for reading my documentation and I hope you learned some stuff about how to use my python project **Ranthon**.