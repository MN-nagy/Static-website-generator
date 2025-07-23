import os
import subprocess


def commit():
    git_dir = '/home/Nagy/fortests/projects/DSA/.git' # Assuming this is your .git directory
    lock_file = os.path.join(git_dir, 'index.lock')

    # 1. Check for and remove the lock file
    if os.path.exists(lock_file):
        print(f"Found existing lock file: {lock_file}. Attempting to remove it.")
        try:
            os.remove(lock_file)
            print("Lock file removed successfully.")
        except OSError as e:
            print(f"Error removing lock file: {e}")
            print("Please remove the lock file manually and try again.")
            return   

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
    commit()
