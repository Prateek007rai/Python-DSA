# marker - a string pattern that is placed between a substring that is to be masked.
# plainText - the actual string containing substrings wrapped by markers that would need to be masked
# retainChars - the number of characters that should be retained on both ends of the substring upon masking.
# 
# Input:
# marker = "$$"
# plainText = "This String is Plain while this $$string here$$ will need to be $$masked$$."
# retainChars = 2
# Output: "This String is Plain while this st*******re will need to be ma**ed."

# Input:
# marker = "#$"
# plainText = "This String #$is#$ Plain while this #$string here#$ will need to be masked#$."
# retainChars = 2
# Output: "This String is Plain while this st*******re will need to be masked#$."


# Best approach - O(n)
def mask_pattern(marker, text, retain):
    res = ""                                      # final result string
    i = 0                                         # pointer for text

    while i < len(text):                          # loop through string

        start = text.find(marker, i)              # find opening marker
        # DRY RUN: first "$$" found at index 5

        if start == -1:
            res += text[i:]                       # add remaining text
            break

        res += text[i:start]                      # add normal text before marker
        # DRY RUN: "This " added

        end = text.find(marker, start + len(marker))  
        # DRY RUN: closing "$$" found after "string here"

        if end == -1:
            res += text[start:]                   # no closing marker
            break

        word = text[start + len(marker): end]     # extract content inside marker
        # DRY RUN: word = "string here"

        masked = marking(word, retain)            # mask it
        # DRY RUN: "st********re"

        if masked:
            res += masked                         # add masked text
        else:
            res += word                           # if too small, keep original

        i = end + len(marker)                     # move pointer after closing marker
        # DRY RUN: i jumps after "$$"

    return res


# for marking
def marking(text, retain):
    res =""
    if len(text) < 2*retain:
        return
    
    for i in range(len(text)):
        if retain <= i <= (len(text) - retain - 1):
            res = res + "*"
        else: 
            res = res + text[i]
    
    return res


print(mask_pattern("$$", "This String is Plain while this $$string here$$ will need to be $$masked$$.", 2))


print(mask_pattern("#$", "This String #$is#$ Plain while this #$string here#$ will need to be masked#$.", 2))
        

#-------------------------------------------------**************************------------------------------------------------------- 
        
           

#    Worst Case - O(n^2), normally - O(k*n)
def mask_pattern2(marker, text, retainChars):
    if marker not in text:                      # check if marker exists in text
        return text

    mark_text = []                              # store $$text$$ parts
    clip_text = False                           # flag to start/stop capturing
    short_text = ''                             # temp string to collect substring

    i = 0                                       # pointer

    while i < len(text):                        # traverse full string

        if text[i:i+len(marker)] == marker:     # check marker match
            if not clip_text:                   # opening marker
                clip_text = True
                short_text = marker             # start storing with marker
            else:                               # closing marker
                clip_text = False
                short_text += marker            # add closing marker
                mark_text.append(short_text)    # store complete $$text$$
                short_text = ''                 # reset

            i += len(marker)                    # skip marker length
            continue

        if clip_text:
            short_text += text[i]               # collect inner characters

        i += 1                                 # move forward

    # process each collected substring
    for i in mark_text:
        old_text_i = i                          # original $$text$$
        clean = i.replace(marker, '')           # remove markers

        output = marking(clean, retainChars)    # mask inner text

        if output is not None:
            text = text.replace(old_text_i, output)   # replace full segment (⚠️ O(n))

    return text

def marking2(text, retain):
    if len(text) < 2 * retain:
        return None                             # skip small strings

    res = ""

    for i in range(len(text)):
        if retain <= i <= (len(text) - retain - 1):
            res += "*"                          # mask middle part
        else:
            res += text[i]                      # keep first & last chars

    return res


print(mask_pattern2("$$", "This String is Plain while this $$string here$$ will need to be $$masked$$.", 2))

print(mask_pattern2("#$", "This String #$is#$ Plain while this #$string here#$ will need to be masked#$.", 2))
            