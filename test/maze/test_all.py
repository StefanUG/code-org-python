import subprocess
import os

def run_script(script_path):
    env = os.environ.copy()
    # Add your custom environment variable
    env["TESTMODE"] = "True"

    result = subprocess.run(['python', script_path], env=env, stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').strip()
    
    print(f"{output} {script_path}")

def visit_dir(dir):
    for file in os.listdir(dir):
        if os.path.isdir(file):
            visit_dir(os.path.join(dir, file))
        elif file.endswith(".py") and dir != ".":
            run_script(os.path.join(dir, file))


if __name__ == "__main__":
    visit_dir(".")
    print("DONE")
