/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

import (
    "strings"
    "strconv"
)
type Codec struct {
    
}

func Constructor() Codec {
    return Codec{}
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
    var builder strings.Builder
    var preOrder func(*TreeNode)
    preOrder = func(node *TreeNode){
        if node == nil{
            builder.WriteString("N,")
            return
        } 
        builder.WriteString(strconv.Itoa(node.Val))
        builder.WriteString(",")
        preOrder(node.Left)
        preOrder(node.Right)

        return
    }

    preOrder(root)
    s := builder.String()
    // fmt.Println("serialized", s)
    return s
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {    
    index := 0
    stringSlice := strings.Split(data, ",")
    stringSlice = stringSlice[:len(stringSlice) - 1]
    
    var buildTree func() *TreeNode
    buildTree = func() *TreeNode{
        if stringSlice[index] == "N"{
            index++
            return nil
        }

        val, err := strconv.Atoi(stringSlice[index])
        if err != nil{
            panic(err)
        }
        root := &TreeNode{Val: val}
        index++
        root.Left = buildTree()
        root.Right = buildTree()
        return root
    }

    return buildTree()
}


/**
 * Your Codec object will be instantiated and called as such:
 * ser := Constructor();
 * deser := Constructor();
 * data := ser.serialize(root);
 * ans := deser.deserialize(data);
 */