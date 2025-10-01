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
    total_variations = 0
    known_patterns = {}

    for design in designs:
        if can_build_design(design, towels):
            valid_designs += 1

            # only count possible arrangements
            total_variations += num_valid_designs(design, towels, known_patterns)
        
    
    # print(f"The total number of Valid Designs is: {valid_designs}")
    # print()
    print(f"The total number of Possible Arrangements is: {total_variations}")
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
                
                # resurse on sub-design
                if can_build_design(new_sub_design, available_pieces):
                    return True
                # continue
    
        # if nothing matches the beginning of the target design, cannot be built
        return False


def num_valid_designs(target_design, available_pieces, memo):
    """
    Counts how many target designs can be built from available pieces, using each piece at most once.
    Uses recursion while matching starting sub-strings with available pieces
    """

    # if we've seen the sub-design, we know how many arrangements it took last time
    if memo and target_design in memo.keys():
        return memo.get(target_design)

    # if fully reduced, have found one valid variation
    if len(target_design) == 0:
        return 1
    
    else:  # must try to match beginnings
        variation_counter = 0
        for matching_piece in available_pieces:
            # target's start *does match* the available piece
            if target_design.startswith(matching_piece):
                new_sub_design = target_design.replace(matching_piece, "", 1)  # only the first occurence
                
                # resurse on sub-design
                valid_variations = num_valid_designs(new_sub_design, available_pieces, memo)
                variation_counter += valid_variations

                if new_sub_design not in memo.keys():
                    memo[new_sub_design] = valid_variations
                # continue
        
        # we have counted all the possible variations from the current state
        return variation_counter



if __name__ == "__main__":
    main()
