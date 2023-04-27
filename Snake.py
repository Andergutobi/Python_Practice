import pygame
import random
import sys

#_________Configuracion pantalla

screen_width = 640
screen_height = 480
cell_size = 20
grid_width = screen_width // cell_size
grid_height = screen_height // cell_size

#_________Colores

bg_color = (0, 128, 0)
snake_color = (139, 69, 19)
apple_color = (255, 0, 0)
text_color = (255, 255, 255)

#________Direcciones serpiente

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

#________SERPIENTE
class Snake:
    def __init__(self):
        self.body = [(grid_width//2, grid_height//2)]
        self.direction = random.choice([up, down, right, left])
        self.grow = False
        
    def update(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        
    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, snake_color, (segment[0] * cell_size, segment[1] * cell_size, cell_size, cell_size))
            
    def check_collision(self):
        head = self.body[0]
        if head[0] < 0 or head[0] >= grid_width or head[1] < 0 or head[1] >= grid_height:
            return True
        for segment in self.body[1:]:
            if segment == head:
                return True
        return False
    
    def change_direction(self, direction):
        if (direction[0], direction[1]) != (-self.direction[0],-self.direction[1]):
            self.direction = direction
            
    def grow_snake(self):
        self.grow = True
        
#________MANZANA
        
class Apple:    
    
    def __init__(self):
        self.position = (random.randint(0, grid_width - 1), random.randint(0, grid_height -1))
        
    def draw(self, screen):
         pygame.draw.rect(screen, apple_color, (self.position[0] * cell_size, self.position[1] * cell_size, cell_size, cell_size))
         
def game_over(screen):
    font = pygame.font.SysFont(None, 40)
    text = font.render('Game Over', True, text_color)
    text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
    button_rect = pygame.Rect(screen_width/2 - 50, screen_height/2 + 50, 100, 50)
    pygame.draw.rect(screen, text_color, button_rect)
    font = pygame.font.SysFont(None, 30)
    text_button = font.render('Play again', True, (0,0,0))
    text_button_rect = text_button.get_rect(center=(screen_width/2, screen_height/2 + 75))
    screen.blit(text, text_rect)
    screen.blit(text_button, text_button_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    return True
                    
        pygame.display.update()
        
# Funcion principal del juego
def main():
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('snake')
    clock = pygame.time.Clock()
    snake = Snake()
    apple = Apple()
    
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(up)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(down)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(left)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(right)
                
        snake.update()

        if snake.check_collision():
            game_running = game_over(screen)
            if game_running:
                snake = Snake()
                apple = Apple()
        else:
            screen.fill(bg_color)

            apple.draw(screen)

            snake.draw(screen)

            pygame.display.update()

            clock.tick(10)

            if snake.body[0] == apple.position:
                apple = Apple()
                snake.grow_snake()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
