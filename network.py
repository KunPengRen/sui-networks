import os
import subprocess
import yaml
import sys
# Path to the directory containing the YAML files
files_dir = '/users/kunpeng/sui-networks/genesis/files/'

full_node_file_path = '/users/kunpeng/sui-networks/genesis/static/fullnode.yaml'

def start_validators():
    # Iterate over all YAML files in the directory
    for filename in os.listdir(files_dir):
        if filename.endswith('8080.yaml'):
            # Full path to the current YAML file
            file_path = os.path.join(files_dir, filename)
            ip_port = filename.replace('.yaml', '')
            ip, port = ip_port.split('-')

            # Construct the ssh command
            ssh_command = f'ssh {ip} "/users/kunpeng/local/bin/sui-node --config-path {file_path}  > /dev/null 2>&1 &"'
            print(ssh_command)
            # Execute the command
            try:
                subprocess.Popen(ssh_command, shell=True)
                print(f"Executed command on {ip}:{port}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to execute command on {ip}:{port}")

def start_fullnode():
    # Iterate over all YAML files in the directory
    for filename in os.listdir(files_dir):
        if filename.endswith('8080.yaml'):
            # Full path to the current YAML file
            file_path = os.path.join(files_dir, filename)
            ip_port = filename.replace('.yaml', '')
            ip, port = ip_port.split('-')

            # Construct the ssh command
            ssh_command = f'ssh {ip} "/users/kunpeng/local/bin/sui-node --config-path {full_node_file_path}  > /dev/null 2>&1 &"'
            print(ssh_command)
            # Execute the command
            try:
                subprocess.Popen(ssh_command, shell=True)
                print(f"Executed command on {ip}:{port}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to execute command on {ip}:{port}")
                 
def stop_validators():
    # Iterate over all YAML files in the directory
    for filename in os.listdir(files_dir):
        if filename.endswith('8080.yaml'):
            # Full path to the current YAML file
            file_path = os.path.join(files_dir, filename)

            # Assuming the structure of the YAML is straightforward
            ip_port = filename.replace('.yaml', '')
            ip, port = ip_port.split('-')

            kill_command = f'ssh {ip} \"pkill -f sui-node\"'
            process_kill = subprocess.Popen(kill_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process_kill.communicate()  # This waits for the command to complete

            if process_kill.returncode == 0:
                print(f"Killed sui-node on {ip}:{port}")
            else:
                print(f"Failed to kill sui-node on {ip}:{port}: {stderr.decode()}")

            # Second SSH command to remove the directory
            remove_command = f'ssh {ip} \"rm -rf /data/kunpeng/sui-test/sui\"'
            process_remove = subprocess.Popen(remove_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process_remove.communicate()  # This waits for the command to complete

            if process_remove.returncode == 0:
                print(f"Removed directory on {ip}:{port}")
            else:
                print(f"Failed to remove directory on {ip}:{port}: {stderr.decode()}")

                
                    
if __name__ == '__main__':
    error_msg = "python3 network.py [start|stop]"
    if len(sys.argv) != 2:
        print(error_msg)
        sys.exit(1)
    if sys.argv[1] == "start":
        start_validators()
        start_fullnode()
    elif sys.argv[1] == "stop":
        stop_validators()
