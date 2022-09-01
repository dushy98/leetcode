/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


int goodNodes(struct TreeNode* root){
    int count = 0;
    void dfs(struct TreeNode* node, int curMax){
        if (!node) return;
        
        if (node->val >= curMax){
            count++;
            curMax = node->val;
        }
        
        dfs(node->left, curMax);
        dfs(node->right, curMax);
    }
    
    dfs(root, root->val);
    return count;

}