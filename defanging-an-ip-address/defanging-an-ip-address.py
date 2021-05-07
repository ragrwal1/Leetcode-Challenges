class Solution:
    def defangIPaddr(self, address: str) -> str:
        g = address.split(".")
        s = "[.]"
        return s.join(g)
        