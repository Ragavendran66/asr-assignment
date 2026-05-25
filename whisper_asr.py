import whisper
import pandas as pd
import os


model = whisper.load_model("base")


audio_folder = "audio"


results = []


for file in os.listdir(audio_folder):

    
    if file.endswith(".mp4") or file.endswith(".wav"):

        file_path = os.path.join(audio_folder, file)

        print(f"\nProcessing: {file}")

        
        result = model.transcribe(file_path)

        transcript = result["text"]

        print("Transcription:")
        print(transcript)

        
        results.append({
            "filename": file,
            "transcript": transcript
        })


df = pd.DataFrame(results)


os.makedirs("outputs", exist_ok=True)


df.to_csv("outputs/whisper_output.csv", index=False)

print("\nAll transcriptions saved successfully!")


