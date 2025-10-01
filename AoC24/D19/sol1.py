def main():
    
    # get input
    towels = []
    designs = []

    with open("input.txt") as f:
        # available towels
        towel_list = f.readline().strip('\n')
        for towel in towel_list.split(','):
            towel = towel.strip(' ')
            towels.append(towel)
        
        # target designs
        for line in f.readlines():
            design = line.strip('\n')
            designs.append(design)
    
    print(f"Towels:  {towels}\n\n")
    print(f"Designs:  {designs}\n\n")
    


if __name__ == "__main__":
    main()
