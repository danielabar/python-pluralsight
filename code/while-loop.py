while True:
    # get input from the user
    response = input()
    # test if user provided value is evenly divisible by five
    if int(response, 10) % 5 == 0:
        break
