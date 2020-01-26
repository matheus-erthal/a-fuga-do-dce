import sys
import time
import pygame
from . import window
from . import animation
from pygame.locals import *

import tiledtmxloader

pygame.init()

class TileMap():

    def __init__(self,filename):
        self.x_pixels = 0
        self.y_pixels = 0
        self.cam_world_pos_x = 0
        self.cam_world_pos_y = 0

        self.world_map = {}
        self.resources = {}
        self.renderer = {}
        self.sprite_layers = {}

    def load(filename):
        world_map = tiledtmxloader.tmxreader.TileMapParser().parse_decode(file_name)
        # let see how many pixels it will use
        x_pixels = world_map.pixel_width
        y_pixels = world_map.pixel_height
        resources = tiledtmxloader.helperspygame.ResourceLoaderPygame()
        resources.load(world_map)
        renderer = tiledtmxloader.helperspygame.RendererPygame()
        sprite_layers = tiledtmxloader.helperspygame.get_layers_from_map(resources)

    def render(window,self):
        # render the map
        for sprite_layer in self.sprite_layers:
            if sprite_layer.is_object_group:
                # we dont draw the object group layers
                # you should filter them out if not needed
                continue
            else:
                self.renderer.render_layer(window.screen, sprite_layer)

        pygame.display.flip()


    def setCameraPosition(self,cam_world_pos_x,cam_world_pos_y):
        self.renderer.set_camera_position(cam_world_pos_x, \
                             cam_world_pos_y, "topleft")

    def getNumLayers(self):
        return len(self.world_map.layers)

    def getNumTiles(self):
        return self.world_map.width, self.world_map.height


