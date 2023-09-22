# Blocks websites on Chrome and Edge browsers
# Does not work on Firefox

import os

def block_it(url):
    print("Working on it")
    # Modify the system's host file to block the website
    try:
        # Add the website URL to the host file, redirecting to localhost
        with open('/etc/hosts' if os.name != 'nt' else r'C:\Windows\System32\drivers\etc\hosts', 'a') as hosts_file:
            hosts_file.write('127.0.0.1\t{}\n'.format(url))
        print('Website blocked successfully.')
    except PermissionError:
        print('Permission denied. Run the script as administrator.')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    website = "gop.com"
    block_it(website)

