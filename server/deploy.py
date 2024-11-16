from flask import Flask, request, jsonify
from flask_cors import CORS
# from audiocraft.models import musicgen
# import torch
# import soundfile as sf
import subprocess

app = Flask(__name__)
CORS(app)
@app.route('/generate-music', methods=['POST'])
def generate_music():
    # Extract JSON data from the POST request
    data = request.get_json()

    # Extract the model ID and the user prompt from the JSON
    # model_id = data.get('model_id', 'melody')  # Default model_id if not provided
    prompt = data.get('prompt', '')
    print(prompt)

    # Load the pre-trained model
    # model = musicgen.MusicGen.get_pretrained(model_id, device='cuda')
    # model.set_generation_params(duration=20)

    # Assuming you have a model checkpoint specific to the model_id
    # model.lm.load_state_dict(torch.load(f'./models_small_2/lm_final_{model_id}.pt'))

    # Generate the music based on the prompt
    # res = model.generate([prompt], progress=True)

    # Move the generated audio from GPU to CPU
    # res = res.cpu().numpy()
    # res = res.squeeze()  # Remove unnecessary dimensions

    # Save the audio to a file
    # output_file = 'smallModelNewDataset.wav'
    # sf.write(output_file, res, 32000)

    # Optionally, play the audio file
    # subprocess.call(['start', output_file], shell=True)

    return jsonify({"message": "Music generated and saved to file"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
