#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            try:
                val1 = float(my_list_1[i]) if isinstance(my_list_1[i], (int, float)) else None
                val2 = float(my_list_2[i]) if isinstance(my_list_2[i], (int, float)) else None
                if val2 == 0:
                    raise ZeroDivisionError
                elif val1 is None or val2 is None:
                    raise TypeError
                new_list.append(val1 / val2)
            except ZeroDivisionError:
                print('division by 0')
                new_list.append(0)
            except TypeError:
                print('wrong type')
                new_list.append(0)
    except IndexError:
        print("out of range")
        new_list.append(0)
    finally:
        return new_list
