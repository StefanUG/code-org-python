import subprocess
import os

def run_script(dir, file):
    env = os.environ.copy()
    # Add your custom environment variable
    env["TESTMODE"] = "True"

    result = subprocess.run(['python', file], env=env, stdout=subprocess.PIPE, cwd=dir)
    output = result.stdout.decode('utf-8').strip()
    
    print(f"{output} {os.path.join(dir, file)}")

def visit_dir(dir):
    for file in os.listdir(dir):
        fullpath = os.path.join(dir,file)
        if os.path.isdir(fullpath):
            visit_dir(fullpath)
        elif file.endswith(".py") and file.startswith("test_") and file != "test_all.py":
            run_script(dir, file)


if __name__ == "__main__":
    visit_dir(".")
    print("DONE")
