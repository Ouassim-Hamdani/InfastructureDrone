import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((50,50))
    
def getKey(keyName):
    for eve in pygame.event.get():
        pass
    keyInp = pygame.key.get_pressed()
    key_arg = getattr(pygame,"K_{}".format(keyName))
    if keyInp[key_arg]:
        pygame.display.update()
        return True
    
    pygame.display.update()
    return False

if __name__=="__main__":
    
    init()
    while True:
        print(getKey("a"))

