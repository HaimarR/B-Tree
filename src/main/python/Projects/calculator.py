import function_curator as fcur

class FindDerivative:
    __slots__ = ["__a_function", "__incogs", "__powers", "__signs", "__x_indexes"]

    def __init__(self, a_function):
        my_function, incogs, powers, signs, x_indexes = fcur.curate(a_function)
        self.__a_function = my_function
        self.__incogs = incogs
        self.__powers = powers
        self.__signs = signs
        self.__x_indexes = x_indexes

    def __repr__(self):
        new_function = self.get_derivative()
        signs = self.__signs
        print(signs)

        derivative = ""
        for index in range(len(new_function)):
            derivative += new_function[index] + " " + signs[index] + " "

        if derivative[len(derivative) - 2] == signs[len(signs) - 1]:
            return derivative[:-3]
        else:
            return derivative[:-1]
        
    def get_function(self):
        return self.__a_function

    def get_derivative(self):
        coefficients, powers = self.power_rule()

        new_function = []
        for index in range(len(coefficients)):
            new_function.append(str(coefficients[index]) + "x" + str(powers[index]))

        return new_function

    def power_rule(self):
        a_function = self.__a_function
        powers = self.__powers
        x_indexes = self.__x_indexes
        print(x_indexes)
        
        new_powers = []
        new_coefficients = []
        index = 0
        for power in powers:
            new_power = int(powers[power]) - 1
            coefficient = power[:x_indexes[index]]
            try:
                coefficient = int(coefficient)
            except ValueError:
                coefficient = 1
            new_coefficient = coefficient * int(powers[power])
            new_coefficients.append(new_coefficient)
            new_powers.append(power[x_indexes[index] + 1:-1] + str(new_power))
            index += 1

        return new_coefficients, new_powers

def main():
    my_func = "2x**3 + x**2 + 2x"
    new_func = FindDerivative(my_func)
    print(new_func)

if __name__ == "__main__":
    main()