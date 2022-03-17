class Unit:
    def __init__(self, name, job, level, experience):
        self.name = name
        self.job = job  # class is a protected word in python (look line 1 of this script...), so I have replace it with 'job'
        self.level = level
        self.experience = experience


# u1 = Unit('Roy', 'Lord', 1, 0)


def experienceCalculator():
    """
        This function calculates the amount of experience a unit receives after a successful attack or kill.
        This function is based on : https://serenesforest.net/the-sacred-stones/miscellaneous/calculations/ --> Experience
        (FE8 =? FE7 != FE6)
    """
