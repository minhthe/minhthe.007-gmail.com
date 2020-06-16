'''
https://leetcode.com/problems/validate-ip-address/
'''
class Solution:
    def validIPAddress(self, IP: str) -> str:
        try:
            ips = IP.split(".")
            if len(ips) == 4:
                for ip in ips:
                    if int(ip) < 0 or int(ip) > 255 or len(str(ip)) != len(str(int(ip))): return 'Neither'
                return "IPv4"
            ips = IP.split(":")
            if len(ips) == 8:
                for ip in ips:
                    ip2 = int(ip, 16)
                    if ip2 < 0 or ip2 > int('FFFF', 16) or len(ip) > 4 or ip[0] == '-': return "Neither"
                return "IPv6"
            return "Neither"
        except:
            return "Neither"