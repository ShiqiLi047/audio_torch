import os
import sys
print(sys.path)
def convert_video_audio(video_dir, save_dir):
    video_paths = os.listdir(video_dir)
    
    for i in range(len(video_paths)):
        predix = video_paths[i].split(".")[0]
        filename = os.path.join(video_dir, video_paths[i])
        out_filename = os.path.join(save_dir, predix + ".wav")

        command = "ffmpeg -i \"" + filename.replace("\\", "/") + "\" -ac 2 -f wav -y \"" + out_filename.replace("\\", "/") + "\""

        print(command)
        # os.system(
        #     command.encode('ascii', 'ignore').decode('unicode_escape').replace(
        #         "\0", ""))
        os.system(command)

if __name__ == "__main__":
    video_dir = "f:\\learn\\code\\ASR_torch\\audio_data\\video"
    save_dir = "f:\\learn\\code\\ASR_torch\\audio_data\\audio"
    convert_video_audio(video_dir, save_dir)