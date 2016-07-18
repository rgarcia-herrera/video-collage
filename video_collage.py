import argparse
from sh import find
from random import shuffle, randrange, random
import vlc
from time import sleep

parser = argparse.ArgumentParser(description='play random samples from films')
parser.add_argument('--path', type=str)
parser.add_argument('--lapse_min', type=int, default=3*60, help="minimum lapse length in seconds")
parser.add_argument('--lapse_max', type=int, default=11*60, help="maximum lapse length in seconds")
args = parser.parse_args()


filmes = find( args.path, '-iname', '*mp4',
               '-o', '-iname', '*avi',
               '-o', '-iname', '*mkv',
               '-o', '-iname', '*iso',
               '-o', '-iname', '*vob',
               '-o', '-iname', '*ogm',
               '-o', '-iname', '*m4v',
               '-o', '-iname', '*ogg',
               '-o', '-iname', '*flv',
               '-o', '-iname', '*divx',
               '-o', '-iname', '*wmv',
               '-o', '-iname', '*mov')

filtered = []

for f in filmes:
    film = f.strip()
    if film.lower().find('sample') == -1:
        filtered.append( film )

shuffle(filtered)

vlci = vlc.Instance()
p = vlci.media_player_new()

for f in filtered:
    try:
        media = vlci.media_new(f)
        p.set_media(media)
        p.play()
        p.set_position(random())
        print f
        sleep(randrange(args.lapse_min, args.lapse_max))
    except:
        p.stop()
