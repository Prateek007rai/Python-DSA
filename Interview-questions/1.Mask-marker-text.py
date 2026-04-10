# marker - a string pattern that is placed between a substring that is to be masked.
# plainText - the actual string containing substrings wrapped by markers that would need to be masked
# retainChars - the number of characters that should be retained on both ends of the substring upon masking.
# 
# Input:
# marker = "$$"
# plainText = "This String is Plain while this $$string here$$ will need to
# be $$masked$$."
# retainChars = 2
# Output:
# "This String is Plain while this st*******re will need to be ma**ed."

# Input:
# marker = "#$"
# plainText = "This String #$is#$ Plain while this #$string here#$ will need
# to be masked#$."
# retainChars = 2
# Output:
# "This String is Plain while this st*******re will need to be masked#$."