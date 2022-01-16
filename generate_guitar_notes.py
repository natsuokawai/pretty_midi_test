import pretty_midi

note_names = ['C5', 'C#5', 'D5', 'D#5', 'E5', 'F5',
              'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5', 'C6']
guitar_program = pretty_midi.instrument_name_to_program(
    'Acoustic Guitar (nylon)')

for note_name in note_names:
    guitar_sound = pretty_midi.PrettyMIDI()
    guitar = pretty_midi.Instrument(program=guitar_program)
    note_num = pretty_midi.note_name_to_number(note_name)
    note = pretty_midi.Note(velocity=100, pitch=note_num, start=0, end=.5)
    guitar.notes.append(note)
    guitar_sound.instruments.append(guitar)
    guitar_sound.write('guitar_{}.mid'.format(note_name))
