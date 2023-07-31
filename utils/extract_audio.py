import torchaudio
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class ExtractAudio():
    def __init__(self, audio_path) -> None:
        self.audio_path = audio_path
    
    def read_audio(self):
        waveform, sample_rate = torchaudio.load(self.audio_path, normalize=True)
        if waveform.shape[0] == 2:
            waveform = waveform.flatten()
        return sample_rate, waveform
    
    def extract_mfcc(self, waveform):
        # waveform, sample_rate = torchaudio.load(self.audio_path, normalize=True)
        # plt.figure()
        # plt.plot(waveform.t().numpy())
        
        # 波形创建频谱图， 对数刻度查看频谱图的对数
        # specgram = torchaudio.transforms.Spectrogram()(waveform)

        # print("Shape of spectrogram: {}".format(specgram.size()))

        # plt.figure()
        # plt.imshow(specgram.log2()[0,:,:].numpy(), cmap='gray')

        # 对数刻度查看梅尔光谱图
        specgram = torchaudio.transforms.MelSpectrogram()(waveform)

        print("Shape of spectrogram: {}".format(specgram.size()))

        plt.figure()
        p = plt.imshow(specgram.log2().detach().numpy(), cmap='gray')