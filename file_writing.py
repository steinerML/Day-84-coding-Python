filename = 'File Reading/write.txt'

#Write my first line
with open (filename, 'w') as f:
    f.write('This is my first writing exercise.')

#Write multiple lines
with open (filename, 'w') as f:
    f.write('This is my second writing exercise.\n')
    f.write('This is my third writing exercise.\n')
    f.write('This is my fourth writing exercise.\n')

#Note that 
with open (filename, 'w') as f:
    f.write('This erases everything.\n')
