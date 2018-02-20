from randomgraph import random_graph

def graph_iso(g1, g2):
    if len(g1) != len(g2):
        return False
    if sum(sum(x) for x in g1) != sum(sum(x) for x in g2):
        return False
    seq_deg_g1 = [sum(x) for x in g1]
    seq_deg_g2 = [sum(x) for x in g2]

    if sorted(seq_deg_g1) != sorted(seq_deg_g2):
        return False

    return True

if __name__=="__main__":
    g1 = random_graph(5)
    print(g1)
    g2 = random_graph(5)
    print(g2)
    isometry = graph_iso(g1, g2)

    print(isometry)
