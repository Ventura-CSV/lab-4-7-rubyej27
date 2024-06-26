def main():
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    previous_value = None
    
    while True:
        current_value = int(input('Enter an integer: '))
        
        if previous_value is None or current_value <= previous_value:
            numbers.append(current_value)
            previous_value = current_value
        else:
            break
    

    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
