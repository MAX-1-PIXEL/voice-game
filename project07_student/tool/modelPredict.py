import sounddevice as sd
import numpy as np
import librosa
from sklearn.linear_model import LogisticRegression
from joblib import dump, load
import threading
import time
import keyboard

def extract_features(audio, sample_rate):
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_processed = np.mean(mfccs.T, axis=0)
    return mfccs_processed

duration = 1/5  
sample_rate = 22050

laststat = 'background'

# 按鍵模擬
def press_key(key, duration=None):
    keyboard.press(key)
    if duration:
        time.sleep(duration)
        keyboard.release(key)
    else:
        keyboard.release(key)

# callback 裡不再直接使用 model，改用 closure 傳進來的 model
def get_callback(model):
    def callback(indata, frames, time, status):
        if status:
            print("Error:", status)

        audio = indata[:, 0]
        features = extract_features(audio, sample_rate)
        prediction = model.predict([features])
        print("Prediction result:", prediction)

        global laststat
        if prediction[0] == "up":
            if laststat == 'up':
                threading.Thread(target=press_key, args=("up",)).start()
            laststat = 'up'

        elif prediction[0] == "down":
            if laststat == 'down':
                threading.Thread(target=press_key, args=("down", 0.5)).start()
            laststat = 'down'
        else:
            laststat = 'background'
    return callback

def main(file):
    global stop_flag
    stop_flag = False

    # 載入模型
    model = load(file)

    print("Start live monitoring (press q to return to the main menu)")
    with sd.InputStream(callback=get_callback(model), dtype='float32', channels=1, samplerate=sample_rate, blocksize=int(sample_rate * duration)):
        while not stop_flag:
            if keyboard.is_pressed('q'): 
                print("Detect 'q', end recording and return to the main menu")
                stop_flag = True
            time.sleep(0.2)

    return
