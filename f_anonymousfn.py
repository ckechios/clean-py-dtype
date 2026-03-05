def increase_by(pct):
    """ Increase a value by 5% """
    return pct*1.05

print("Increase 100 by 5%", increase_by(100))

anon_increase = lambda p: p * 1.05

print(type(anon_increase), "Increase 100 by 5%", anon_increase(100))

print("Increase 100 by 5% using anonymous function: ", (lambda p: p * 1.05)(100))

