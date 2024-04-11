################################
# Your Name:Bishal Mpngar
# Your Section : Mechanical Engineering 
# Your Student ID Number : 02230260
################################
# REFERENCES
# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa0lWbFZfS0NYSUdzLThGQ2tEYms3akI0aEdpQXxBQ3Jtc0ttLXRqMjV6eU4zanpJOXI5a0tBTWQ1WlZTZHc0NU5QVEVzWlVYS0FOVHhoRVRCLWdXZFg5MXhnVkxBOVB2ejlwQVhPS2xhby14d0U3MXc0R054Wnc5dXB5MjZ1c1ZfdTIxRlBTb2pOWThMSDdLZ1JlNA&q=https%3A%2F%2Fwww.codewithharry.com%2Fvideos%2Fpython-tutorials-for-absolute-beginners-28&v=ZNIe4Nf-6-c
# https://youtu.be/TSHEnfUz6wk?si=uRvCkHqooCafele2
# https://www.w3schools.com/python/python_file_open.asp
# https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/
#https://www.w3schools.com/python/python_for_loops.asp
################################
# SOLUTION
# Your Solution Score: 50054
# Put your number here : 0
################################
# Read the input.txt file
def read_input():
    f = open('input_0_cap1.txt', 'r')
    print(f.read())
    f.close()

   
def calculate_score():
    f = open('input_0_cap1.txt', 'r')
    read_file = f.read()
    marks =0
    for i in read_file:
        if i =="A":
            marks += 1
        elif i == "B":
            marks += 2
        elif i=="C":
            marks += 3
        elif i == "X":
            marks += 0
        elif i == "Y":
            marks += 3
        elif i == "Z":
            marks += 6

    print("The total marks is ", marks)

read_input()
calculate_score()

