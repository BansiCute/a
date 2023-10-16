import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Questions and Answers
questions = [
    {
        'question': 'What is the capital of France?',
        'answers': ['Paris', 'London', 'Berlin', 'Rome'],
        'correct': 'Paris'
    },
    {
        'question': 'What order is the sun in the Milky Way galaxy?',
        'answers': ['1', '2', '3', '4'],
        'correct': '2'
    }
]
compare = {
    0: "A",
    1: "B",
    2: "C",
    3: "D"
}
correct_answer = questions[1]['correct']

# Choose a random question
current_question = random.choice(questions)

# Screen dimensions
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 683

# Create a Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Quiz Game')

# Answer positions
answer_positions = {
    'A': (642, 528),
    'B': (830, 529),
    'C': (637, 609),
    'D': (829, 607),
}

# Pity level and background images
pity = 0
background_images = {
    0: 'backgroundcauhoi0.png',
    1: 'backgroundcauhoi50.png',
    2: 'backgroundcauhoi100.png',
}
background_image = pygame.image.load(background_images[pity])
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
background_rect = background_image.get_rect()

# Load the "wrong.png" image and scale it
wrong_image = pygame.image.load('wrong.png')
wrong_image = pygame.transform.scale(wrong_image, (100, 100))
wrong_rect = wrong_image.get_rect()
wrong_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Load the "correct.png" image and scale it
correct_image = pygame.image.load('correct.png')
correct_image = pygame.transform.scale(correct_image, (100, 100))
correct_rect = correct_image.get_rect()
correct_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Set the question text position and dimensions
question_rect = pygame.Rect(24, 520, 568, 139)

# Text for the "Start Game" message
start_game_text = font.render('Start Game', True, BLACK)
start_game_rect = start_game_text.get_rect()
start_game_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Main loop for the Start Game screen
start_game = True
while start_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_game = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the player clicked on the "Start Game" message
            if start_game_rect.collidepoint(event.pos):
                start_game = False  # Exit the start game loop to begin the quiz

    # Load the start screen background image
    start_background_image = pygame.image.load('background_start.png')
    start_background_image = pygame.transform.scale(start_background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(start_background_image, start_background_image.get_rect())

    # Draw the "Start Game" message
    screen.blit(start_game_text, start_game_rect)
    pygame.display.flip()

# Actual Quiz Game Loop
running = True
show_wrong = False
show_correct = False
feedback_start_time = 0
feedback_duration = 2000  # Feedback display duration in milliseconds

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check which answer the player has selected
            for answer, position in answer_positions.items():
                if (
                    position[0] <= event.pos[0] <= position[0] + 50 and
                    position[1] <= event.pos[1] <= position[1] + 50
                ):
                    selected_answer = answer

    # Update the background image based on pity
    background_image = pygame.image.load(background_images[pity])
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Handle showing the feedback images
    current_time = pygame.time.get_ticks()
    if show_correct and current_time - feedback_start_time < feedback_duration:
        screen.blit(correct_image, correct_rect)
    elif show_wrong and current_time - feedback_start_time < feedback_duration:
        screen.blit(wrong_image, wrong_rect)
    else:
        show_correct = False
        show_wrong = False
        # Continue to display the background image

    # Check if a selected answer is correct
    if 'selected_answer' in locals() and selected_answer is not None:
        if selected_answer == compare[questions.index(current_question)]:
            print("Correct answer!")
            show_correct = True
            pity += 1
            pity = min(pity, max(background_images.keys()))
        else:
            print("Wrong answer!")
            show_wrong = True
            pity += 1
            pity = min(pity, max(background_images.keys()))
        feedback_start_time = pygame.time.get_ticks()
        selected_answer = None

        # Select a new random question
        current_question = random.choice(questions)



    # Display the background image when there is no feedback
    if not show_correct and not show_wrong:
        screen.blit(background_image, background_rect)

    # Draw the question (with text wrapping)
    question_text = current_question['question']
    question_lines = []
    words = question_text.split()
    current_line = ''
    for word in words:
        test_line = current_line + word + ' '
        test_surface = font.render(test_line, True, BLACK)
        if test_surface.get_width() <= question_rect.width:
            current_line = test_line
        else:
            question_lines.append(current_line)
            current_line = word + ' '
    question_lines.append(current_line)

    y = question_rect.top
    for line in question_lines:
        line_surface = font.render(line, True, BLACK)
        screen.blit(line_surface, (question_rect.left, y))
        y += line_surface.get_height()

    # Draw answers A, B, C, D
    for answer, position in answer_positions.items():
        answer_surface = font.render(f'{answer}. {current_question["answers"][ord(answer) - ord("A")]}', True, BLACK)
        screen.blit(answer_surface, (position[0], position[1]))

    pygame.display.flip()

# Close the Pygame window
pygame.quit()
sys.exit()