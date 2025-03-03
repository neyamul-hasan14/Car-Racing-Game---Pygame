import pygame
import random

pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 711
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
class Score:
    def __init__(self):
        self.score = 0
    def get_score(self):
        return self.score
    def set_score(self, score):
        self.score = score;

class Player:
    def __init__(self):
        self.width = 40
        self.height = 70
        self.x = WINDOW_WIDTH // 2 - self.width // 2
        self.y = WINDOW_HEIGHT - 150
        self.speed = 5
        
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        # Main body
        pygame.draw.rect(self.surface, RED, (0, 10, self.width, self.height-20))
        # Front windshield
        pygame.draw.polygon(self.surface, BLACK, [(5, 20), (35, 20), (30, 35), (10, 35)])
        # Wheels
        pygame.draw.rect(self.surface, BLACK, (0, 0, 10, 15))
        pygame.draw.rect(self.surface, BLACK, (30, 0, 10, 15))
        pygame.draw.rect(self.surface, BLACK, (0, self.height-15, 10, 15))
        pygame.draw.rect(self.surface, BLACK, (30, self.height-15, 10, 15))
    
    
    def move(self, keys):
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed
        
        # Keep player on screen
        self.x = max(0, min(self.x, WINDOW_WIDTH - self.width))
        self.y = max(0, min(self.y, WINDOW_HEIGHT - self.height))
    
    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

class Obstacle:
    def __init__(self):
        self.width = 40
        self.height = 70
        self.speed = random.uniform(3, 6)  # Initialize speed here
        
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        # Main body
        pygame.draw.rect(self.surface, BLUE, (0, 10, self.width, self.height-20))
        # Front windshield
        pygame.draw.polygon(self.surface, BLACK, [(10, 35), (30, 35), (35, 50), (5, 50)])
        # Wheels
        pygame.draw.rect(self.surface, BLACK, (0, 0, 10, 15))
        pygame.draw.rect(self.surface, BLACK, (30, 0, 10, 15))
        pygame.draw.rect(self.surface, BLACK, (0, self.height-10, 10, 15))
        pygame.draw.rect(self.surface, BLACK, (30, self.height-10, 10, 15))
        
    
        self.x = 0
        self.y = 0
        
    def check_collision_with_obstacles(self, obstacles):
        my_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        margin = 20
        my_rect.inflate_ip(margin, margin)
        
        for obstacle in obstacles:
            if obstacle != self:
                other_rect = pygame.Rect(obstacle.x, obstacle.y, 
                                       obstacle.width, obstacle.height)
                if my_rect.colliderect(other_rect):
                    return True
        return False

    def reset(self, all_obstacles, game_score):
        max_attempts = 100
        attempt = 0
        
        while attempt < max_attempts:
            self.x = random.randint(0, WINDOW_WIDTH - self.width)
            self.y = -self.height - random.randint(0, 200)  
            self.speed = random.uniform(3+game_score.get_score()/300, 6+game_score.get_score()/300)  # Increase speed with score
            
            if not self.check_collision_with_obstacles(all_obstacles):
                break
            attempt += 1
            
            if attempt == max_attempts:
                self.y = min([o.y for o in all_obstacles]) - self.height - 100
    
    def move(self, all_obstacles, game_score):
        old_y = self.y
        self.y += self.speed
        
        # Check for collisions after movement
        if self.check_collision_with_obstacles(all_obstacles):
            self.y = old_y 
            self.speed = min([o.speed for o in all_obstacles if o.y < self.y], default=self.speed)
        
        if self.y > WINDOW_HEIGHT:
            self.reset(all_obstacles, game_score)
            return True
        return False
    
    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Racing Game")
    clock = pygame.time.Clock()
    
    player = Player()
    obstacles = []
    game_score = Score()
    score = 0
    game_score.set_score(score)
    
    for _ in range(4):
        new_obstacle = Obstacle()
        new_obstacle.reset(obstacles, game_score)  # Initialize position properly
        obstacles.append(new_obstacle)
        
    score = 0;
    game_score.set_score(score)
    
    game_over = False
    font = pygame.font.Font(None, 36)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_SPACE:
                    player = Player()
                    obstacles = []
                    for _ in range(4):
                        new_obstacle = Obstacle()
                        new_obstacle.reset(obstacles, game_score)
                        obstacles.append(new_obstacle)
                    score = 0
                    game_score.set_score(score)
                    game_over = False
                elif event.key == pygame.K_ESCAPE:
                    running = False
        
        if not game_over:
            keys = pygame.key.get_pressed()
            player.move(keys)
            
            # Update obstacles
            for obstacle in obstacles:
                if obstacle.move(obstacles, game_score):
                    score += 10
                    game_score.set_score(score)
                    obstacle.reset(obstacles, game_score)
            
            # Check collisions
            for obstacle in obstacles:
                if (player.x < obstacle.x + obstacle.width and
                    player.x + player.width > obstacle.x and
                    player.y < obstacle.y + obstacle.height and
                    player.y + player.height > obstacle.y):
                    game_over = True
        
        # Draw everything
        screen.fill(GRAY)
        
        # Draw road markings
        for i in range(0, WINDOW_HEIGHT, 50):
            pygame.draw.rect(screen, WHITE, (WINDOW_WIDTH//2 - 5, i, 10, 30))
        
        # Draw game objects
        for obstacle in obstacles:
            obstacle.draw(screen)
        player.draw(screen)
        
        # Draw score
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))
        
        if game_over:
            game_over_text = font.render('Game Over!', True, WHITE)
            restart_text = font.render('Press SPACE to restart', True, WHITE)
            quit_text = font.render('Press ESC to quit', True, WHITE)
            screen.blit(game_over_text, 
                      (WINDOW_WIDTH//2 - game_over_text.get_width()//2,
                       WINDOW_HEIGHT//2 - game_over_text.get_height()))
            screen.blit(restart_text,
                      (WINDOW_WIDTH//2 - restart_text.get_width()//2,
                       WINDOW_HEIGHT//2 + restart_text.get_height()))
            screen.blit(quit_text,
                      (WINDOW_WIDTH//2 - quit_text.get_width()//2,
                       WINDOW_HEIGHT//2 + 3*quit_text.get_height()))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()