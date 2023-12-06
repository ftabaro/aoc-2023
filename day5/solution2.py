def main(path: str) -> int:
    """
    Day 5 solution to part 2

    From: https://www.reddit.com/r/adventofcode/comments/18b4b0r/comment/kc2v876
    """

    seeds, *maps = open(path).read().split("\n\n")
    seeds = [int(seed) for seed in seeds.split()[1:]]
    maps = [[list(map(int, line.split())) for line in m.splitlines()[1:]] for m in maps]

    locations = []
    
    for i in range(0, len(seeds), 2):
        
        # Calculate seed interval
        ranges = [[seeds[i], seeds[i + 1] + seeds[i]]]
        
        results = []
        for _map in maps:
            
            while ranges:
                
                start_range, end_range = ranges.pop()
                
                for target, start_map, r in _map:
                    
                    # Calculate end position
                    end_map = start_map + r
                    
                    # Calculate mapping offset
                    offset = target - start_map
                    
                    # 1. Map ends before range
                    # RANGE        |------|
                    # MAP   |----|
                    # 2. Map begins after range
                    # RANGE |------|
                    # MAP            |----|
                    if end_map <= start_range or end_range <= start_map:  
                        # No overlap
                        continue

                    # 3. Range starts before map
                    # RANGE  |------|
                    # MAP        |----|
                    if start_range < start_map:
                        # from start_range to star_map is already mapped
                        ranges.append([start_range, start_map])
                        
                        # the mapped portion starts at start map
                        start_range = start_map
                    
                    # 4. Range ends after map
                    # RANGE   |------|
                    # MAP      |----|
                    if end_map < end_range:
                        # from end_mat to end_range is already mapped
                        ranges.append([end_map, end_range])

                        # the mapped portion ends at end_map
                        end_range = end_map
                    
                    # Map range values
                    results.append([start_range + offset, end_range + offset])
                    break
                else:
                    # The range is not mapped
                    results.append([start_range, end_range])
            
            # Replace ranges with mapped ranges
            ranges = results
            results = []
        # Save last mapping results, the locations            
        locations += ranges
    
    # Calculate output
    return min(loc[0] for loc in locations)


if __name__ == "__main__":
    import sys

    res = main(sys.argv[1])
    print(res)
