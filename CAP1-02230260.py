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
# Your Solution Score: 49894
# Put your number here : 0
################################
# Read the input.txt file
def read_input():
   with open('input_0_cap1.txt', 'r') as my_file:
        for line in my_file:
            yield line.strip()

def calculate_score(lines):
    score = {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}
    total_score = 0
    for line in lines:
        key = line.strip()
        value_in_dict = score.get(key, None)
        if value_in_dict is not None:
            total_score += value_in_dict
    print("The total score is:", total_score)


calculate_score(read_input())

