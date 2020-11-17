import os

for path, subdirs, files in os.walk("."):
    for name in files:
        if '.mp4' in name:
            try:
                filename = os.path.join(path, name)
                filename = filename.replace('.mp4', '')

                print(f'Starting {filename}')

                # Add Subtitle to MP4 file using FFMPEG binary
                os.system(
                    f'ffmpeg.exe -i "{filename}.mp4" -i "{filename}.srt" -c:s mov_text -c:v copy -c:a copy -map 0:v -map 0:a -map 1 -disposition:s:0 default -metadata:s:s:0 language=eng "outfile.mp4"')

                # Delete original MP4 file
                os.remove(f'{filename}.mp4')

                # Delete original SRT file
                os.remove(f'{filename}.srt')

                # Rename 'outfile.mp4' to original MP4's name
                os.rename('outfile.mp4', f'{filename}.mp4')

                print(f'Done {filename}')
            except Exception as e:
                print(f'ERROR!\nFile - {filename}\nException - [{e}]')
