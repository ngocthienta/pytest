import pygame
pygame.init()
notes = ['a','b','c','d','e','f','g']
octaves = ['2','3','4','5']
conv = {'c#':'db','d#':'eb','f#':'gb','g#':'ab','a#':'bb'}
gay = (
    'C4', 'C4', 'D4', 'C4', 'F4', 'E4',
    'C4', 'C4', 'D4', 'C4', 'G4', 'F4',
    'C4', 'C4', 'C5', 'A4', 'F4', 'E4', 'D4',
    'A#4', 'A#4', 'A4', 'F4', 'G4', 'F4', 'GbA4'
)

print(type(gay))

def play_melody(melody, sound_basedir):
    if (not isinstance(melody,list) and not isinstance(melody,tuple)) or not melody:
        raise TypeError
    for i in melody:
        if not isinstance(i,str):
            raise TypeError
    new_mel = []
    for i in melody:
        new_mel.append(i.lower())
    for i in range(len(new_mel)):
        if not len(new_mel[i]) < 2 or len(new_mel[i]) > 3:
            raise ValueError
        if not new_mel[i][0] in notes or not new_mel[i][-1] in octaves:
            raise ValueError
        for j in ['e#','b#','cb','fb']:
            if j in new_mel[i]:
                raise ValueError
        if new_mel[i][0:2] in conv:
            print(new_mel[i][0:2])
            new_mel[i] = new_mel[i].replace(new_mel[i][0:2],conv[new_mel[i][0:2]])
    lst = []
    for i in new_mel:
        lst.append('{}/{}.ogg'.format(sound_basedir,i))
        sound = pygame.mixer.Sound('{}/{}.ogg'.format(sound_basedir,i))
        sound.play()
        pygame.time.delay(300)
        pygame.mixer.stop()
    return lst
print(play_melody(gay, './sounds/piano'))
