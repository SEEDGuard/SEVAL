import subprocess
import os

script_path = "../../tasks/clone_detection/eval.py"
arguments = ["--answers", "answers.json", 
             "--predictions", "predictions.txt"]

# Run the model
with open("output.txt", "w") as f:
    subprocess.run(["python", script_path] + arguments, stderr=f)

# Open the output and expected files
with open("output.txt", "r") as f_output, open("expected.txt", "r") as f_expected:
    output_lines = f_output.readlines()
    expected_lines = f_expected.readlines()
  
    correct_lines = sum(1 for out, exp in zip(output_lines, expected_lines) if out == exp)
    accuracy = (correct_lines / total_lines) * 100

    print(f"Accuracy: {accuracy:.2f}%")

# Delete the output.txt file
os.remove("output.txt")
