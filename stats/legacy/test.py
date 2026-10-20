servers = [
    {"name": "Debian", "cpu_usage": 75},
    {"name": "Proxmox", "cpu_usage": 20},
    {"name": "Docker", "cpu_usage": 45}
]

server_sort = sorted(servers, key=lambda server: server["cpu_usage"])
print(server_sort)