#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ret = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            raise
    print("")
    return ret
if __name__ == "__main__":
    import doctest
    doctest.testmod()
