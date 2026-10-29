import subprocess

def run_git(command):
    try:
        result = subprocess.run(
            ["git"] + command,
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Git error:", e.stderr)

print("=== Git Helper ===")
print("1. Git Status")
print("2. Git Add")
print("3. Git Commit")
print("4. Git Log")
print("5. Git Pull")
print("6. Git Push")

choice = input("Choose an option: ")

if choice == "1":
    run_git(["status"])

elif choice == "2":
    run_git(["add", "."])

elif choice == "3":
    message = input("Enter commit message: ")
    run_git(["commit", "-m", message])

elif choice == "4":
    run_git(["log", "--oneline"])

elif choice == "5":
    run_git(["pull"])

elif choice == "6":
    run_git(["push"])

else:
    print("Invalid choice.")


    



