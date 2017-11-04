# Created by : Sidney Kang
# Created on : 11 Oct. 2017
# Created for : ICS3UR
# Wednesday Assignment - wed_08
# This scene displays the main menu scene

from scene import * 
import ui

from main_game_scene import *
from help_scene import *

class MainMenuScene(Scene):
      def setup(self):
          #Add Mt blue background colour
          self.background = SpriteNode(position = self.size/2, 
                                       color = (0.61, 0.78, 0.87), 
                                       parent = self,
                                       size = self.size)
          self.start_button = SpriteNode('./assets/sprites/start_button.PNG',
                                         parent = self,
                                         position = self.size/2)

          help_button_position = self.size/2
          help_button_position.y = help_button_position.y - 200                                
          self.help_button = SpriteNode('./assets/sprites/help_button.PNG',
                                        parent = self,
                                        position = help_button_position)
                                          

      def update(self):
        # this method is called, hopefully, 60 times a second
          pass
    
      def touch_began(self, touch):
        # this method is called, when user touches the screen
          pass

      def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
          pass

      def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
          pass
        
          # If start button is pressed, go to MainGameScene
          if self.start_button.frame.contains_point(touch.location):
             self.present_modal_scene(MainGameScene())

          # If help button is pressed, go to HelpScene
          if self.help_button.frame.contains_point(touch.location):
             self.present_modal_scene(HelpScene())

      def did_change_size(self):
          # this method is called, when user changes the orientation of the screen
          # thus changing the size of each dimension
          pass

      def pause(self):
          # this method is called, when user touches the home button
          # save anything before app is put to background
        pass

      def resume(self):
          # this method is called, when user place app from background 
          # back into use. Reload anything you might need.
          pass
