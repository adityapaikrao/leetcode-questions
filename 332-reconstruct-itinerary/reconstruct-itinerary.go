import (
    "slices"
)


func dfs(node string, outDegree map[string]int, adj map[string]map[string]int, postOrder *[]string){
    // recruse until no nbrs
    if outDegree[node] == 0{
        *postOrder = append(*postOrder, node)
        return
    }
    
    // sort nbrs to search in lexical order
    nbrs := make([]string, 0, len(adj[node]))
    for nbrKey := range adj[node]{
        if adj[node][nbrKey] != 0{
            nbrs = append(nbrs, nbrKey)
        }
    }

    slices.Sort(nbrs)

    for _, nbrKey := range nbrs{
        if adj[node][nbrKey] != 0 {
            adj[node][nbrKey]-- // reduce count
            outDegree[node]-- // reduce outdegree

            dfs(nbrKey, outDegree, adj, postOrder)
        }
    }

    *postOrder = append(*postOrder, node)
    return
}

func findItinerary(tickets [][]string) []string {
    // create adjacency list & outDegree list
    outDegree := make(map[string]int, 0)
    adj := make(map[string]map[string]int, 0) // node -> {nbr:count}
    for _, ticket := range tickets{
        if adj[ticket[0]] == nil{
            adj[ticket[0]] = make(map[string]int, 0)
        }
        adj[ticket[0]][ticket[1]]++
        outDegree[ticket[0]]++
    }

    // skip check since guaranteed at least one eulerian path with startNode JFK
    postOrder := make([]string, 0)
    dfs("JFK", outDegree, adj, &postOrder)

    // reverse post order traversal is the visit order
    slices.Reverse(postOrder)

    return postOrder

}