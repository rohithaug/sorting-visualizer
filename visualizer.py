import os, sys, time
import import_algorithms as algorithms

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame.locals import *
import pygame

# Pygame Initialisation
pygame.init()
screen = pygame.display.set_mode((1024, 512), HWSURFACE|DOUBLEBUF|RESIZABLE)
screen.fill((255, 255, 255))

#algorithm names to be displayed
algorithm_names = [["Selection", "Bubble", "Merge", "Quick"],
                   ["Comb", "Shell", "Heap", "Insertion"],
                   ["Bitonic", "Cocktail", "Cycle", "Tim"],
                   ["Gnome", "Stooge", "Radix", "Pancake"]]

def draw(size, pos):
    width = size[0]
    height = size[1]
    cols = rows = 4
    w = width/cols
    h = height/rows

    for row in range(rows+1):
        if row != 0:
            thickness = 3
            color = (0, 0, 0)
        else:
            thickness = 1
            color = (160, 160, 160)
        pygame.draw.lines(screen, color, False, [(row*w, 0), (row*w, height)], thickness)
        pygame.draw.lines(screen, color, False, [(0, row*h), (width, row*h)], thickness)

    font = pygame.font.SysFont("cambria", 40)
    for i, row in enumerate(range(rows)):
        for j, col in enumerate(range(cols)):
            x = col * (width/cols)
            y = row * (height/rows)
            text = font.render(algorithm_names[i][j], 1, (0, 0, 0))
            screen.blit(text, (x + (w/2 - text.get_width()/2), y + (h/2 - text.get_height()/2)))

    if pos != None:
        row = int(pos[1]/h)
        col = int(pos[0]/w)
        pygame.draw.rect(screen, (0, 255, 0), (col*w, row*h, w, h), 4)
        return(algorithm_names[row][col])

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type==VIDEORESIZE:
            screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
            pygame.display.flip()

def sleep_time(algorithm):
    if algorithm in ["Bubble Sort", "Cocktail Sort", "Gnome Sort", "Stooge Sort"]:
        return 0
    if algorithm in ["Comb Sort", "Radix Sort", "Shell Sort", "Tim Sort"]:
        return 0.05
    if algorithm in ["Bitonic Sort", "Heap Sort", "Merge Sort", "Quick Sort"]:
        return 0.03
    if algorithm in ["Cycle Sort", "Insertion Sort", "Selection Sort", "Pancake Sort"]:
        return 0.1

def update_screen(algorithm, swap_index_1=None, swap_index_2=None, pivot=None, screen=screen):
    screen.fill((255, 255, 255))
    pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Status: Sorting     Delay: {} ms".format(algorithm.name, int(1000*sleep_time(algorithm.name))))
    width, height = pygame.display.get_surface().get_size()
    length = len(algorithm.array)
    size = (width//length)//4
    for i in range(4*length):
        if i%4 != 0:
            colour = (66, 134, 244, 0.8)
            if pivot == i//4:
                colour = (169, 92, 232, 0.8)
            if swap_index_1 == i//4:
                colour = (0, 255, 0, 0.8)
            elif swap_index_2 == i//4:
                colour = (255, 0, 0, 0.8)
            pygame.draw.rect(screen, colour, (i*size, height, size, -algorithm.array[i//4]))
        else:
            colour = (255, 255, 255)
            pygame.draw.rect(screen, colour, (i*size, height, size, 0))
    events()
    pygame.display.update()
    time.sleep(sleep_time(algorithm.name))

def fixed_update_screen(algorithm, status, screen=screen):
    screen.fill((255, 255, 255))
    if status == "Start":
        pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Status: Generated Random Unsorted Array".format(algorithm.name))
    elif status == "End":
        pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Status: Array Sorted".format(algorithm.name))
    width, height = pygame.display.get_surface().get_size()
    length = len(algorithm.array)
    size = (width//length)//4
    for i in range(4*length):
        if i%4 != 0:
            colour = (66, 134, 244, 0.8)
            pygame.draw.rect(screen, colour, (i*size, height, size, -algorithm.array[i//4]))
        else:
            colour = (255, 255, 255)
            pygame.draw.rect(screen, colour, (i*size, height, size, 0))
    events()
    pygame.display.update()

def main():
    while True:
        pos = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type==VIDEORESIZE:
                screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
                pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                algorithm_name = draw(pygame.display.get_surface().get_size(), pos)

        if pos != None and algorithm_name != None:
            pygame.display.update()
            time.sleep(1.5)

            #here array length is set to the width of the screen
            array_length = pygame.display.get_surface().get_size()[1]
            algorithm = algorithms.algorithms[algorithm_name]
            algorithm.start(array_length)

            while True:
                events()
                pygame.display.update()
                break

        screen.fill((255, 255, 255))
        pygame.display.set_caption("Sorting Visualizer          Select an Algorithm:")
        draw(pygame.display.get_surface().get_size(), pos)
        pygame.display.update()

if __name__=='__main__':
    main()
    pygame.quit()
    sys.exit()
