
"""
For this problem, imagine you are asked to write a program for NYU.
The task is to be able to quickly look up a student by Net ID.
That should yield a record that includes the student's name, and
also a list of the courses the student has taken, organized by 
semester.
You should prompt the user "What Net ID do you want?"
The user of your program can type "ejc369," and "Eugene Callahan"
will appear.
(You should also handle the ID not being there! But you don't
need to loop: just print a message and exit.)
Then prompt the user "What semester do you want?"
The user could type "2020S" and you will give them a list like:
    "CS1114, CS2124, AG3421"
(You should check for a missing semester as well!)
All of the data can be made up!
"""

# sample code:
students = {"ejc369": {"name": "Eugene Callahan",
                       "2020S": ["CS1114", "CS2124", "AG3421"]},
            "pdp456": {"name": "PDP-8",
                       "1992F": ["DP453", "DP567"]}}

netID = input("What NetID do you want? ")
if netID in students:
    print(students[netID]["name"])
    semester = input("What semester do you want? ")
    if semester in students[netID]:
        print(students[netID][semester])
    else:
        print(students[netID]["name"],
              "took no classes that semester!")
else:
    print("NetID not found.")

"""
Write a simple program to check if a number is prime.
(A prime number is divisible only by 1 and itself.)
Use the modulus operator in your check.
When we say "simple" we mean you don't need to worry
about extra checks: of course, if a number is not
divisible by 2, it is also not divisible by 4, but
you can check 4 anyway. But for full points, stop
checking at the smallest number possible.
(For example, for 9, you *can't* stop checking at 2:
    you would miss the fact that 9 is divisible by 3.)
Ask the user for the number to check.
Don't worry about exceptions!
And you might want to use "import math" here!
"""

# sample code:
import math

num_to_check = int(
    input("Enter a number and I will tell you if it's prime: "))
stop = math.floor(math.sqrt(num_to_check)) + 1
is_prime = True
for i in range(2, stop):
    if num_to_check % i == 0:
        print(num_to_check, "is not prime: divisible by", i)
        is_prime = False
        break
if is_prime:
    print(num_to_check, "is indeed prime!")

"""

"""

