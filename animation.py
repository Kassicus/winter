import pygame

class StaticAnimation():
    def __init__(self, x, y, frame_count, delay, frames=[]):
        self.x = x
        self.y = y
        
        self.frame_count = frame_count
        self.delay = delay
        self.frames = frames

        self.active_frame_count = 0

        self.active_frame = self.frames[self.active_frame_count]

        self.anim_time = 0

        self.playing = False

    def play_animation(self):
        self.anim_time += 1

        if self.anim_time == self.delay:
            if self.active_frame_count < self.frame_count - 1:
                self.active_frame_count += 1
            else:
                self.active_frame_count = 0

            self.anim_time = 0

    def draw(self, surface):
        surface.blit(self.active_frame, (self.x, self.y))

    def update(self):
        self.active_frame = self.frames[self.active_frame_count]

        if self.playing:
            self.play_animation()