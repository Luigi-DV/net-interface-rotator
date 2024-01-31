import subprocess

command = "openssl rand -hex 6 | sed 's/\\(..\\)/\\1:/g; s/.$//'"


def generateMacAddress() -> str:
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True)
        if result.stderr:
            return result.stderr
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Command execution failed with return code", e.returncode)
        print("Error:", e.stderr)
