class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            temp = [str(ord(c)) for c in s]
            encoded_string += "_".join(temp) + " "
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == " ":
            return [""]
        decoded_strs = s.split()
        for i in range(len(decoded_strs)):
            temp = decoded_strs[i].split("_")
            decoded_strs[i] = ""
            for c in temp:
                decoded_strs[i] += chr(int(c))
        return decoded_strs