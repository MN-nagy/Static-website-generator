import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser(
        description="Fast pushing",
        usage="python commit.py <commit message>"
    )


    parser.add_argument("commit", type=str, nargs="+", help="add commit message")


    args = parser.parse_args()
    commit_message = " ".join(args.commit)

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
