func isInterleave(s1 string, s2 string, s3 string) bool {
    if len(s3) != len(s1)+len(s2) {
        return false
    }

    prev := make([]bool, len(s2) + 1)
    for j := range len(s2) + 1{
        if s2[j:] == s3[j + len(s1):]{
            prev[j] = true
        }
    }


    for i := len(s1) - 1; i >= 0; i--{
        curr := make([]bool, len(s2) + 1)
        curr[len(s2)] = (s1[i:] == s3[i + len(s2): ])

        for j := len(s2) - 1; j >= 0; j--{
            if s1[i] == s3[i + j]{
                curr[j] = curr[j] || prev[j]
            }
            if s2[j] == s3[i + j]{
                curr[j] = curr[j] || curr[j + 1]
            }
        }

        copy(prev, curr)
    }

    return prev[0]
}

