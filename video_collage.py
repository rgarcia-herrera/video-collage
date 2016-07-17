import argparse
from sh import find, cvlc
from random import shuffle, randint
import vlc

parser = argparse.ArgumentParser(description='play random samples from films')
parser.add_argument('--path', type=str)
parser.add_argument('--min_start', type=int, default=3*60, help="minimum start time in seconds")
parser.add_argument('--lapse_min', type=int, default=3*60, help="minimum lapse length in seconds")
parser.add_argument('--lapse_max', type=int, default=11*60, help="maximum lapse length in seconds")
args = parser.parse_args()


filmes = find( args.path, '-iname', '*mp4',
               '-o', '-iname', '*avi',
               '-o', '-iname', '*mkv',               
               '-o', '-iname', '*mov')

filtered = []

for f in filmes:
    film = f.strip()
    if film.lower().find('sample') == -1:
        filtered.append( film )

shuffle(filtered)

vlci = vlc.Instance()

for f in filtered:
    media = vlci.media_new(f)
    media.parse()
    media_length = media.get_duration()/1000

    lapse = randint(args.lapse_min, args.lapse_max)
    start = randint(args.min_start, media_length - lapse)
    stop  = start + lapse
    
    cvlc(f,
         no_osd=True,
         start_time=start,
         stop_time=stop )
