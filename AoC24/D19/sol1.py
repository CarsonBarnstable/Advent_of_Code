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
        
        # empty line
        f.readline()
        
        # target designs
        for line in f.readlines():
            design = line.strip('\n')
            designs.append(design)
    
    # print(f"Towels:  {towels}\n\n")
    # print(f"Designs:  {designs}\n\n")

    valid_designs = 0

    for design in designs:
        if can_build_design(design, towels):
            valid_designs += 1
    
    print(f"The total number of Valid Designs is: {valid_designs}")
    print()
    


def can_build_design(target_design, available_pieces):
    """
    Checks if a target design can be built from available pieces, using each piece at most once.
    Uses recursion while matching starting sub-strings with available pieces
    """
    # if fully reduced
    if len(target_design) == 0:
        return True
    
    else:  # must try to match beginnings
        for matching_piece in available_pieces:
            # target's start *does match* the available piece
            if target_design.startswith(matching_piece):
                new_sub_design = target_design.replace(matching_piece, "", 1)  # only the first occurence
                remaining_pieces = [piece for piece in available_pieces if piece != matching_piece]  # need to make copy
                
                # resurse on sub-design
                if can_build_design(new_sub_design, remaining_pieces):
                    return True
                # continue
    
        # if nothing matches the beginning of the target design, cannot be built
        return False



if __name__ == "__main__":
    main()
