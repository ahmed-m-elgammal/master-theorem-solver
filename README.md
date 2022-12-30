# Project Title

Master theorem solver

## Description

Solving the recursion using master theorem solver

## Getting Started

### Dependencies

* Python >= 3.6 libraries math , re
* ex. Windows 10

### Installing

* pip install math
* pip install re

### Executing program

* How to run the program
Frist download the data of (Explore US Bikeshare Data) from kaggle and put in with same path of the code
```
python solve_recurrence.py
```
# Input
```
Format: T(n) = aT(n/b)+ f(n)
    where f(n) = O(n^k * log(n)^p)
    Case #1 : if log(a,b) > k, then T(n) = O(n^log(a,b))
    Case #2 : if lag(a,b) == k, then if p>-1, T(n) = O(n^k * log(n)^p+1)
                                    if p =-1, T(n) = O(n^k loglog(n))
                                    if p<-1, T(n) = O(n^k)
    Case #3 : if log(a,b) < k, then if p>=0, T(n) = O(n^k * log(n)^p)
                                    if p<0, T(n) = O(n^k)

```
## Authors

contact info

ex. [@me](https://www.linkedin.com/in/ahmed-m-elgammal/)

