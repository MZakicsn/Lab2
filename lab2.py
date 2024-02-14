import sys

def print_arguments(script_name, *variables):
    print(f"Script Name: {script_name}")
    print(f"Variables: {variables}")
    print(f"Script with Variables: {script_name} {variables}")

if __name__ == "__main__":
    script_name = sys.argv[0]
    variables = sys.argv[1:]

    print_arguments(script_name, *variables)

# Text from Professor LAb
def helloWorld():
	print ('helloWorld')
helloWorld()

print('Code by Mzikria')