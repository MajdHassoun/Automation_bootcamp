class BasicErrorHandling:

    @staticmethod
    def read_file(file_path='./ni.txt'):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"The {file_path} not found")
        except IOError as e:
            print(e)

    @staticmethod
    def write_file(file_path='./ni.txt'):
        try:
            with open(file_path, 'w') as file:
                return file.write("owues8rhygf098")
        except FileNotFoundError:
            print(f"The {file_path} not found")
        except IOError as e:
            print(e)