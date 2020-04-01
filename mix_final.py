#play the output video in vlc player , quicktime player does not seems to play audio.

#first canny edge detection using edge.py to get the artistic video ..no audio is present here
#then extract the audio for that video file which will be superimposed later. use the extract_audio.py for this
#superimpose video and corresponding audio using mix_final.py

import moviepy.editor as mp 
video=mp.VideoFileClip("elvis_videoedge.mp4")
video.write_videofile("elvis_final.mp4", audio="elvis.mp3")

'''
import moviepy.editor as mp
video = mp.VideoFileClip("yiyasha_video.mp4")
audio = mp.AudioFileClip("yiyasha.mp3")
#video.write_videofile("mix.mp4", audio="yiyasha.mp3")

mix = video.set_audio(mp.AudioFileClip("yiyasha.mp3"))
#mix = video.set_audio(audio.set_duration(video))
mix.write_videofile("mix.mp4",codec='libx264', 
                     audio_codec='aac',remove_temp=False)
'''

#https://www.reddit.com/r/moviepy/comments/343q8j/what_is_the_correct_way_to_add_audio_to_a_video/
#https://stackoverflow.com/questions/40445885/no-audio-when-adding-mp3-to-videofileclip-moviepy