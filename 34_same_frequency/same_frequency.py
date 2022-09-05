from distutils.command.build_scripts import first_line_re


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    first_freq = {}
    second_freq = {}
    
    for x in str(num1):
        first_freq[x] = first_freq.get(x, 0) + 1

    for x in str(num2):
        second_freq[x] = second_freq.get(x, 0) + 1

    return first_freq == second_freq    