import time
class Frame(object):
    def __init__(self, Frame):
        self.Frame = Frame

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
Scene = []
FrameRate = 24
Loop = True

# Constructing Scene
Scene.append(Frame(ROFLCopter1))
Scene.append(Frame(ROFLCopter2))

# Rendering Here
while True:
    for frame in Scene:
        time.sleep(1.0/FrameRate)
        print '\n'*50   # Clearing Frame Hack
        print frame.Frame
    # Loop Condition Check
    if not Loop:
        break
