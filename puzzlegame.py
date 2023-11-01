import pygame
import sys
import random
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 400))

# Create a blank image with a white background
image = pygame.Surface((400, 400))
image.fill((255, 255, 255))

# Define the difficulty levels (number of puzzle pieces)
difficulty_levels = [4, 9, 16, 25]
current_level = 0
total_pieces = difficulty_levels[current_level]

# Function to split the image into pieces
def split_image(image, rows, columns):
    width, height = image.get_size()
    piece_width = width // columns
    piece_height = height // rows
    piece_list = []
    for y in range(rows):
        for x in range(columns):
            rect = pygame.Rect(x * piece_width, y * piece_height, piece_width, piece_height)
            piece = image.subsurface(rect)
            piece_list.append(piece)
    return piece_list

# Function to shuffle the pieces
def shuffle_pieces(piece_list):
    random.shuffle(piece_list)

# Function to draw the pieces on the screen
def draw_pieces(piece_list):
    piece_width, piece_height = piece_list[0].get_size()
    for i, piece in enumerate(piece_list):
        x = i % int(total_pieces ** 0.5) * piece_width
        y = i // int(total_pieces ** 0.5) * piece_height
        screen.blit(piece, (x, y))

# Split the image into pieces
pieces = split_image(image, int(total_pieces ** 0.5), int(total_pieces ** 0.5))
shuffle_pieces(pieces)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current_level = min(current_level + 1, len(difficulty_levels) - 1)
                total_pieces = difficulty_levels[current_level]
                pieces = split_image(image, int(total_pieces ** 0.5), int(total_pieces ** 0.5))
                shuffle_pieces(pieces)
    
    screen.fill((0, 0, 0))
    draw_pieces(pieces)
    pygame.display.update()
