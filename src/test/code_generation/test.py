import subprocess
import os

script_path = "../../tasks/code_generation/eval.py"
arguments = ["--answers", "answers.json", 
             "--predictions", "predictions.txt"]

with open("output.txt", "w") as f:
    subprocess.run(["python", script_path] + arguments, stderr=f)
    

# Check if the text in the output.txt file matches the string "INFO:__main__:BLEU: 16.68, EM: 17.0"
expected_text = "INFO:__main__:BLEU: 16.68, EM: 17.0"
with open("output.txt", "r") as f:
    file_content = f.read()
    if expected_text in file_content:
        print("The text in output.txt matches the expected string.")
    else:
        print("The text in output.txt does not match the expected string.")

# Delete the output.txt file
os.remove("output.txt")
        