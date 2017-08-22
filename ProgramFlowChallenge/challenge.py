ipAddress = input("Please enter an IP address: ")
if ipAddress[-1] != '.':
    ipAddress += '.'

segment = 1
segment_length = 0
# character = ''


for character in ipAddress:
    if character == '.':
        print("Segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

# unless the final character in the string was a . then we haven't printed the last segment
# if character != '.':
#     print("Segment {} contains {} characters".format(segment, segment_length))
