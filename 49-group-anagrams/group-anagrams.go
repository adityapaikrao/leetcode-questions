type Config [26]int

func groupAnagrams(strs []string) [][]string {
    hmap := make(map[Config][]string, 0)

    for _, str := range strs{
        currConfig := Config{}
        for _, ch := range str{
            currConfig[int(ch) - int('a')]++
        }
        hmap[currConfig] = append(hmap[currConfig], str)
    }
    groupedAnagrams := [][]string{}
    for key := range hmap{
        groupedAnagrams = append(groupedAnagrams, hmap[key])
    }
    return groupedAnagrams
}