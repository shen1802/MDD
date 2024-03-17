from pydub import AudioSegment
import os


class AudioEditor:
    @staticmethod
    def load_audio(file_path):
        file_ext = os.path.splitext(file_path)[1].lower()
        if file_ext == '.mp3':
            return AudioSegment.from_mp3(file_path)
        elif file_ext == '.aac':
            return AudioSegment.from_file(file_path, format='aac')
        elif file_ext == '.flac':
            return AudioSegment.from_file(file_path, format='flac')
        elif file_ext == '.wav':
            return AudioSegment.from_wav(file_path)
        elif file_ext == '.aiff':
            return AudioSegment.from_file(file_path, format='aiff')
        else:
            raise ValueError("Unsupported file type")

    @staticmethod
    def save_audio(audio_data, output_path):
        file_ext = os.path.splitext(output_path)[1].lower()
        if file_ext in ['.mp3', '.aac', '.flac', '.wav', '.aiff']:
            audio_data.export(output_path, format=file_ext[1:])
        else:
            raise ValueError("Unsupported file type or format")

    @staticmethod
    def convert_audio_format(audio_data, new_format, new_file_path=None):
        if new_file_path is None:
            base = os.path.splitext(audio_data.filename)[0]
            new_file_path = f"{base}.{new_format}"
        audio_data.export(new_file_path, format=new_format)
        print(f"Audio converted and saved as {new_file_path}")
        return new_file_path

    @staticmethod
    def trim_audio(audio_data, start_time_ms, end_time_ms, output_path=None):
        trimmed_audio = audio_data[start_time_ms:end_time_ms]
        if output_path:
            trimmed_audio.export(output_path, format=os.path.splitext(output_path)[1][1:])
            print(f"Trimmed audio saved as {output_path}")
        else:
            return trimmed_audio

    @staticmethod
    def speed_up_audio(audio_data, factor, output_path=None):
        sped_up_audio = audio_data.speedup(playback_speed=factor)
        if output_path:
            sped_up_audio.export(output_path, format=os.path.splitext(output_path)[1][1:])
            print(f"Sped-up audio saved as {output_path}")
        else:
            return sped_up_audio

    @staticmethod
    def slow_down_audio(audio_data, factor, output_path=None):
        new_frame_rate = int(audio_data.frame_rate / factor)
        slowed_down_audio = audio_data.set_frame_rate(new_frame_rate)
        if output_path:
            slowed_down_audio.export(output_path, format=os.path.splitext(output_path)[1][1:])
            print(f"Slowed-down audio saved as {output_path}")
        else:
            return slowed_down_audio

    @staticmethod
    def volume_up_audio(audio_data, dB, output_path=None):
        louder_audio = audio_data + dB
        if output_path:
            louder_audio.export(output_path, format=os.path.splitext(output_path)[1][1:])
            print(f"Volume-increased audio saved as {output_path}")
        else:
            return louder_audio

    @staticmethod
    def volume_down_audio(audio_data, dB, output_path=None):
        quieter_audio = audio_data - dB
        if output_path:
            quieter_audio.export(output_path, format=os.path.splitext(output_path)[1][1:])
            print(f"Volume-decreased audio saved as {output_path}")
        else:
            return quieter_audio
