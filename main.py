# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
# template= f"what's up {name}"
# name=Bob
name = ""


def greet(name='Bob', greeting="Hello, <name>!"):
    x = greeting.replace("<name>", name)
    print(x)
    return x


greet()
greet('Bob', "What's up, <name>!")
greet("Kate", "How do you do <name> ")


def force(mass=9.8, body='earth'):
    gravity_dictionary = {
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.8,
        'venus': 8.8,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
    }
    print(gravity_dictionary[body])
    # pass argumet body to find value i dict
    force = mass * gravity_dictionary[body]
    print(force)
    return round(force)


force()
force(4, "pluto")


def pull(m1, m2, d):
    G = 6.674 * 10**-11
    gravitional_pull = G * ((m1*m2)/d**2)
    print(round(gravitional_pull))
    return gravitional_pull


pull(1800, 1500, 3)









