import re
print sum([int(v) for v in re.findall('\D*(\d+)\D+?', open('regex_sum_202730.txt').read())])
