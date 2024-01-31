import subprocess
import os


script_path = "../../tasks/code_summarization/eval.py"
reference_file = 'reference.txt'
predictions_file = 'predictions.txt'

with open("output.txt", "w") as f:
    subprocess.run(['python', script_path, reference_file], stdin=open(predictions_file, 'r'), stdout=f, stderr=f, text = True)


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
