import java.util.*;
class Node{ 
    int data; 
    char color; 
    Node left,right; 
    Node(int d,char c){ 
        data=d;
        color=c; 
    }
}

class Solution{
    Node buildTree(String[] arr){
        if(arr.length==0 || arr[0].equals("-1")) return null;
        Map<Integer, Node> map = new HashMap<>();
        Node root = null;
        Queue<Node> q = new LinkedList<>();
        int i=0;
        if(i<arr.length && !arr[i].equals("-1")){
            String[] parts = arr[i].split(":");
            int val = Integer.parseInt(parts[0]);
            char col = parts[1].charAt(0);
            root = new Node(val, col);
            q.add(root);
            map.put(0, root);
        }
        i++;
        while(!q.isEmpty() && i<arr.length){
            Node curr = q.poll();
            if(i<arr.length && !arr[i].equals("-1")){
                String[] parts = arr[i].split(":");
                int val = Integer.parseInt(parts[0]);
                char col = parts[1].charAt(0);
                curr.left = new Node(val, col);
                q.add(curr.left);
            }
            i++;
            if(i<arr.length && !arr[i].equals("-1")){
                String[] parts = arr[i].split(":");
                int val = Integer.parseInt(parts[0]);
                char col = parts[1].charAt(0);
                curr.right = new Node(val, col);
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }
    
    boolean checkRootBlack(Node root){
        return root==null || root.color=='B';
    }
    
    boolean checkNoRedRed(Node root){
        if(root==null) return true;
        if(root.color=='R'){
            if(root.left!=null && root.left.color=='R') return false;
            if(root.right!=null && root.right.color=='R') return false;
        }
        return checkNoRedRed(root.left) && checkNoRedRed(root.right);
    }
    
    int getBlackHeight(Node root){
        if(root==null) return 1;
        int leftBH = getBlackHeight(root.left);
        int rightBH = getBlackHeight(root.right);
        if(leftBH==-1 || rightBH==-1 || leftBH!=rightBH) return -1;
        return leftBH + (root.color=='B' ? 1 : 0);
    }
    
    boolean validateProperties(Node root){
        if(root==null) return true;
        if(!checkRootBlack(root)) return false;
        if(!checkNoRedRed(root)) return false;
        return getBlackHeight(root) != -1;
    }
    
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(); 
        sc.nextLine();
        String[] arr=sc.nextLine().split(" ");
        Solution sol=new Solution();
        Node root=sol.buildTree(arr);
        System.out.println(sol.validateProperties(root)?"YES":"NO");
    }
}

