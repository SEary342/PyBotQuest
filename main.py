import pygame
import sys
import settings
import Field
from robot_sim import Robot
from localization import calculate_position_from_tag

def main():
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("7th Grade Robotics: Maze Localization")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 18)

    # Create Robot in the center
    robot = Robot(settings.SCREEN_WIDTH // 4, settings.SCREEN_HEIGHT // 2)

    running = True
    while running:
        # 1. Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        robot.move(keys)

        # 2. Simulation Logic (The "Camera")
        # Get data about tags we can see
        visible_tags = robot.scan_for_tags(Field.KNOWN_TAGS)

        # 3. Student Logic (Localization)
        # If we see tags, let's try to calculate where we are!
        if visible_tags:
            # For simplicity, we just take the first tag we see to calculate position.
            # In advanced robotics, we would average all of them.
            target = visible_tags[0]
            
            # CALL THE STUDENT'S FUNCTION
            new_x, new_y = calculate_position_from_tag(
                robot.heading,
                target['tx'],
                target['ty'],
                target['distance'],
                target['angle']
            )
            
            # Update robot's estimated position
            robot.est_x = new_x
            robot.est_y = new_y
            
            debug_text = f"Seeing Tag {target['id']} | Dist: {int(target['distance'])}"
        else:
            debug_text = "No Tags Visible - Position Unknown"

        # 4. Drawing
        mid_x = settings.SCREEN_WIDTH // 2
        # Left half (Blue Alliance)
        pygame.draw.rect(screen, settings.LIGHT_BLUE, (0, 0, mid_x, settings.SCREEN_HEIGHT))
        # Right half (Red Alliance)
        pygame.draw.rect(screen, settings.LIGHT_RED, (mid_x, 0, mid_x, settings.SCREEN_HEIGHT))

        # Draw Field Boundary
        pygame.draw.rect(screen, settings.BLACK, (0, 0, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), 5)

        # Center Line
        pygame.draw.line(screen, settings.BLACK, (mid_x, 0), (mid_x, settings.SCREEN_HEIGHT), 4)

        # Mid-Alliance Lines
        pygame.draw.line(screen, settings.BLACK, (mid_x // 2, 0), (mid_x // 2, settings.SCREEN_HEIGHT), 2)
        pygame.draw.line(screen, settings.BLACK, (mid_x + mid_x // 2, 0), (mid_x + mid_x // 2, settings.SCREEN_HEIGHT), 2)

        # Draw Tags (The Maze Landmarks)
        for tag_id, (x, y) in Field.KNOWN_TAGS.items():
            # Draw Tag Square
            tag_color = Field.TAG_SPECIFIC_COLORS.get(tag_id, Field.DEFAULT_TAG_COLOR)
            screen_y = settings.SCREEN_HEIGHT - y
            rect = pygame.Rect(x - 15, screen_y - 15, 30, 30)
            pygame.draw.rect(screen, tag_color, rect)
            # Draw Tag ID
            text = font.render(str(tag_id), True, settings.WHITE)
            screen.blit(text, (x - 5, screen_y - 10))

        # Draw Robot
        robot.draw(screen)
        
        # Draw Vision Lines (Visual feedback)
        for tag in visible_tags:
            pygame.draw.line(screen, settings.GRAY, 
                             (robot.true_x, settings.SCREEN_HEIGHT - robot.true_y), 
                             (tag['tx'], settings.SCREEN_HEIGHT - tag['ty']), 1)

        # Draw UI
        info = font.render(debug_text, True, settings.BLACK)
        screen.blit(info, (10, 10))
        
        pos_text = f"({int(robot.true_x)}, {int(robot.true_y)})"
        pos_info = font.render(pos_text, True, settings.BLACK)
        screen.blit(pos_info, (10, 35))
        
        instr = font.render("Use Arrow Keys to Move. Blue Circle = Calculated Position", True, settings.BLUE)
        screen.blit(instr, (10, settings.SCREEN_HEIGHT - 30))

        pygame.display.flip()
        clock.tick(settings.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
