import argparse
from sh import find, cvlc
from random import shuffle, randint

parser = argparse.ArgumentParser(description='play random samples from films')
parser.add_argument('root_path', type=str)
args = parser.parse_args()


filmes = find( args.root_path, '-iname', '*mp4',
               '-o', '-iname', '*avi',
               '-o', '-iname', '*mkv',               
               '-o', '-iname', '*mov')


filtered = []

for f in filmes:
    film = f.strip()
    if film.lower().find('sample') == -1:
        filtered.append( film )

shuffle(filtered)

# 90 minutes, 60 seconds each
start = randint(3*60, 90*60)
lapse = 7
lapse = randint(3*60, 11*60)
stop  = start + lapse

for f in filtered:
    cvlc(f,
         no_osd=True,
         start_time=start,
         stop_time=stop )
