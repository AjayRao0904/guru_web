import csv
from pytube import YouTube
from moviepy.editor import VideoFileClip
import google.generativeai as genai

genai.configure(api_key="AIzaSyDFtRLzmGtpbs0tI1H3VJhTvMhia1eFdpo")

generation_config = {
  "temperature": 0.6,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}
safety_settings=[]

with open('urls8.csv',mode='r',encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile)
    i=1
    for row in csvreader:  
         # Download the video
        model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                    generation_config=generation_config,
                                  safety_settings=safety_settings)

        convo =  model.start_chat(
            history=[
              {
                "role": "user",
                "parts": [
                  "given this text:\nSRI.N RAMANI FLUTE Ragam Thanam Pallavi - Amritavarshini.\n{\n \"Raaga\":\"Amritavarshini\",\n \"rasa\":[\"Veera\",\"Bhayanakam\",\"Adhbutha\"],\n\"description\":\"\",\n\"instrument\":\"\"\n}\nonly fill the description and instrument fields based on the instructions i give you \nfill the description field with 5-10 keywords that the given text insinuates.\nfill the instrument field with instrument mentioned in the text.",
                ],
              },
              {
                "role": "model",
                "parts": [
                  "{\n \"Raaga\":\"Amritavarshini\",\n \"rasa\":[\"Veera\",\"Bhayanakam\",\"Adhbutha\"],\n\"description\":\"Ragam Thanam Pallavi,Thanam,Pallavi,Flute\",\n\"instrument\":\"Flute\"\n}",
                ],
              },
            ]
          )

        message =row[2]
        convo.send_message(f"given this text:\n\"{message}\"\n{{\n \"Raaga\":\"Amritavarshini\",\n \"rasa\":[\"Veera\",\"Bhayanakam\",\"Adhbutha\"],\n\"description\":\"\",\n\"instrument\":\"\"\n}}\nonly fill the description and instrument fields based on the instructions i give you \n fil the description field with 5-10 keywords that the given text insinuates.\nfill the instrument field with instrument mentioned in the text.")
        output_text = convo.last.text

        # Write output to a file
        with open(f"carnatic,Amritavarshini{i}.txt", "w") as file:
            file.write(output_text)

        print(f"Output has been saved to file{i}.txt")
        i+=1