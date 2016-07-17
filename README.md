# video-collage

Watch random fragments of a video collection.

You might call it thusly:

    python video_collage.py --path /mnt --lapse_min=30 --lapse_max=100 2>/dev/null

It will go through you'r video collection in /mnt and play at random
order lapses of 30 to 100 seconds, at random. In this example I added
2>/dev/null to ignore stuff stderr from libvlc. It will print to
stdout played videos.
