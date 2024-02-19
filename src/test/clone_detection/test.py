import subprocess
import os

# Path to the script you want to execute
script_path = "../../tasks/clone_detection/eval.py"

# Command line arguments for the script
arguments = ["--a", "answers.jsonl",
             "--p", "predictions.jsonl"]

try:
    # Execute the script and redirect both stdout and stderr to the output.txt file
    with open("output.txt", "w") as f:
        subprocess.run(["python", script_path] + arguments, stdout=f, stderr=subprocess.STDOUT)
    print("Evaluation completed successfully.")
except Exception as e:
    print(f"Error during evaluation: {str(e)}")

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
