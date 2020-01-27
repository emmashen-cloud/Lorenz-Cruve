# Lorenz-Cruve
The attached NumPy file contains the population of N=200+ countries and territories in 2010 (in mln. people).

A Lorenz curve shows the contribution to the common "wealth" (in our case, the common population) of the bottom x "people" (in our case, the countries). For example, y(1) is the contribution of the smallest country, y(2) is the contribution of the two smallest countries, and y(N) is the total contribution (which is equal to either 1.0 or 100%). Typically, the range of x is normalized either to 0.0-1.0 or 0%-100%, too.

Using only NumPy and matplotlib, plot the Lorenz curve for the population data. The curve shall be normalized both in X and Y dimensions to the range from 0.0 to 1.0. The program shall not use any loops or non-array arithmetic operations.

Make sure the plot has the axes labels and a title. The program shall save the plot as population-lorenz.png with the resolution of 200dpi. 

Deliverables: a complete Python program that reads the data from pop2010.npy (located in the same folder as the program itself) and produces the PNG file, all without any human interaction.
