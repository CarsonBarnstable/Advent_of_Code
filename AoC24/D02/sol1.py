def main():
    
    # get input
    reports = []
    with open("input.txt") as f:
        for line in f.readlines():
            row = line.strip('\n').split(" ")
            reports.append([int(num) for num in row])
    
    # count valid reports
    valid_counter = 0
    for report in reports:
        diffs = [report[i+1] - report[i] for i in range(len(report)-1)]

        if report[1] > report[0]:  # strictly increasing
            is_valid = all(diff >= 1 and diff <= 3 for diff in diffs)
        else:  # decreasing
            is_valid = all(diff <= -1 and diff >= -3 for diff in diffs)
        
        if is_valid:
            valid_counter += 1
    
    # result
    print(f"Number of Valid Reports: {valid_counter}")


if __name__ == "__main__":
    main()
