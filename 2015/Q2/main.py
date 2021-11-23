from math import prod


def get_area(lst):
    length = int(lst[0])
    width = int(lst[1])
    height = int(lst[2])
    sorted_dimensions = [length, width, height]
    sorted_dimensions.sort()

    # Calculate box Area and add extra slack
    area1 = 2 * length * width
    area2 = 2 * width * height
    area3 = 2 * height * length
    slack = sorted_dimensions[0] * sorted_dimensions[1]
    tot_area = area1 + area2 + area3 + slack

    return tot_area


def get_ribbon_length(lst):
    sorted_dimensions = [int(lst[0]), int(lst[1]), int(lst[2])]     # length x width x height
    sorted_dimensions.sort()

    ribbon = sorted_dimensions[0]*2 + sorted_dimensions[1]*2
    bow = prod(sorted_dimensions)

    return ribbon + bow


if __name__ == '__main__':
    area_for_boxes = 0
    ribbon_length = 0

    with open('dimensions.txt') as fp:
        lines = fp.readlines()
        for dim in lines:
            dimensions_lwh = dim.strip('\n').split('x')
            area_for_boxes += get_area(dimensions_lwh)
            ribbon_length += get_ribbon_length(dimensions_lwh)

    print("Ans Q2a::   Total amount of wrapping paper: {} sq/ft^2".format(area_for_boxes))
    print("Ans Q2b::   Total amount of ribbon length: {} ft".format(ribbon_length))
