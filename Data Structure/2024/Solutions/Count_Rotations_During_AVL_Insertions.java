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
    int LL=0,RR=0,LR=0,RL=0;
    
    int getHeight(AVLNode node){
        if(node==null) return 0;
        return node.height;
    }
    
    int getBalance(AVLNode node){
        if(node==null) return 0;
        return getHeight(node.left) - getHeight(node.right);
    }
    
    AVLNode rightRotate(AVLNode y){
        AVLNode x = y.left;
        AVLNode T2 = x.right;
        x.right = y;
        y.left = T2;
        y.height = Math.max(getHeight(y.left), getHeight(y.right)) + 1;
        x.height = Math.max(getHeight(x.left), getHeight(x.right)) + 1;
        return x;
    }
    
    AVLNode leftRotate(AVLNode x){
        AVLNode y = x.right;
        AVLNode T2 = y.left;
        y.left = x;
        x.right = T2;
        x.height = Math.max(getHeight(x.left), getHeight(x.right)) + 1;
        y.height = Math.max(getHeight(y.left), getHeight(y.right)) + 1;
        return y;
    }
    
    AVLNode insertNode(AVLNode root,int key){
        if(root==null) return new AVLNode(key);
        if(key < root.key)
            root.left = insertNode(root.left, key);
        else if(key > root.key)
            root.right = insertNode(root.right, key);
        else
            return root;
        
        root.height = 1 + Math.max(getHeight(root.left), getHeight(root.right));
        int balance = getBalance(root);
        
        if(balance > 1 && key < root.left.key){
            LL++;
            return rightRotate(root);
        }
        if(balance < -1 && key > root.right.key){
            RR++;
            return leftRotate(root);
        }
        if(balance > 1 && key > root.left.key){
            LR++;
            root.left = leftRotate(root.left);
            return rightRotate(root);
        }
        if(balance < -1 && key < root.right.key){
            RL++;
            root.right = rightRotate(root.right);
            return leftRotate(root);
        }
        return root;
    }
    
    int[] solveAVL(int[] arr){
        AVLNode root=null;
        for(int x:arr) root=insertNode(root,x);
        return new int[]{LL,RR,LR,RL};
    }
    
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0;i<n;i++) arr[i]=sc.nextInt();
        Solution sol=new Solution();
        int[] ans=sol.solveAVL(arr);
        System.out.println("LL: "+ans[0]);
        System.out.println("RR: "+ans[1]);
        System.out.println("LR: "+ans[2]);
        System.out.println("RL: "+ans[3]);
    }
}

