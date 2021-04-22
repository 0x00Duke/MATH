##
## EPITECH PROJECT, 2020
## B-MAT-200-BAR-2-1-107transfer-leon.ducasse
## File description:
## error_check.rb
##

require "./src/usage"

def is_str_valid(str)
    valid_char = "0123456789*"
    x = 0

    while x < str.length
        if !valid_char.include?str[x]
            return 84
        end
        x += 1
    end
    return 0
end

def is_arg_valid(av)
    x = 0
    while x < av.length
        if is_str_valid(av[x]) == 84
            return 84
        end
        x += 1
    end
    return 0
end

def error_check()
    av = ARGV
    if av.length == 1 && av[0] == "-h"
        usage()
        return 84
    elsif av.length < 2
        usage()
        return 84
    elsif !av.length.even?
        usage()
        return 84
    elsif is_arg_valid(av) == 84
        usage()
        return 84
    end
end