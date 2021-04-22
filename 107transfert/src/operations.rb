##
## EPITECH PROJECT, 2020
## B-MAT-200-BAR-2-1-107transfer-leon.ducasse
## File description:
## operations functions
##


def print_result(x, result)
	x = format("%0.3f", x)
	print (x)
	print(" -> ")
	result = format("%0.5f", result)
	print (result)
	print("\n")
end


def solve_this(arr, x)
	i = 0
	result = 0
	while i < arr.length()

		result = result + (arr[i] * (x**i))
		i += 1
	end
	return (result)
end


def get_expression(av)
	i = 0
	result_expression = [ ]

	while i < av.length()

		result_expression[i] = av[i].split('*').map{ |s| s.to_i }
		i += 1
	end
	return (result_expression)
end


def solve_expression(result_expression, x, av)
	i = 0

	while i < av.length()

		result_expression[i] = solve_this(result_expression[i], x)
		i += 1
	end
	return (result_expression)
end


def do_op(av)
	result_expression = [ ]
	expression = get_expression(av)
	result_division = [ ]
	result = 1.0
	x = 0.0
	power = 0
	i = 0

	while x <= 1.001

		while i < av.length()

			result_expression[i] = solve_this(expression[i], x)
			i += 1
		end
		i = 0
		while i < av.length

			result_division[i] = (result_expression[i] / result_expression[i + 1])
			i += 2
		end
		i = 0
		while i < result_division.length

			if result_division[i] != nil
				result = result * result_division[i]
			end
			i += 1
		end
		if (result.infinite?)
			exit(84)
		end
		if (result.nan?)
			exit(84)
		end
		print_result(x, result)
		result = 1
		i = 0
		x += 0.001
	end
end