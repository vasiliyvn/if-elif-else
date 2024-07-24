# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
name = int(input('first:'))
name1 = int(input('second:'))
name2 = int(input('third:'))
if name == name1 and name != name2 or name != name1 and name == name1:
    print(2)
elif name != name1 != name2:
    print(0)
elif name == name1 == name2:
    print(3)

