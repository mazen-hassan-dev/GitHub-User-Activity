from get_user_activity import getUserActivity
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
        getUserActivity(username)
    else:
        print("Error fetching the following GitHub username. Please check the command line arguments or username.")

