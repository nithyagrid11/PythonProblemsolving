import re
import json
from collections import defaultdict
import os
print(os.getcwd()) #returns a str of the current working directory of the file

def analyze_logs_from_lines(lines):
    patterns = [re.compile(r'(\d+\.\d+\.\d+\.\d+)\s+-\s+(\S+)\s+\[(.*?)\]\s+"(\S+)\s+(\S+)\s+(\S+)"\s+(\d{3})\s+(\S+)\s+"(.*?)"\s+"(.*?)"'), 
                re.compile(r'(\d+\.\d+\.\d+\.\d+)\s+-\s+(\S+)\s+\[(.*?)\]\s+"(\S+)\s+(\S+)\s+(\S+)"\s+(\d{3})\s+(\S+)')]
    
    valid_ip_pattern = re.compile(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b')
    
    ip_counts = defaultdict(int)
    error_freq = defaultdict(int)
    warning_detection = defaultdict(int)
    usage_slots = defaultdict(int)
    method_counts = defaultdict(int)
    endpoint_counts = defaultdict(int)
    
    
    total_count = 0

    for line in lines:
        match = None
        for pattern in patterns:
            match = pattern.search(line)
            if match:
                break
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
        parts = timestamp.split(':')
        hour = parts[1] if len(parts) > 1 else "00"
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
    #spike detection
    spikes ={}
    if len(usage_slots) == 0:
        avg = 0
    else:
        avg = sum(usage_slots.values())/len(usage_slots)
    for hour, count in usage_slots.items():
        if count > avg * 1.5:
            spikes[hour] = count

    total_errors = sum(error_freq.values())
    total_warnings = sum(warning_detection.values())
    suspicious_count = len(suspicious_activity)
    peak_hour = max(usage_slots, key=usage_slots.get, default="None")
    return {
        "total_count": total_count,
        "total_errors": total_errors,
        "total_warnings": total_warnings,
        "suspicious_count": suspicious_count,
        "peak_hour":peak_hour,
        "spike_hours": spikes,

        "details":{
            'ip count': dict(ip_counts),
            'error frequency': dict(error_freq),
            'warning detection': dict(warning_detection),
            'usage slots': dict(usage_slots),
            'suspicious activity detection':   suspicious_activity,
            'log summary': log_summary,
            'total count': total_count
        }
    }
'''if __name__ == "__main__":
    result = analyze_logs_from_lines('server.log')
    print('\nLog Analysis Report\n')
    print(json.dumps(result, indent = 4)) #dumps converts python to json'''




'''172.16.0.1 - user4 [10/Oct/2000:13:00:01 -0700] "GET /home HTTP/1.1" 200 900
172.16.0.1 - user4 [10/Oct/2000:13:01:02 -0700] "GET /about HTTP/1.1" 200 850
172.16.0.1 - user4 [10/Oct/2000:13:02:03 -0700] "GET /services HTTP/1.1" 200 870
172.16.0.1 - user4 [10/Oct/2000:13:03:04 -0700] "GET /contact HTTP/1.1" 200 880
172.16.0.1 - user4 [10/Oct/2000:13:04:05 -0700] "GET /products HTTP/1.1" 200 920
10.0.0.3 - user5 [10/Oct/2000:14:10:10 -0700] "GET /home HTTP/1.1" 200 1000'''

#single json string i/p of above logs
'''{
  "content": "172.16.0.1 - user4 [10/Oct/2000:13:00:01 -0700] \"GET /home HTTP/1.1\" 200 900\n172.16.0.1 - user4 [10/Oct/2000:13:01:02 -0700] \"GET /about HTTP/1.1\" 200 850\n172.16.0.1 - user4 [10/Oct/2000:13:02:03 -0700] \"GET /services HTTP/1.1\" 200 870\n172.16.0.1 - user4 [10/Oct/2000:13:03:04 -0700] \"GET /contact HTTP/1.1\" 200 880\n172.16.0.1 - user4 [10/Oct/2000:13:04:05 -0700] \"GET /products HTTP/1.1\" 200 920\n10.0.0.3 - user5 [10/Oct/2000:14:10:10 -0700] \"GET /home HTTP/1.1\" 200 1000"
}'''


'''192.168.1.10 - john [10/Oct/2000:13:55:36 -0700] "GET /home HTTP/1.1" 200 2326 "http://example.com/start" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
10.0.0.5 - alice [10/Oct/2000:14:01:22 -0700] "POST /api/login HTTP/1.1" 500 1200 "http://example.com/login" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
172.16.0.3 - bob [10/Oct/2000:14:05:10 -0700] "GET /dashboard HTTP/1.1" 404 800 "http://example.com/home" "Mozilla/5.0 (X11; Linux x86_64)"
192.168.1.10 - john [10/Oct/2000:14:10:45 -0700] "GET /profile HTTP/1.1" 200 1500 "http://example.com/dashboard" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
10.0.0.5 - alice [10/Oct/2000:14:12:30 -0700] "PUT /api/update HTTP/1.1" 403 950 "http://example.com/settings" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
172.16.0.3 - bob [10/Oct/2000:14:15:00 -0700] "DELETE /api/remove HTTP/1.1" 500 1100 "http://example.com/admin" "Mozilla/5.0 (X11; Linux x86_64)"'''

#server logs in json string
'''{
  "content": "192.168.1.1 - user1 [10/Oct/2000:12:10:10 -0700] \"GET /home HTTP/1.1\" 200 2326\n10.0.0.5 - user3 [10/Oct/2000:13:01:01 -0700] \"GET /home HTTP/1.1\" 200 1000\n10.0.0.5 - user3 [10/Oct/2000:13:02:02 -0700] \"POST /api HTTP/1.1\" 500 1500\n10.0.0.5 - user3 [10/Oct/2000:13:03:03 -0700] \"GET /data HTTP/1.1\" 404 800\n10.0.0.5 - user3 [10/Oct/2000:13:04:04 -0700] \"GET /data HTTP/1.1\" 404 800\n10.0.0.5 - user3 [10/Oct/2000:13:05:05 -0700] \"GET /data HTTP/1.1\" 404 800\n10.0.0.5 - user3 [10/Oct/2000:13:06:06 -0700] \"GET /data HTTP/1.1\" 404 800\n10.0.0.5 - user3 [10/Oct/2000:13:07:07 -0700] \"GET /data HTTP/1.1\" 404 800\n10.0.0.5 - user3 [10/Oct/2000:13:08:08 -0700] \"GET /data HTTP/1.1\" 404 800\n172.16.0.1 - user4 [10/Oct/2000:14:10:10 -0700] \"GET /contact HTTP/1.1\" 200 900\n172.16.0.1 - user4 [10/Oct/2000:14:11:11 -0700] \"GET /about HTTP/1.1\" 200 1200\n172.16.0.1 - user4 [10/Oct/2000:14:12:12 -0700] \"GET /services HTTP/1.1\" 200 950\n192.168.1.1 - user1 [10/Oct/2000:15:00:00 -0700] \"GET /home HTTP/1.1\" 200 2300\n192.168.1.1 - user1 [10/Oct/2000:15:01:01 -0700] \"GET /products HTTP/1.1\" 200 2100\n10.0.0.5 - user3 [10/Oct/2000:15:05:05 -0700] \"GET /data HTTP/1.1\" 404 800\n10.0.0.5 - user3 [10/Oct/2000:15:05:10 -0700] \"GET /data HTTP/1.1\" 404 800\n10.0.0.5 - user3 [10/Oct/2000:15:05:15 -0700] \"GET /data HTTP/1.1\" 404 800\n10.0.0.5 - user3 [10/Oct/2000:15:05:20 -0700] \"GET /data HTTP/1.1\" 404 800\n10.0.0.5 - user3 [10/Oct/2000:15:05:25 -0700] \"GET /data HTTP/1.1\" 404 800\n10.0.0.5 - user3 [10/Oct/2000:15:05:30 -0700] \"GET /data HTTP/1.1\" 404 800\n10.0.0.5 - user3 [10/Oct/2000:15:05:35 -0700] \"GET /data HTTP/1.1\" 404 800\n10.0.0.5 - user3 [10/Oct/2000:15:05:40 -0700] \"GET /data HTTP/1.1\" 404 800\n10.0.0.5 - user3 [10/Oct/2000:15:05:45 -0700] \"GET /data HTTP/1.1\" 404 800\n10.0.0.5 - user3 [10/Oct/2000:15:05:50 -0700] \"GET /data HTTP/1.1\" 404 800\n10.0.0.5 - user3 [10/Oct/2000:15:05:55 -0700] \"GET /data HTTP/1.1\" 404 800\n10.0.0.5 - user3 [10/Oct/2000:15:06:00 -0700] \"GET /data HTTP/1.1\" 404 800"
}'''