import java.util.*;
class RBNode{ 
    int key,color; 
    RBNode left,right,parent; 
    RBNode(int k){ 
        key=k; 
        color=0; 
    }
}

class Solution{
    RBNode leftRotate(RBNode root, RBNode x){
        if(x==null || x.right==null) return root;
        RBNode y = x.right;
        x.right = y.left;
        if(y.left != null) y.left.parent = x;
        y.parent = x.parent;
        if(x.parent == null) root = y;
        else if(x == x.parent.left) x.parent.left = y;
        else x.parent.right = y;
        y.left = x;
        x.parent = y;
        return root;
    }
    
    RBNode rightRotate(RBNode root, RBNode x){
        if(x==null || x.left==null) return root;
        RBNode y = x.left;
        x.left = y.right;
        if(y.right != null) y.right.parent = x;
        y.parent = x.parent;
        if(x.parent == null) root = y;
        else if(x == x.parent.right) x.parent.right = y;
        else x.parent.left = y;
        y.right = x;
        x.parent = y;
        return root;
    }
    
    RBNode fixInsert(RBNode root, RBNode node){
        while(node != root && node.parent != null && node.parent.color == 0){
            RBNode parent = node.parent;
            RBNode grandparent = parent.parent;
            if(grandparent == null) break;
            
            if(parent == grandparent.left){
                RBNode uncle = grandparent.right;
                if(uncle != null && uncle.color == 0){
                    parent.color = 1;
                    uncle.color = 1;
                    grandparent.color = 0;
                    node = grandparent;
                } else {
                    if(node == parent.right){
                        root = leftRotate(root, parent);
                        node = parent;
                        parent = node.parent;
                    }
                    parent.color = 1;
                    grandparent.color = 0;
                    root = rightRotate(root, grandparent);
                }
            } else {
                RBNode uncle = grandparent.left;
                if(uncle != null && uncle.color == 0){
                    parent.color = 1;
                    uncle.color = 1;
                    grandparent.color = 0;
                    node = grandparent;
                } else {
                    if(node == parent.left){
                        root = rightRotate(root, parent);
                        node = parent;
                        parent = node.parent;
                    }
                    parent.color = 1;
                    grandparent.color = 0;
                    root = leftRotate(root, grandparent);
                }
            }
        }
        root.color = 1;
        return root;
    }
    
    RBNode insertNode(RBNode root,int key){
        RBNode node = new RBNode(key);
        RBNode parent = null;
        RBNode current = root;
        
        while(current != null){
            parent = current;
            if(key < current.key) current = current.left;
            else current = current.right;
        }
        
        node.parent = parent;
        if(parent == null) root = node;
        else if(key < parent.key) parent.left = node;
        else parent.right = node;
        
        return fixInsert(root, node);
    }
    
    void inorder(RBNode root, ArrayList<Integer> list){
        if(root==null) return;
        inorder(root.left, list);
        list.add(root.key);
        inorder(root.right, list);
    }
    
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0;i<n;i++) arr[i]=sc.nextInt();
        Solution sol=new Solution();
        RBNode root=null;
        for(int x:arr) root=sol.insertNode(root,x);
        ArrayList<Integer> ans=new ArrayList<>();
        sol.inorder(root,ans);
        if(ans.size()==0) System.out.println("Tree is Empty");
        else{
            for(int i=0;i<ans.size();i++){
                System.out.print(ans.get(i));
                if(i<ans.size()-1) System.out.print(" ");
            }
        }
    }
}

