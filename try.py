while True:
    try:
        number = int(input("What's your fav number hoss\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure and enter a numver.")
    except ZeroDivisionError:
        print("Don't pick Zero")
    finally:
        print("Loop complete")