'''
TextCaptchaBreaker. Created on Nov 11, 2010

@author: Sajid Anwar
'''

import re

colors = ['alizarin', 'almond', 'amaranth', 'amber', 'amber', 'amethyst', 'ao', 'ao', 'apricot', 'aqua', 'aquamarine', 'arsenic', 'asparagus', 'auburn', 'aureolin', 'aurometalsaurus', 'awesome', 'azure', 'azure', 'bazaar', 'beaver', 'beige', 'bistre', 'bittersweet', 'black', 'blond', 'blue', 'blue', 'blue', 'blush', 'bole', 'brass', 'bronze', 'brown', 'brown', 'bubbles', 'buff', 'burgundy', 'burlywood', 'byzantine', 'byzantium', 'cadet', 'camel', 'capri', 'cardinal', 'carmine', 'carnelian', 'ceil', 'celadon', 'cerise', 'cerulean', 'chamoisee', 'champagne', 'charcoal', 'chartreuse', 'chartreuse', 'chestnut', 'chocolate', 'cinereous', 'cinnabar', 'cinnamon', 'citrine', 'cobalt', 'copper', 'coquelicot', 'coral', 'cordovan', 'corn', 'cornsilk', 'cream', 'crimson', 'cyan', 'cyan', 'daffodil', 'dandelion', 'denim', 'desert', 'drab', 'ecru', 'eggplant', 'eggshell', 'emerald', 'fallow', 'fandango', 'fawn', 'feldgrau', 'firebrick', 'flame', 'flavescent', 'flax', 'folly', 'fuchsia', 'fulvous', 'gainsboro', 'gamboge', 'glaucous', 'gold', 'gold', 'goldenrod', 'gray', 'green', 'green', 'green', 'green', 'grullo', 'harlequin', 'heliotrope', 'honeydew', 'iceberg', 'icterine', 'inchworm', 'indigo', 'indigo', 'iris', 'isabelline', 'ivory', 'jade', 'jasper', 'jonquil', 'khaki', 'khaki', 'lava', 'lavender', 'lavender', 'lemon', 'lilac', 'lime', 'lime', 'linen', 'liver', 'lust', 'magenta', 'magenta', 'magenta', 'magnolia', 'mahogany', 'maize', 'malachite', 'manatee', 'maroon', 'maroon', 'mauve', 'mauvelous', 'melon', 'mint', 'moccasin', 'mulberry', 'mustard', 'myrtle', 'ochre', 'olive', 'olivine', 'onyx', 'orange', 'orange', 'orange', 'orchid', 'peach', 'pear', 'pearl', 'peridot', 'periwinkle', 'persimmon', 'pink', 'pistachio', 'platinum', 'plum', 'plum', 'prune', 'puce', 'pumpkin', 'purple', 'purple', 'raspberry', 'razzmatazz', 'red', 'red', 'red', 'redwood', 'regalia', 'rose', 'rosewood', 'ruby', 'ruddy', 'rufous', 'russet', 'rust', 'saffron', 'salmon', 'sand', 'sandstorm', 'sangria', 'sapphire', 'scarlet', 'seashell', 'sepia', 'shadow', 'sienna', 'silver', 'sinopia', 'skobeloff', 'smalt', 'snow', 'straw', 'sunglow', 'sunset', 'tan', 'tangelo', 'tangerine', 'taupe', 'teal', 'thistle', 'timberwolf', 'tomato', 'toolbox', 'tumbleweed', 'turquoise', 'ube', 'ultramarine', 'umber', 'urobilin', 'vanilla', 'verdigris', 'vermilion', 'veronica', 'violet', 'violet', 'violet', 'violet', 'viridian', 'wenge', 'wheat', 'white', 'wisteria', 'xanadu', 'yellow', 'yellow', 'yellow', 'zaffre']
ordinals =  {
                '1st': 1, 'first': 1,
                '2nd': 2, 'second': 2,
                '3rd': 3, 'third': 3,
                '4th': 4, 'fourth': 4,
                '5th': 5, 'fifth': 5,
                '6th': 6, 'sixth': 6,
                '7th': 7, 'seventh': 7,
                '8th': 8, 'eight': 8,
                '9th': 9, 'ninth': 9,
                '10th': 10, 'tenth': 10
            }

def solve(question):
    
    tokens = re.sub(r'[^\w\d\s]', '', question).lower().split(' ')
    found = []
    which = -1
    
    # Singular colour:
    #    'The pink church is what colour?' - pink
    #    'What is the 1st colour in the list coat, purple, yellow, black, pink and white?' - purple
    if 'colour' in tokens:
        
        for i in range(len(tokens)):
            
            # Go through each token and save those that are colors and those that are ordinal.
            if tokens[i] in colors:
                found.append(tokens[i])
            elif tokens[i] in ordinals:
                which = ordinals[tokens[i]]
                
        if len(found) == 1 or which == -1:
            return found[0]
        else:
            return found[which - 1]
        
    # Plural colours:
    #    'The list blue, brown, T-shirt, white and purple contains how many colours?' - four
    #    'Red, cheese and blue: how many colours in the list?' - two
    elif 'colours' in tokens:
        
        for i in range(len(tokens)):
            
            # Go through each token and save those that are colors.
            if tokens[i] in colors:
                found.append(tokens[i])
                
        return str(len(found))
    
    else:
        return None
