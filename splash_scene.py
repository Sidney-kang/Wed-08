# Created by : Sidney Kang
# Created on : 11 Oct. 2017
# Created for : ICS3UR
# Wednesday Assignment - wed_08
# This scene shows a splash screen for 2 seconds, then transition to the main menu

from scene import *
import ui
import time

from main_menu_scene import *

start_time = time.time()
#Create timer so that after 2 seconds it moves to next scene

class SplashScene(Scene):
      def setup(self):
      #This method is called, when user moves to this scene

      #Add Mt blue background colour
          self.background = SpriteNode(position = self.size/2, 
                                       color = (0.61, 0.78, 0.87), 
                                       parent = self, 
                                       size = self.size)
          self.school_crest = SpriteNode('./assets/sprites/MT_Crest.jpg', 
                                         parent = self, 
                                         position = self.size/2)

      def update(self): 
      #This function called every 60 seconds
     
      #After 2 seconds, move to main menu scene
          if not self.presented_scene and time.time() - start_time > 2:
             self.present_modal_scene(MainMenuScene())
             
     

      def touch_began(self, touch):
      #This method is called when user touches the screen 
          pass
