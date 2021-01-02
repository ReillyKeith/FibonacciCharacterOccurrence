# Program to display the Fibonacci sequence up to n-th term
import numpy
import matplotlib.pyplot as plt

def main():
    # first two terms
    n1, n2 = 0, 1
    nO = []
    count = 0

    nterms = int(input("How many terms? "))

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(f"Fibonacci Num: {n1}")
            print(f"Len:{len(str(n1))}")
            nO.append(len(str(n1)))
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

    unique, counts = count_unique(nO)
    plot_graph(unique, counts, nterms)


def count_unique(data):
    a = numpy.array(data)
    unique, counts = numpy.unique(a, return_counts=True)
    return unique, counts


def plot_graph(unique, counts, nterms):
    plt.scatter(unique, counts, c=unique)  # plotting by columns
    plt.locator_params(axis="both", integer=True, tight=True)
    plt.margins(0.05)
    plt.tight_layout()
    plt.suptitle(f'Fibonacci Sequence: {nterms}', fontsize=20)
    plt.xlabel('Character Count:', fontsize=12)
    plt.ylabel('Occurrence Count:', fontsize=12)
    ax = plt.gca()
    ax.set_xticks(unique)
    plt.savefig(f'Fibonacci_Sequence_{nterms}.pdf', bbox_inches='tight')

if __name__ == "__main__":
    main()
