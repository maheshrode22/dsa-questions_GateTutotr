import java.util.*;
class Node{ 
    int key; 
    Node left,right; 
    Node(int k){ 
        key=k; 
    }
}

class Solution{
    Node leftRotate(Node x){
        if(x==null || x.right==null) return x;
        Node y = x.right;
        x.right = y.left;
        y.left = x;
        return y;
    }
    
    int solveAVL(int a,int b){
        Node root = new Node(a);
        root.right = new Node(b);
        root = leftRotate(root);
        return root.key;
    }
    
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        Solution sol=new Solution();
        System.out.println("root: "+sol.solveAVL(a,b));
    }
}

