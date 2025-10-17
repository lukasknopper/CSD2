

import eindopdracht_sequencer_ui
numerator, bpm, totalDur = eindopdracht_sequencer_ui.choose_settings()

import eindopdracht_sequencer_generatie
event_dict = (eindopdracht_sequencer_generatie.make_fractal_rhythm_event_dict(3, numerator, totalDur))

import eindopdracht_sequencer_playback
eindopdracht_sequencer_playback.play_events(event_dict)






#TODO loopen fixen, laatste is nu gesynced met eerste
