import winsound
import time


def beep_delay(f_complete):
    return max(0.1 + 0.9 * f_complete, 0.15)


def play_bomb_beep_sound():
    total_time = 40
    start_time = time.time()
    elapsed_time = 0

    while elapsed_time < total_time:
        elapsed_time = time.time() - start_time
        f_complete = (40 - elapsed_time) / total_time
        frequency = 2640  # Frequency of beep in Hz
        duration = 100  # Duration of beep in milliseconds
        delay = beep_delay(f_complete)

        print(f"Elapsed time: {elapsed_time:.2f}s - Delay: {delay:.2f}s - Frequency: {frequency:.2f}Hz - Duration: {duration:.2f}")

        winsound.Beep(frequency, duration)
        time.sleep(delay - duration / 1000)

    # Explosion sound
    winsound.PlaySound("explosion.wav", winsound.SND_FILENAME)


play_bomb_beep_sound()
