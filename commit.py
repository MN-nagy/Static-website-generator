import os
import subprocess


def commit():
    commit_message = 'DSA Tests passed'
    git_dir_path = "/home/Nagy/fortests/projects/DSA/.git"
    lock_file_path = os.path.join(git_dir_path, "index.lock")

    # Attempt the git add and commit operation
    try:
        # Using '&&' instead of '&' to ensure git commit runs only if git add succeeds
        result = subprocess.run(
            f"git add . && git commit -m '{commit_message}'",
            shell=True,
            check=True,
            capture_output=True,
            text=True,
        )
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        # Check if the error is due to the lock file
        if "index.lock': File exists" in e.stderr:
            print(f"Detected Git lock file issue: {lock_file_path}")
            print("Attempting to remove the lock file and retry the commit.")
            try:
                os.remove(lock_file_path)
                print("Lock file removed successfully.")
                # After removing the lock file, retry the commit operation
                # We'll re-call the main logic, but without recursion for safety
                print("Retrying git add and commit...")
                try:
                    retry_result = subprocess.run(
                        f"git add . && git commit -m '{commit_message}'",
                        shell=True,
                        check=True,
                        capture_output=True,
                        text=True,
                    )
                    print(retry_result.stdout)
                except subprocess.CalledProcessError as retry_e:
                    print(f"Error on retry during git add/commit: {retry_e}")
                    print(f"Stdout: {retry_e.stdout}")
                    print(f"Stderr: {retry_e.stderr}")
                    return # Exit if retry also fails

            except OSError as remove_e:
                print(f"Error removing lock file: {remove_e}")
                print("Please manually remove the lock file and try again.")
                return # Exit if we can't remove the lock file
        else:
            # Handle other types of CalledProcessError
            print(f"Error during git add/commit: {e}")
            print(f"Stdout: {e.stdout}")
            print(f"Stderr: {e.stderr}")
            return # Exit for other errors

    # Attempt the git push operation
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
