import subprocess
import os

# Get current working directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Navigate directories to eval.py and set file parth vairables
script_path = os.path.normpath(os.path.join(script_directory, "../../tasks/code_search/eval.py"))
arguments = ["--answers", "test.jsonl", 
            "--predictions", "predictions.jsonl"]

# Navigate directories to the expected file
expected_file_path = os.path.join(script_directory, "expected.txt")

with open("output.txt", "w") as f:
    subprocess.run(["python", script_path] + arguments, stdout=f)

# Check if the text in the output.txt file matches the text in the expected.txt file
with open("output.txt", "r") as f_output, open(expected_file_path, "r") as f_expected:
    output_content = f_output.read().strip()
    expected_content = f_expected.read().strip()
    if output_content == expected_content:
        print("The text in output.txt matches the text in expected.txt.")
    else:
        print("The text in output.txt does not match the text in expected.txt.")

# Delete the output.txt file
os.remove("output.txt")
