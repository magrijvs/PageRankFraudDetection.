import networkx as nx
import matplotlib.pyplot as plt
import scipy.sparse as sp

# Create a directed graph to represent transactions
G = nx.DiGraph()

# Add nodes for each account involved in the transactions
accounts = ["Alice", "Bruno", "Carlos", "Douglas", "Evandro", "Frederico", "Gustavo", "Henrique", "Isabela"]
G.add_nodes_from(accounts)

# Add edges to represent transactions between accounts
transactions = [("Alice", "Bruno", {"amount": 100}),
                ("Alice", "Carlos", {"amount": 200}),
                ("Bruno", "Carlos", {"amount": 50}),
                ("Carlos", "Douglas", {"amount": 500}),
                ("Douglas", "Evandro", {"amount": 1000}),
                ("Frederico", "Alice", {"amount": 300}),
                ("Evandro", "Frederico", {"amount": 400}),
                ("Gustavo", "Douglas", {"amount": 200}),
                ("Carlos", "Gustavo", {"amount": 100}),
                ("Frederico", "Gustavo", {"amount": 150}),
                ("Bruno", "Henrique", {"amount": 100}),
                ("Henrique", "Isabela", {"amount": 100}),
                ("Isabela", "Bruno", {"amount": 100})]
G.add_edges_from(transactions)

# Calculate the PageRank score for each account
pr = nx.pagerank(G)

# Find the account with the highest PageRank score
max_pr_account = max(pr, key=pr.get)

# Convert the PageRank scores to a sparse matrix
pr_sparse = sp.dok_matrix((1, len(accounts)))
for i, account in enumerate(accounts):
    pr_sparse[0, i] = pr[account]

# Visualize the PageRank scores using a bar chart, highlighting the account with the highest score
color_map = ["red" if account == max_pr_account else "blue" for account in accounts]
plt.bar(accounts, pr.values(), color=color_map)
plt.title("PageRank Scores")
plt.xlabel("Account")
plt.ylabel("Score")
plt.show()

# Plot the graph, highlighting the account with the highest score
pos = nx.spring_layout(G, k=0.5, iterations=50)
pos_labels = {account: (x, y+0.05) for account, (x, y) in pos.items()}
node_colors = ["red" if account == max_pr_account else "blue" for account in accounts]
nx.draw_networkx_nodes(G, pos, node_color=node_colors)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos_labels, labels={account: account for account in accounts}, font_size=12)
plt.show()
