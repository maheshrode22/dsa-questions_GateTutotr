import java.util.*;
class Node{ 
    int data; 
    Node left,right; 
    Node(int d){ 
        data=d; 
    }
}

class Solution{
    Node buildAVL(int[] arr,int l,int r){
        if(l > r) return null;
        int mid = (l + r) / 2;
        Node root = new Node(arr[mid]);
        root.left = buildAVL(arr, l, mid-1);
        root.right = buildAVL(arr, mid+1, r);
        return root;
    }
    
    void preorder(Node root,ArrayList<Integer> list){
        if(root==null) return;
        list.add(root.data);
        preorder(root.left, list);
        preorder(root.right, list);
    }
    
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0;i<n;i++) arr[i]=sc.nextInt();
        Solution sol=new Solution();
        Node root=sol.buildAVL(arr,0,n-1);
        ArrayList<Integer> ans=new ArrayList<>();
        sol.preorder(root,ans);
        if(ans.size()==0) System.out.println("Tree is Empty");
        else{
            for(int i=0;i<ans.size();i++){
                System.out.print(ans.get(i));
                if(i<ans.size()-1) System.out.print(" ");
            }
        }
    }
}

