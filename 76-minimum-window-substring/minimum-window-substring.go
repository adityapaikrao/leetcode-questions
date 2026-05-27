/*
A D O B E C O D E B A N C
  i    
          j
{A:1, B:1, C:1}

A B C 
{A:1, B:1, C:1}


when valid window found: 
    - prune from front until it stays valid & capture min length

window found? 
    -> check everytime a new char is added? O(26)
    -> 
*/


func minWindow(s string, t string) string {
    if len(t) > len(s) {return ""}

    n, m := len(s), len(t)
    tFreq := make(map[byte]int, m)
    for _, char := range t {
        tFreq[byte(char)]++
    }
    count := len(tFreq)

    i, j := 0, 0
    start, end := -1, n

    for j < n {
        if _, ok := tFreq[s[j]]; ok{
            tFreq[s[j]]--
            if tFreq[s[j]] == 0 {count--}
        }

        if count > 0 { 
            j++
            continue
        }

        // fmt.Println(i, j)
        for count == 0 {
            if _, ok := tFreq[s[i]]; ok {
                tFreq[s[i]]++
                if tFreq[s[i]] > 0 {count++}
            }
            i++
        }

        if j - i  + 1 < end - start + 1 {
            start = i - 1
            end = j
        } 
        j++
    }

    if start == -1 {return ""}

    return s[start: end + 1]

}