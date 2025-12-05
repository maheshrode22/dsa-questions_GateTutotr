import java.util.*;
class AVLNode{ 
    int key,height; 
    AVLNode left,right; 
    AVLNode(int k){ 
        key=k; 
        height=1; 
    } 
}

class Solution{
    AVLNode insertNode(AVLNode root, int key){
        if(root==null) return new AVLNode(key);
        return root;
    }
    
    int solveAVL(int x){
        AVLNode root = insertNode(null, x);
        return root.height;
    }
    
    public static void main(String[] args)throws Exception{
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        Solution sol=new Solution();
        System.out.println("height: "+sol.solveAVL(x));
    }
}

