import re
import json
from collections import defaultdict
import os
print(os.getcwd()) #returns a str of the current working directory of the file

def analyze_logs(n):
    log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)\s+-\s+(\S+)\s+\[(.*?)\]\s+"(\S+)\s+(\S+)\s+(\S+)"\s+(\d{3})\s+(\S+)')
    
    valid_ip_pattern = re.compile(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b')
    
    ip_counts = defaultdict(int)
    error_freq = defaultdict(int)
    warning_detection = defaultdict(int)
    usage_slots = defaultdict(int)
    method_counts = defaultdict(int)
    endpoint_counts = defaultdict(int)
    
    total_count = 0

    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #__file__ is a built-in variable in python holds the path of the current file; dirname - so till backend
    filepath = os.path.join(BASE_DIR, n) #joining backend and server.log

    with open(filepath, 'r') as f:  
        for line in f:
            match = log_pattern.search(line)
            if not match:
                continue

            ip = match.group(1)
            status = int(match.group(7))
            timestamp = match.group(3)
            method = match.group(4)
            endpoint = match.group(5)

            total_count += 1
            #metric 1: ip freq - later used for sus activity
            if valid_ip_pattern.fullmatch(ip):
                ip_counts[ip] += 1
            #metric2: error freq - server side issues (500-599 range)
            if status >= 500:
                error_freq[status] += 1
            #metric3: warning detection - client side issues (400-499 range)
            if 400<=status<500:
                warning_detection[status] += 1
            #metric4: usage slots - timestamp
            hour = timestamp.split(':')[1]
            usage_slots[hour] += 1
            #metric5: log summary
            method_counts[method] += 1
            endpoint_counts[endpoint] += 1

    suspicious_activity = {}
    threshold = 4
    for ip, count in ip_counts.items():
        if count >= threshold:
            suspicious_activity[ip] = count
    log_summary = {
        'methods': dict(method_counts),
        'endpoint': dict(endpoint_counts)
    }
    return {
        'ip count': dict(ip_counts),
        'error frequency': dict(error_freq),
        'warning detection': dict(warning_detection),
        'usage slots': dict(usage_slots),
        'suspicious activity detection': suspicious_activity,
        'log summary': log_summary,
        'total count': total_count
    }
if __name__ == "__main__":
    result = analyze_logs('server.log')
    print('\nLog Analysis Report\n')
    print(json.dumps(result, indent = 4)) #dumps converts python to json