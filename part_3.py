def main():
    get_coordinate()

def get_coordinate():
        while True:
            try:
                _ = int(input("Enter an X-coordinate integer: "))
                print(_)
                break
            except ValueError:
                print("Invalid Coordinate")
main()