import subprocess
import os

script_path = "../../tasks/code_generation/eval.py"
arguments = ["--answers", "answers.json", 
             "--predictions", "predictions.txt"]

with open("output.txt", "w") as f:
    subprocess.run(["python", script_path] + arguments, stderr=f)
    

# Check if the text in the output.txt file matches the text in the expected.txt file
with open("output.txt", "r") as f_output, open("expected.txt", "r") as f_expected:
    output_content = f_output.read()
    expected_content = f_expected.read()
    if output_content == expected_content:
        print("The text in output.txt matches the text in expected.txt.")
    else:
        print("The text in output.txt does not match the text in expected.txt.")

# Delete the output.txt file
os.remove("output.txt")
