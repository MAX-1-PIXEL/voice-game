import sounddevice as sd
from scipy.io.wavfile import write
import os
import keyboard  # 鍵盤觸發錄音
import sys

# 錄音參數
sample_rate = 44100  # 取樣率（每秒樣本數）
duration = 1.5         # 錄音持續時間（秒）
file_extension = '.wav'  # 音訊檔案副檔名

def record_audio(count, base_filename):
    print("Starting recording...")
    try:
        audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32', device=0)
        sd.wait()  # 等待錄音完成
    except Exception as e:
        print(e)
        return count

    filename = f"{base_filename}_{count}{file_extension}"
    path = os.path.join(base_filename, filename)

    write("./" + '遊戲' + "/" + path, sample_rate, audio)
    print(f"\nRecording finished, file saved to: {path}\n")
    return count + 1

def main():
    print("###############################")
    print("##                           ##")
    print("##                           ##")
    print("##      Voice Recorder       ##")
    print("##                           ##")
    print("##                           ##")
    print("###############################")
    print("")

    run = True
    while run:
        count = 1
        print("")
        print("1. Background")
        print("2. Up")
        print("3. Down")
        print("4. Exit")
        print("")
        usr_input2 = input("Please choose which type of sound to record: ")

        print("You chose", usr_input2)

        if usr_input2 == "1":
            base_filename = "background"
        elif usr_input2 == "2":
            base_filename = "up"
        elif usr_input2 == "3":
            base_filename = "down"
        elif usr_input2 == "4":
            break
        else:
            print("Error! Please input a number from 1 to 4.")
            continue  # 跳過後面流程，回到主選單

        if usr_input2 in ["1", "2", "3"]:
            try:
                num = int(input("How many times do you want to collect: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            os.makedirs("./" + '遊戲' + "/" + base_filename, exist_ok=True)

            print("Press 'R' to start recording...")
            keyboard.wait('r')  # 等待使用者按下 'R'

            while count <= num:
                count = record_audio(count, base_filename)

                if count == num + 1:
                    print("All recordings complete.")
                else:
                    print(f"We have {num - count + 1} times left. Press 'R' to record again.")
                    keyboard.wait('r')

if __name__ == "__main__":
    main()
