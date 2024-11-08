import pygame
import sys

# Pygame �ʱ�ȭ
pygame.init()

# ȭ�� ũ�� ����
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 780
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# ��� �̹��� �ε� �� ũ�� ����
background = pygame.image.load("background.jpg")
background = pygame.transform.smoothscale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# �����̴� ����
class Slider(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, width, height):
        super().__init__()
        self.original_image = pygame.image.load(image_path)  # �����̴� �̹��� �ε�
        self.image = pygame.transform.scale(self.original_image, (width, height))  # �̹��� ũ�� ����
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # �����̴� �ʱ� ��ġ ����
        self.dragging = False

    def update(self):
        if self.dragging:
            self.rect.centery = pygame.mouse.get_pos()[1]
            # Y ��ǥ�� ȭ�� ������ ����� �ʵ��� ����
            self.rect.centery = max(self.min_y, min(self.max_y, self.rect.centery))

# ��� �����̴��� ���� �׷�
slider_group = pygame.sprite.Group()

# �����̴� ����
num_sliders = 40
slider_spacing = 56

# �����̴� �׷� ����
group1_sliders = []
group2_sliders = []

for i in range(1, num_sliders + 1):
    if i <= num_sliders // 2:
        y = SCREEN_HEIGHT // 2 - 50
        group = group1_sliders
    else:
        y = SCREEN_HEIGHT - 50
        group = group2_sliders
    
    if i<=num_sliders//2:
        if(i <= 10):
            slider = Slider(i * slider_spacing, y, "slider.png", 50, 100)
    
        else:
            slider = Slider((i+1) * slider_spacing - 20, y, "slider.png", 50, 100)
    else:
        if(i <= 30):
            slider = Slider((i-20) * slider_spacing, y, "slider.png", 50, 100)
    
        else:
            slider = Slider((i-19) * slider_spacing - 20, y, "slider.png", 50, 100)

    group.append(slider)
    slider_group.add(slider)

# �׷� ���� y�� ���� ���� ����
for slider in group1_sliders:
    slider.min_y = 80
    slider.max_y = SCREEN_HEIGHT // 2 - 50

for slider in group2_sliders:
    slider.min_y = SCREEN_HEIGHT // 2 + 80
    slider.max_y = SCREEN_HEIGHT - 50

# ���� ����
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # ���콺 Ŭ�� �� �����̴��� �巡���� �� �ֵ��� ����
            for slider in slider_group:
                if slider.rect.collidepoint(event.pos):
                    slider.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # ���콺 ��ư ���� �����̴� �巡�� ����
            for slider in slider_group:
                slider.dragging = False

    # ȭ�� �׸���
    screen.blit(background, (0, 0))
    slider_group.update()
    slider_group.draw(screen)
    pygame.display.flip()

# Pygame ����
pygame.quit()
sys.exit()
