import apis
import time
import socket


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


def compiler(source):
    """compiles the input source code and returns output."""
    compiler_req = apis.Compiler(source)
    return compiler_req.pyresponse['output']


def point_finder(source, N):
    """uses compiler function to get the output of user source and finds a point based on output and N."""
    final_source = f"N = {N}\n" + source
    output = compiler(final_source)
    tup = (N, len(output))

    # TEST not important, just to print log
    print(f"""      N={N}
                output: {output}
                len(output) = {len(output)}
                found point: {tup}
    ##########################################""")
    # TSET
    return tup


def plot(power, power2=0):
    """first generates the plot.py file then executes it."""
    plot_file = open('plot.py', 'w+')
    plot_file.write(f"""\n
import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0., 1, 0.03)
plt.title('Algorithm Complexity')
plt.ylabel('Output Length')
plt.xlabel('N')
plt.plot(t, t ** {power}, 'g-', label=f"n*{power}")
plt.plot(t, t ** {power2} , 'r-', label=f"n*{power2}")
plt.show()
""")

    plot_file.close()
    exec(open("./plot.py").read())


def equation_finder(usr_src):
    """using the function point_finder, this function creates a list of tuples and sends it to dcode.fr api
       to find the final equation."""
    points = ""
    for i in range(0, 21, 5):
        points += str(point_finder(usr_src, i))

    print("final points are: {}".format(points))
    equation_req = apis.DcodeFR(points)
    equation = equation_req.output['results']
    print(f"Equation: {equation.strip('$$')}")
    bigo = "O(n"
    power = ""
    for i, letter in enumerate(equation):
        if letter == 'x' and equation[i + 1] == "^":
            bigo += equation[i + 1:i + 3] + ")"
            power += equation[i + 2]
            print(power)
            break
    else:
        bigo += ")"
    print(f"Estimated Algorithm Complexity(BIG O notation): {bigo}")

    lizt = [bigo, power]
    return lizt

# equation_finder("""for i in range(0, N):
#     for j in range(0, N):
#         for k in range(0, N):
#             print("*", end='')""")

# equation_finder("""i = 1
# while i < N:
#     print("*", end='')
#     i *= 2""")

# import numpy as np
# import matplotlib.pyplot as plt
#
# t = np.arange(0., 1, 0.03)
# plt.title('Algorithm Complexity')
# plt.ylabel('Output Length')
# plt.xlabel('N')
# plt.plot(t, t ** 1, 'g-')
# plt.plot(t, t ** 2, 'r-')
# plt.show()
