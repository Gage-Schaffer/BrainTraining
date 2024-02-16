"""

Defanging an IP address
https://leetcode.com/problems/defanging-an-ip-address/description/

"""


def defangIPaddr(address: str) -> str:
    defanged_ip = address.replace(".", "[.]")
    return defanged_ip


ip_addr = "192.168.0.1"
print(defangIPaddr(ip_addr))

# Expected Output: 192[.]168[.]0[.]1
