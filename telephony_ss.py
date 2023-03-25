# signalling schemas copied from BetterBlueBox (developed Filip Miscevic)

mf = {1: [700, 900], 2: [700, 1100], 3: [900, 1100], 4: [700, 1300], 5: [900, 1300], 6: [1100, 1300],
          7: [700, 1500], 8: [900, 1500], 9: [1100, 1500], '*': [1100, 1700], 0: [1300, 1500], '-': [1500, 1700],
          '+': [2600]};

dtmf = {1: [697, 1209], 2: [697, 1336], 3: [697, 1477], 4: [770, 1209], 5:
    [770, 1336], 6: [770, 1477], 7: [852, 1209], 8: [852, 1336], 9: [852, 1477],
        '*': [941, 1209], 0: [941, 1336], '-': [941, 1477],
        'B1': {'frequencies': [2400, 2600], 'mark': 150, 'space': 100},
        'B2': {'frequencies': [2400], 'mark': 100, 'space': 100},
        '+': {'sequence': ['B1', 'B2']}, 'A': [697, 1633], 'B': [770, 1633], 'C': [852, 1633], 'D': [941, 1633]};

redbox = {"\'": {'frequencies': [1700, 2200], 'extra-text': '5c', 'mark': 66, 'space': 66},
          "\`": {'frequencies': [1700, 2200], 'mark': 33, 'space': 33},
          1: {'sequence': "\'", 'extra-text': '5c', 'space': 1000},
          2: {'sequence': "\'\'", 'extra-text': '10c', 'space': 1000},
          3: {'sequence': "`````", 'extra-text': '25c', 'space': 1000},
          };

rotary = {'+': {'frequencies': [2600], 'mark': 75, 'space': 25},
          1: {'sequence': '+', 'space': 1000},
          2: {'sequence': '++', 'extra-text': 'ABC', 'space': 1000},
          3: {'sequence': '+++', 'extra-text': 'DEF', 'space': 1000},
          4: {'sequence': '++++', 'extra-text': 'HIJ', 'space': 1000},
          5: {'sequence': '+++++', 'extra-text': 'KLM', 'space': 1000},
          6: {'sequence': '++++++', 'extra-text': 'NOP', 'space': 1000},
          7: {'sequence': '+++++++', 'extra-text': 'QRS', 'space': 1000},
          8: {'sequence': '++++++++', 'extra-text': 'TUV', 'space': 1000},
          9: {'sequence': '+++++++++', 'extra-text': 'WXY', 'space': 1000},
          0: {'sequence': '++++++++++', 'extra-text': 'OPERATOR', 'space': 1000},
          11: {'sequence': '+++++++++++', 'space': 1000},
          }

ss4 = {'.': {'frequencies': [2400.5], 'mark': 35, 'space': 35}, ',': {'frequencies': [2040], 'mark': 350, 'space': 35},
       '\'': {'frequencies': [2040], 'mark': 35, 'space': 35}, ';': {'frequencies': [2040], 'mark': 100, 'space': 35},
       'CF': {'frequencies': [2400.5, 2040], 'mark': 100, 'space': 0},
       "\"": {'frequencies': [2400.5], 'mark': 100, 'space': 35},
       1: {'sequence': "...'", 'space': 0},
       2: {'sequence': "..'.", 'space': 0},
       3: {'sequence': "..''", 'space': 0},
       4: {'sequence': ".'..", 'space': 0},
       5: {'sequence': ".'.'", 'space': 0},
       6: {'sequence': ".''.", 'space': 0},
       7: {'sequence': ".'''", 'space': 0},
       8: {'sequence': "'...", 'space': 0},
       9: {'sequence': "'..'", 'space': 0},
       0: {'sequence': "'.'.", 'space': 0},
       'A': {'sequence': "'.''", 'space': 350},
       'B': {'sequence': ['CF', "\""], 'space': 350},
       'C': {'sequence': "''..", 'space': 350},
       'D': {'sequence': ['CF', ','], 'space': 100},
       '-': {'sequence': "''''", 'space': 350},
       '*': {'sequence': ['CF', ';'], 'space': 100},
       }

ss5 = {1: {'frequencies': [700, 900],
           },
       2: {'frequencies': [700, 1100],
           'extra-text': 'ABC',
           },
       3: {'frequencies': [900, 1100],
           'extra-text': 'DEF',
           },
       4: {'frequencies': [700, 1300],
           'extra-text': 'GHI',
           },
       5: {'frequencies': [900, 1300],
           'extra-text': 'JKL',
           },
       6: {'frequencies': [1100, 1300],
           'extra-text': 'MNO',
           },
       7: {'frequencies': [700, 1500],
           'extra-text': 'PRS',
           },
       8: {'frequencies': [900, 1500],
           'extra-text': 'TUV',
           },
       9: {'frequencies': [1100, 1500],
           'extra-text': 'WXY',
           },
       '*': {'frequencies': [1100, 1700],
             'extra-text': 'KP', 'mark': 110,
             },
       0: {'frequencies': [1300, 1500],
           'extra-text': 'OPERATOR',
           },
       '-': {'frequencies': [1500, 1700],
             'extra-text': 'ST',
             },
       'B0': {'frequencies': [1300, 1700],
              'extra-text': 'KP2', 'mark': 110,
              },
       '+': {'frequencies': [2600],
             'extra-text': '', 'mark': 250, 'space': 1000}
       };

def parse_sequence(sequence):
    if type(sequence) is str:
        return sequence
    elif type(sequence) is list:
        return ''.join(sequence)
    return ''

def interpret_telephony(number, signaling_system, sol_eol=True):
    number = str(number)
    dial_string = ''

    if 'sequence' in signaling_system[1]:
        dial_string += parse_sequence(signaling_system['*']['sequence']) if sol_eol and '*' in signaling_system else ''
        for digit in number:
            try:
                digit = int(digit)
            except:
                continue
            dial_string += str(signaling_system[digit]['sequence'])
        dial_string += parse_sequence(signaling_system['-']['sequence']) if sol_eol and '-' in signaling_system else ''
    else:
        return '*' + number + '-' if sol_eol else number

    return dial_string