import time
class Frame(object):
    def __init__(self, Frame):
        self.Frame = Frame

class Engine(object):
    def __init__(self):
        # Default Frame Rate is 24 fps
        self.FrameRate = 24
        self.Scene = []
        self.Loop = True
    
    def AddFrame(self, frame):
        """For Adding a Frame to the Scene"""
        self.Scene.append(frame)

    def RenderFrame(self, frame):
        """A Crude Frame Renderer"""
        print frame.Frame

    def Render(self):
        """Render Function to be called by main"""
        while True:
            for frame in self.Scene:
                time.sleep(1.0/self.FrameRate)
                print '\n'*50   # Clearing Frame Hack
                self.RenderFrame(frame)
            if not self.Loop:
                break

engine = Engine()
ROFLCopter1 = '''
          ROFL:ROFL:LOL:
                    _^___
           L    __/   [] \    
           O ===__        \ 
           L      \________]
                    I   I
                   --------/'''
ROFLCopter2 = '''
                   :LOL:ROFL:ROFL
                    _^___
                __/   [] \    
          LOL===__        \ 
                  \________]
                    I   I
                   --------/'''
engine.AddFrame(Frame(ROFLCopter1))
engine.AddFrame(Frame(ROFLCopter2))
engine.Render()
