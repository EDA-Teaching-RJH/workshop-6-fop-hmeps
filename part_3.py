def main():
    get_coordinate()

def get_coordinate():
        while True:
            try:
                _ = int(input("Enter an X-coordinate integer: "))
                if 100 < _  < -100:
                    print("Coordinate out of Range!")
            except ValueError:
                print("Invalid Coordinate")
            else:
               break
main()

#unsure how to include the if statement into the loop***