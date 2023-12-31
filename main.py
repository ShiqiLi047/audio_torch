import os
from utils.extract_audio import ExtractAudio
from utils import short_term_feature
from utils.audio_basic_io import read_audio_file
from utils import audio_train_test as aT

def load_audio(audio_paths):
    for audio_path in audio_paths:
        # extract_audio = ExtractAudio(audio_path)
        # sample_rate, waveform = extract_audio.read_audio()
        
        # # read audio
        sample_rate, waveform = read_audio_file(audio_path)
        
        print("extract feature")
        # extract_audio.extract_mfcc(waveform)
        feature, f_names = short_term_feature.feature_extraction(waveform, sample_rate, 
                                                        0.050 * sample_rate, 0.050 * sample_rate)
        assert feature.shape[0] == len(f_names), "Number of features and feature " \
                                        "names are not the same"

        

def main():
    audio_path_dir = "f:\\learn\\code\\ASR_torch\\audio_data\\audio"
    audio_path_list = os.listdir(audio_path_dir)
    audio_paths = []
    for path in audio_path_list:
        audio_paths.append(os.path.join(audio_path_dir, path))

    # load_audio(audio_paths)
    
    aT.extract_features_and_train([audio_path_dir], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)
    aT.file_classification("audio_data\\preview.wav", "svmSMtemp","svm")
    

if __name__ == "__main__":
    main()