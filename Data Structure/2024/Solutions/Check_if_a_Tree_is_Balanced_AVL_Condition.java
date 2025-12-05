import java.util.*;
class Node{ 
    int data; 
    Node left,right; 
    Node(int d){ 
        data=d; 
    }
}

class Solution{
    Node buildTree(int[] arr){
        if(arr.length==0 || arr[0]==-1) return null;
        Node root = new Node(arr[0]);
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i=1;
        while(!q.isEmpty() && i<arr.length){
            Node curr = q.poll();
            if(i<arr.length && arr[i]!=-1){
                curr.left = new Node(arr[i]);
                q.add(curr.left);
            }
            i++;
            if(i<arr.length && arr[i]!=-1){
                curr.right = new Node(arr[i]);
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }
    
    int getHeight(Node root){
        if(root==null) return 0;
        return 1 + Math.max(getHeight(root.left), getHeight(root.right));
    }
    
    boolean isBalanced(Node root){
        if(root==null) return true;
        int leftH = getHeight(root.left);
        int rightH = getHeight(root.right);
        int balance = leftH - rightH;
        if(balance < -1 || balance > 1) return false;
        return isBalanced(root.left) && isBalanced(root.right);
    }
    
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0;i<n;i++) arr[i]=sc.nextInt();
        Solution sol=new Solution();
        Node root=sol.buildTree(arr);
        System.out.println(sol.isBalanced(root)?"YES":"NO");
    }
}

