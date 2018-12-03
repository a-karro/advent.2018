import re


pattern = re.compile(r'#(\d*) @ (\d*),(\d*): (\d*)x(\d*)')
rectangles = list()


with open('data/day3_1.txt') as f:
    for rectangle in f:
        for (num, x, y, w, h) in re.findall(pattern, rectangle):
            rectangles.append({'num': num, 'sx': int(x) + 1, 'sy': int(y) + 1,
                               'ex': int(x) + int(w), 'ey': int(y) + int(h)})


def day3_1(rect_list):
    rect_list = sorted(rect_list, key=lambda k: k['sx'])
    end_x = max([rect['ex'] for rect in rect_list]) + 1
    start_x = rect_list[0]['sx']

    overlapped = 0

    for i in range(start_x, end_x):
        column = dict()
        processed = list()
        for r in rect_list:
            if r['sx'] > i:
                break
            if r['ex'] < i:
                processed.append(r)
            if r['sx'] <= i <= r['ex']:
                for cy in range(r['sy'], r['ey'] + 1):
                    column[cy] = column.get(cy, 0) + 1
        for del_this in processed:
            rect_list.remove(del_this)
        overlapped = overlapped + len([key for key, value in column.iteritems() if value > 1])

    return overlapped


def does_overlap(a, b):
    return not (a['sx'] > b['ex'] or b['sx'] > a['ex'] or a['sy'] > b['ey'] or b['sy'] > a['ey'])


def day3_2(rect_list):
    for i in range(len(rect_list)-1):
        for k in range(i + 1, len(rect_list)):
            if does_overlap(rect_list[i], rect_list[k]):
                rect_list[i]['overlaps'] = 1
                rect_list[k]['overlaps'] = 1
    return [rect['num'] for rect in rect_list if rect.get('overlaps', 0) == 0]


print day3_1(rectangles)
print day3_2(rectangles)
