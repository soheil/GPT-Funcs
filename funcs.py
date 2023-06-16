import os
import subprocess


def play_music(audio_data_hex):
    """
    Play music to user.

    Args:
        audio_data_hex (string): Hex representation of the raw audio binary data with 44100 sample rate.
    """
    bin_data = base64.b64decode(audio_data_hex)
    file_path = "/tmp/a.mp3"
    with open(file_path, "wb") as file:
        file.write(bin_data)

    print(f"Binary file saved as: {file_path}")
    os.system("/usr/bin/afplay " + file_path)


def speak(sentence, spoken_speed=210):
    """
    Convert the sentence to spoken words and speak it to user.

    Args:
        sentence (string): English sentence that should be spoken.
        spoken_speed (number): A value from 100 to 300 determining how fast the sentence is spoken.
    """
    subprocess.Popen(['say', '-v', 'Karen', '-r', str(spoken_speed), sentence])


def create_dir(relative_path):
    """
    Create a dir in current working dir.

    Args:
        relative_path (string): Path from the current working dir to create the dir in
    """
    try:
        os.mkdir(relative_path)
    except Exception as e:
        print(e)


def save_file(relative_path_to_file, content):
    """
    Create a file in the specified relative path from the current working dir.

    Args:
        relative_path_to_file (string): Path from the current working dir to create the file in
        content (string): Content of the file to create
    """
    with open(relative_path_to_file, "w") as f:
        f.write(content)
