def common_part(section1, section2):
    return max(min(section1), min(section2)), min(max(section1), max(section2))

print(common_part((8, 4), (6, 2)))