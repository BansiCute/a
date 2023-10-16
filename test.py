questions = [
    {
        'question': 'What is the capital of France?',
        'answers': ['Paris', 'London', 'Berlin', 'Rome'],
        'correct': 'Paris'
    },
    {
        'question': 'What order is the sun in the Milky Way galaxy?',
        'answers': ['1', '2', '3', '4'],
        'correct': '1'
    }
]

compare = {
    0: "A",
    1: "B",
    2: "C",
    3: "D"
}

# Access the correct answer for the second question (index 1)
correct_answer = questions[1]['correct']

# Use the 'compare' dictionary to map it to 'A', 'B', 'C', or 'D'
print(compare[questions[1]['answers'].index(correct_answer)])
