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
        
        if(balance > 1 && key < root.left.key)
            return rightRotate(root);
        if(balance < -1 && key > root.right.key)
            return leftRotate(root);
        if(balance > 1 && key > root.left.key){
            root.left = leftRotate(root.left);
            return rightRotate(root);
        }
        if(balance < -1 && key < root.right.key){
            root.right = rightRotate(root.right);
            return leftRotate(root);
        }
        return root;
    }
    
    AVLNode minValueNode(AVLNode node){
        AVLNode current = node;
        while(current.left != null)
            current = current.left;
        return current;
    }
    
    AVLNode deleteNode(AVLNode root,int key){
        if(root==null) return null;
        if(key < root.key)
            root.left = deleteNode(root.left, key);
        else if(key > root.key)
            root.right = deleteNode(root.right, key);
        else{
            if(root.left==null){
                AVLNode temp = root.right;
                root = null;
                return temp;
            }
            if(root.right==null){
                AVLNode temp = root.left;
                root = null;
                return temp;
            }
            AVLNode temp = minValueNode(root.right);
            root.key = temp.key;
            root.right = deleteNode(root.right, temp.key);
        }
        
        if(root==null) return null;
        
        root.height = 1 + Math.max(getHeight(root.left), getHeight(root.right));
        int balance = getBalance(root);
        
        if(balance > 1 && getBalance(root.left) >= 0)
            return rightRotate(root);
        if(balance > 1 && getBalance(root.left) < 0){
            root.left = leftRotate(root.left);
            return rightRotate(root);
        }
        if(balance < -1 && getBalance(root.right) <= 0)
            return leftRotate(root);
        if(balance < -1 && getBalance(root.right) > 0){
            root.right = rightRotate(root.right);
            return leftRotate(root);
        }
        return root;
    }
    
    void preorder(AVLNode root,ArrayList<Integer> list){
        if(root==null) return;
        list.add(root.key);
        preorder(root.left, list);
        preorder(root.right, list);
    }
    
    ArrayList<Integer> solveAVL(int[] arr,int x){
        AVLNode root = null;
        for(int v : arr) root = insertNode(root, v);
        root = deleteNode(root, x);
        ArrayList<Integer> ans = new ArrayList<>();
        preorder(root, ans);
        return ans;
    }
    
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0;i<n;i++) arr[i]=sc.nextInt();
        int x=sc.nextInt();
        Solution sol=new Solution();
        ArrayList<Integer> ans=sol.solveAVL(arr,x);
        if(ans.size()==0) System.out.println("Tree is Empty");
        else{
            for(int i=0;i<ans.size();i++){
                System.out.print(ans.get(i));
                if(i<ans.size()-1) System.out.print(" ");
            }
        }
    }
}

