import math
from decimal import *
from filelog import Writer
import random

def calpidart(seed, rounds, log):
    inside = 0
    random.seed(seed)

    if log == True:
        for i in range(rounds):
            # compute position of the point
            x = random.uniform(0.0, 1.0)
            y = random.uniform(0.0, 1.0)
            result = x*x + y*y
            if (result <= 1.0):
                inside += 1
            Writer('current', False) >> inside

    else:
        for i in range(rounds):
            # compute position of the point
            x = random.uniform(0.0, 1.0)
            y = random.uniform(0.0, 1.0)
            result = x*x + y*y
            if (result <= 1.0):
                inside += 1

    return(inside)

def calpidartlon(seed, log):
    inside = 0
    random.seed(seed)

    if log == True:
        while True:
            # compute position of the point
            x = random.uniform(0.0, 1.0)
            y = random.uniform(0.0, 1.0)
            result = x*x + y*y
            if (result <= 1.0):
                inside += 1
            Writer('current', False) >> inside

    else:
        while True:
            # compute position of the point
            x = random.uniform(0.0, 1.0)
            y = random.uniform(0.0, 1.0)
            result = x*x + y*y
            if (result <= 1.0):
                inside += 1

def calpivie(rounds, digetmax, log):
    purple = Decimal(math.sqrt(2))
    answer = Decimal(purple / 2)
    getcontext().prec = digetmax

    if log == True:
        for i in range(rounds):
            purple = Decimal(math.sqrt(2 + purple))
            answer = Decimal(answer * (purple / 2))
            Writer('current', False) >> Decimal(2 / answer)
    else:
        for i in range(rounds):
            purple = Decimal(math.sqrt(2 + purple))
            answer = Decimal(answer * (purple / 2))
                      
    return(Decimal(2 / answer))

def calpivielon(digetmax, log):
    purple = Decimal(math.sqrt(2))
    answer = Decimal(purple / 2)
    getcontext().prec = digetmax

    if log == True:
        while True:
            purple = Decimal(math.sqrt(2 + purple))
            answer = Decimal(answer * (purple / 2))
            Writer('current', False) >> Decimal(2 / answer)
    else:
        while True:
            purple = Decimal(math.sqrt(2 + purple))
            answer = Decimal(answer * (purple / 2))
