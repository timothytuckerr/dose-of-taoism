import inflect
import json

p = inflect.engine()

current_chapter = 0
next_chapter_string = ''
chapter_to_string = {}
chapter_tracker = {}
newline_last = False
skip_next = False

with open('gia.txt') as f:
    lines = f.readlines()
    next_chapter_string = p.number_to_words(current_chapter + 1).capitalize() + '\n'

    for line in lines:
        if skip_next:
            skip_next = False
            continue
        if line == next_chapter_string:
            current_chapter += 1
            next_chapter_string = p.number_to_words(current_chapter + 1).capitalize() + '\n'
            # print(repr(next_chapter_string))
            chapter_to_string[current_chapter] = ''
            skip_next = True
            newline_last = False
        else:
            if line == '\n' or line == ' \n':
                newline_last = True
            else:
                if newline_last:
                    chapter_to_string[current_chapter] += '\n'
                chapter_to_string[current_chapter] += line
                newline_last = False

print('exporting txts...')
for key in chapter_to_string.keys():
    w = open('chapters/' + str(key) + '.txt', 'w')
    w.write(chapter_to_string[key])

print('exporting json...')
with open('chapters.json', 'w') as export:
    json.dump(chapter_to_string, export)

print('success!')
