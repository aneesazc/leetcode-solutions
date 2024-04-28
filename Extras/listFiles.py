def list_files(current_node, current_path=""):
    res = []
    
    def helper(node, path):
        # Iterate over the dictionary keys
        for key, value in node.items():
            # Build the path
            new_path = f"{path}/{key}"
            # If the value is None, it's a file, add to results
            if value is None:
                res.append(new_path)
            else:
                # If it's a nested dictionary, recurse deeper
                helper(value, new_path)

    # Start the recursion with the root node and an empty path
    helper(current_node, "")
    
    return res

# Inputs:

#  * current_node: {'Documents': {'Proposal.docx': None, 'Report': {'AnnualReport.pdf': None, 'Financials.xlsx': None}}, 'Downloads': {'picture1.jpg': None, 'picture2.jpg': None}}
