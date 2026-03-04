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
    var preOrder func(node *TreeNode) 
    var builder strings.Builder

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

    return builder.String()
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {   
    nodes := strings.Split(data, ",") 
    if len(nodes) == 0{
        return nil
    }
    index := 0
    var buildTree func() *TreeNode
    buildTree = func() *TreeNode{
        if index == len(nodes){
            return nil
        }
        if nodes[index] == "N"{
            index++
            return nil
        }

        nodeVal, err := strconv.Atoi(string(nodes[index]))
        if err != nil{
            panic(err)
        }
        index++
        root := &TreeNode{Val:nodeVal}
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