import pygame
import math
import settings

class Robot:
    def __init__(self, start_x, start_y):
        self.true_x = start_x
        self.true_y = start_y
        self.heading = 0 # Degrees. 0 is Right, 90 is Up (inverted Y), etc.
        
        # The "Estimated" position is what the robot THINKS it is.
        # We start knowing where we are.
        self.est_x = start_x
        self.est_y = start_y

    def move(self, keys):
        # Rotate
        if keys[pygame.K_LEFT]:
            self.heading += settings.ROTATION_SPEED
        if keys[pygame.K_RIGHT]:
            self.heading -= settings.ROTATION_SPEED

        # Move Forward/Backward
        # Convert heading to radians
        rad = math.radians(self.heading)
        
        if keys[pygame.K_UP]:
            self.true_x += settings.ROBOT_SPEED * math.cos(rad)
            self.true_y += settings.ROBOT_SPEED * math.sin(rad) # Y increases going UP (Cartesian)
        if keys[pygame.K_DOWN]:
            self.true_x -= settings.ROBOT_SPEED * math.cos(rad)
            self.true_y -= settings.ROBOT_SPEED * math.sin(rad)

    def scan_for_tags(self, known_tags):
        """
        Simulates a camera. Returns a list of tags the robot can 'see'.
        Returns: List of dicts {id, distance, angle}
        """
        visible_tags = []
        
        for tag_id, (tx, ty) in known_tags.items():
            # Calculate distance to tag
            dx = tx - self.true_x
            dy = ty - self.true_y # Standard Cartesian logic
            
            # Euclidean distance
            dist = math.sqrt(dx*dx + dy*dy)
            
            if dist <= settings.MAX_DETECTION_DISTANCE:
                # Calculate angle to tag
                # atan2 returns angle in radians between -pi and pi
                angle_to_tag_rad = math.atan2(dy, dx) # Standard atan2
                angle_to_tag_deg = math.degrees(angle_to_tag_rad)
                
                # Relative angle (Where is the tag relative to the robot's nose?)
                relative_angle = angle_to_tag_deg - self.heading
                
                # Normalize angle to -180 to 180
                while relative_angle > 180: relative_angle -= 360
                while relative_angle < -180: relative_angle += 360
                
                # Check if within Field of View
                if abs(relative_angle) < (settings.FOV / 2):
                    visible_tags.append({
                        "id": tag_id,
                        "distance": dist,
                        "angle": relative_angle,
                        "tx": tx,
                        "ty": ty
                    })
                    
        return visible_tags

    def draw(self, screen):
        # Draw the "True" Robot (Green)
        # Convert Cartesian Y to Screen Y (Screen Y = Height - Cartesian Y)
        screen_y = settings.SCREEN_HEIGHT - self.true_y
        
        robot_rect = pygame.Rect(0, 0, settings.ROBOT_SIZE, settings.ROBOT_SIZE)
        robot_rect.center = (int(self.true_x), int(screen_y))
        pygame.draw.rect(screen, settings.GREEN, robot_rect)
        
        # Draw Heading Line
        rad = math.radians(self.heading)
        end_x = self.true_x + 30 * math.cos(rad)
        end_y = self.true_y + 30 * math.sin(rad) # Cartesian end point
        
        screen_end_y = settings.SCREEN_HEIGHT - end_y
        pygame.draw.line(screen, settings.BLACK, (self.true_x, screen_y), (end_x, screen_end_y), 3)

        # Draw the "Estimated" Position (Blue Ghost)
        # This shows the students if their math is working!
        est_screen_y = settings.SCREEN_HEIGHT - self.est_y
        est_rect = pygame.Rect(0, 0, 20, 20)
        est_rect.center = (int(self.est_x), int(est_screen_y))
        pygame.draw.rect(screen, settings.BLUE, est_rect, 2)