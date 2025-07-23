import subprocess


def main():
    commit_message = 'DSA Tests passed'

    try:
        result = subprocess.run(
            f"git add . & git commit -m '{commit_message}'",
            shell=True,
            check=True,
            capture_output=True,
            text=True,
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error during git add/commit: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        return

    try:
        result = subprocess.run(
            'git push',
            shell=True,
            check=True,
            capture_output=True,
            text=True,
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error during git push:")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")


if __name__ == "__main__":
    main()
