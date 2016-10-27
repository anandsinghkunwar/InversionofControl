import time
class Frame(object):
    def __init__(self, Frame):
        self.Frame = Frame
def main():
    ROFLCopter1 = open('roflcopter1', 'r').read()
    ROFLCopter2 = open('roflcopter2', 'r').read()
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

if __name__ == '__main__':
    main()
