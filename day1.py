"""
https://adventofcode.com/2022/day/1
"""
import helpers.file_reader

day = 1


def main():
    lines = helpers.file_reader.read_file_get_lines(day=day)

    elves = []
    calorie_sum = 0
    max_cals = 0
    for line in lines:
        line = line.strip('\n')
        if line == '':
            elves.append(calorie_sum)
            if calorie_sum > max_cals:
                max_cals = calorie_sum
                calorie_sum = 0
                continue
            else:
                calorie_sum = 0
                continue
        calorie_sum += int(line)
    print('Max is ' + str(max_cals))
    elves.sort()
    print(elves)
    print('Top 3 total: ', (elves[len(elves) - 1] + elves[len(elves) - 2] + elves[len(elves) - 3]))


if __name__ == "__main__":
    main()
