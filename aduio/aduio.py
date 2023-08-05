import numpy as np
import scipy.io.wavfile as wav
from scipy.fft import fft, ifft

# 读取音频文件
sampling_rate, audio_data = wav.read('warning.wav')
freq_domain = fft(audio_data)
# 配置滤波器参数
cutoff_freq = 1000.0
# 计算归一化截止频率
freq_domain_highpass = freq_domain.copy()
freq_domain_highpass[:cutoff_freq] = 0
# 创建低通滤波器
audio_data_highpass = ifft(freq_domain_highpass)
# 将滤波后的数据写入新的音频文件
wavfile.write('filtered_warning.wav', sample_rate, np.array(filtered_data, dtype=np.int16))