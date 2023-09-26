import subprocess
import sys
import re

def trace_route(domain):
    # Ensure the domain is valid to prevent command injection
    if not re.match(r'^[a-zA-Z\d\-\.]+$', domain):
        print("Invalid domain provided.")
        return

    # Determine the appropriate command based on the platform
    cmd = []
    if sys.platform == "win32":
        cmd = ["tracert", domain]
    else:
        cmd = ["traceroute", domain]

    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing traceroute: {e.output}")
        return
    except FileNotFoundError:
        print("Traceroute command not found. Ensure it's installed and in your PATH.")
        return
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return

    # Process and display the result
    lines = result.split('\n')
    print(f"Traceroute to {domain}\n{'=' * 40}")
    for line in lines:
        if not line:
            continue
        parts = line.split()
        hop_number = parts[0]
        details = ' '.join(parts[1:])
        print(f"Hop {hop_number}: {details}\n{'-' * 40}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 trace_route.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    trace_route(domain)

