from Random_Graphs import *

def run():
    
    # Main menu
    # Directs the user to the method they want to use
    # by selecting a number

    print("Hello, welcome to Graphic Generator")
    print("Choose an generation method, please:")
    print("1.- Erdos-Rényi")
    print("2.- Gilbert")
    print("3.- Geographic")
    print("4.- Grid")
    print("5.- Barabasi-Albert")
    print("6.- Dorogovtev-Mendes")
    o = int(input())

    #Erdos-Renyi
    if o == 1:
        print("====== ERDOS-RENYI ======")
        name = input("Whats is your graph name?") # Obtaining data to create the graph
        n = int(input("How many nodes do you want?"))
        e = int(input("How many edges do you need?"))
        print("")
        g=randomErdos(n,e,False,False,name) # Call the method to create the graph
        print("Graph Nodes")
        g.printNodes() # Show graph data to verify results on console
        print("")
        print("Graph Edges")
        g.printEdges()
        g.toGVFormat() # Creating gv file

        print("")
        print("Do you want the graph search trees?")
        print("Enter y or n")
        a = str(input())
        if a == "y":
            print("")
            print("Wich is your root node:")
            s = str(input())
            gBFS = g.BFS(s)
            gDFSR = g.DFS_R(s)
            gDFSI = g.DFS_I(s)
            print("")
            print("BFS Tree Nodes")
            gBFS.printNodes()
            print("BFS Tree Edges")
            gBFS.printEdges()
            gBFS.toGVFormat()
            print("")
            print("DFS_R Tree Nodes")
            gDFSR.printNodes()
            print("DFS_R Tree Edges")
            gDFSR.printEdges()
            gDFSR.toGVFormat()
            print("")
            print("DFS_I Tree Nodes")
            gDFSI.printNodes()
            print("DFS_I Tree Edges")
            gDFSI.printEdges()
            gDFSI.toGVFormat()
            print("Cantidad de nodos BFS: " + str(len(gBFS.nodes)))
            print("Cantidad de nodos DFSR: " + str(len(gDFSR.nodes)))
            print("Cantidad de nodos DFSI: " + str(len(gDFSI.nodes)))

        print("")
        print("Do you want the random Dijkstra tree?")
        print("Enter y or n")
        a = str(input())
        if a == "y":
            print("")
            print("Wich is your root node:")
            s = str(input())
            g.addRandomWeights(1,100)
            g.toGVWeights()
            gDij = g.Dijkstra(str(s))
            gDij.printEdges()


    #Gilbert      
    elif o == 2:
        print("====== GILBERT ======")
        name = input("Whats is your graph name?")
        n = int(input("How many nodes do you want?"))
        p = float(input("What probability do you expect to create an edge?")) # Obtaining data to create the graph
        print("")
        if p <= 1 and p >= 0: # Valid probability check
            g=randomGilbert(n,p,False,False,name) # Call the method to create the graph
            print("")
            print("Graph Nodes")
            g.printNodes() # Show graph data to verify results on console
            print("")
            print("Graph Edges")
            g.printEdges()
            g.toGVFormat() # Creating gv file

            print("")
            print("Do you want the graph search trees?")
            print("Enter y or n")
            a = str(input())
            if a == "y":
                print("")
                print("Wich is your root node:")
                s = str(input())
                gBFS = g.BFS(s)
                gDFSR = g.DFS_R(s)
                gDFSI = g.DFS_I(s)
                print("")
                print("BFS Tree Nodes")
                gBFS.printNodes()
                print("BFS Tree Edges")
                gBFS.printEdges()
                gBFS.toGVFormat()
                print("")
                print("DFS_R Tree Nodes")
                gDFSR.printNodes()
                print("DFS_R Tree Edges")
                gDFSR.printEdges()
                gDFSR.toGVFormat()
                print("")
                print("DFS_I Tree Nodes")
                gDFSI.printNodes()
                print("DFS_I Tree Edges")
                gDFSI.printEdges()
                gDFSI.toGVFormat()
                print("Cantidad de nodos BFS: " + str(len(gBFS.nodes)))
                print("Cantidad de nodos DFSR: " + str(len(gDFSR.nodes)))
                print("Cantidad de nodos DFSI: " + str(len(gDFSI.nodes)))

        else:
            print("Select a valid probability value") 

        print("")
        print("Do you want the random Dijkstra tree?")
        print("Enter y or n")
        a = str(input())
        if a == "y":
            print("")
            print("Wich is your root node:")
            s = str(input())
            g.addRandomWeights(1,100)
            g.toGVWeights()
            gDij = g.Dijkstra(str(s))
            gDij.printEdges()  

    #Geographic
    elif o == 3:
        print("====== GEOGRAPHIC ======")
        name = input("Whats is your graph name?")
        n = int (input("How many nodes do you want?"))
        r = float (input("Choose a maximum distance less than 1"))
        print("")
        if r <= 1 and r > 0: # Valid distance check
            g=randomGeo(n,r,False,False,name)
            print("")
            print("Graph Nodes")
            g.printNodes()
            print("")
            print("Graph Edges")
            g.printEdges()
            g.toGVFormat()
            
            print("")
            print("Do you want the graph search trees?")
            print("Enter y or n")
            a = str(input())
            if a == "y":
                print("")
                print("Wich is your root node:")
                s = str(input())
                gBFS = g.BFS(s)
                gDFSR = g.DFS_R(s)
                gDFSI = g.DFS_I(s)
                print("")
                print("BFS Tree Nodes")
                gBFS.printNodes()
                print("BFS Tree Edges")
                gBFS.printEdges()
                gBFS.toGVFormat()
                print("")
                print("DFS_R Tree Nodes")
                gDFSR.printNodes()
                print("DFS_R Tree Edges")
                gDFSR.printEdges()
                gDFSR.toGVFormat()
                print("")
                print("DFS_I Tree Nodes")
                gDFSI.printNodes()
                print("DFS_I Tree Edges")
                gDFSI.printEdges()
                gDFSI.toGVFormat()
                print("Cantidad de nodos BFS: " + str(len(gBFS.nodes)))
                print("Cantidad de nodos DFSR: " + str(len(gDFSR.nodes)))
                print("Cantidad de nodos DFSI: " + str(len(gDFSI.nodes)))

        else:
            print("Select a valid distance")

        print("")
        print("Do you want the random Dijkstra tree?")
        print("Enter y or n")
        a = str(input())
        if a == "y":
            print("")
            print("Wich is your root node:")
            s = str(input())
            g.addRandomWeights(1,100)
            g.toGVWeights()
            gDij = g.Dijkstra(str(s))
            gDij.printEdges()

    #Grid       
    elif o == 4:
        print("====== GRID ======")
        name = input("Whats is your graph name?")
        m = int (input("How many columns do you want?"))
        n = int (input("How many files do you want?"))
        print("")
        if m >= 1 and n >= 0: # Valid colomns and files check
            g=randomGrid(m,n,False,False,False,name)
            print("")
            print("Graph Nodes")
            g.printNodes()
            print("")
            print("Graph Edges")
            g.printEdges()
            g.toGVFormat()

            print("")
            print("Do you want the graph search trees?")
            print("Enter y or n")
            a = str(input())
            if a == "y":
                print("")
                print("Wich is your root node:")
                s = str(input())
                gBFS = g.BFS(s)
                gDFSR = g.DFS_R(s)
                gDFSI = g.DFS_I(s)
                print("")
                print("BFS Tree Nodes")
                gBFS.printNodes()
                print("BFS Tree Edges")
                gBFS.printEdges()
                gBFS.toGVFormat()
                print("")
                print("DFS_R Tree Nodes")
                gDFSR.printNodes()
                print("DFS_R Tree Edges")
                gDFSR.printEdges()
                gDFSR.toGVFormat()
                print("")
                print("DFS_I Tree Nodes")
                gDFSI.printNodes()
                print("DFS_I Tree Edges")
                gDFSI.printEdges()
                gDFSI.toGVFormat()
                print("Cantidad de nodos BFS: " + str(len(gBFS.nodes)))
                print("Cantidad de nodos DFSR: " + str(len(gDFSR.nodes)))
                print("Cantidad de nodos DFSI: " + str(len(gDFSI.nodes)))

        else:
            print("Select a valid number of columns or files")

        print("")
        print("Do you want the random Dijkstra tree?")
        print("Enter y or n")
        a = str(input())
        if a == "y":
            print("")
            print("Wich is your root node:")
            s = str(input())
            g.addRandomWeights(1,100)
            g.toGVWeights()
            gDij = g.Dijkstra(str(s))
            gDij.printEdges()

    #Barabasi-Albert
    elif o == 5:
        print("====== BARABASI-ALBERT ======")
        name = input("Whats is your graph name?")
        n = int (input("How many nodes do you want?"))
        d = int (input("Whats the maximum degree possible per node?"))
        print("")
        g=randomBarabasi(n,d,False,False,name)
        print("")
        print("Graph Nodes")
        g.printNodes()
        print("")
        print("Graph Edges")
        g.printEdges()
        g.toGVFormat()

        print("")
        print("Do you want the graph search trees?")
        print("Enter y or n")
        a = str(input())
        if a == "y":
            print("")
            print("Wich is your root node:")
            s = str(input())
            gBFS = g.BFS(s)
            gDFSR = g.DFS_R(s)
            gDFSI = g.DFS_I(s)
            print("")
            print("BFS Tree Nodes")
            gBFS.printNodes()
            print("BFS Tree Edges")
            gBFS.printEdges()
            gBFS.toGVFormat()
            print("")
            print("DFS_R Tree Nodes")
            gDFSR.printNodes()
            print("DFS_R Tree Edges")
            gDFSR.printEdges()
            gDFSR.toGVFormat()
            print("")
            print("DFS_I Tree Nodes")
            gDFSI.printNodes()
            print("DFS_I Tree Edges")
            gDFSI.printEdges()
            gDFSI.toGVFormat()
            print("Cantidad de nodos BFS: " + str(len(gBFS.nodes)))
            print("Cantidad de nodos DFSR: " + str(len(gDFSR.nodes)))
            print("Cantidad de nodos DFSI: " + str(len(gDFSI.nodes)))

        print("")
        print("Do you want the random Dijkstra tree?")
        print("Enter y or n")
        a = str(input())
        if a == "y":
            print("")
            print("Wich is your root node:")
            s = str(input())
            g.addRandomWeights(1,100)
            g.toGVWeights()
            gDij = g.Dijkstra(str(s))
            gDij.printEdges()

    #Dorogotev-Mendes     
    elif o == 6:
        print("====== DOROGOVTEV-MENDES ======")
        name = input("Whats is your graph name?")
        n = int (input("How many nodes do you want?"))
        print("")
        g=randomDoroMendes(n,False,False,name)
        print("")
        print("Graph Nodes")
        g.printNodes()
        print("")
        print("Graph Edges")
        g.printEdges()
        g.toGVFormat()
        print("")
        print("Do you want the graph search trees?")
        print("Enter y or n")
        a = str(input())
        if a == "y":
            print("")
            print("Wich is your root node:")
            s = str(input())
            gBFS = g.BFS(s)
            gDFSR = g.DFS_R(s)
            gDFSI = g.DFS_I(s)
            print("")
            print("BFS Tree Nodes")
            gBFS.printNodes()
            print("BFS Tree Edges")
            gBFS.printEdges()
            gBFS.toGVFormat()
            print("")
            print("DFS_R Tree Nodes")
            gDFSR.printNodes()
            print("DFS_R Tree Edges")
            gDFSR.printEdges()
            gDFSR.toGVFormat()
            print("")
            print("DFS_I Tree Nodes")
            gDFSI.printNodes()
            print("DFS_I Tree Edges")
            gDFSI.printEdges()
            gDFSI.toGVFormat()
            print("Cantidad de nodos BFS: " + str(len(gBFS.nodes)))
            print("Cantidad de nodos DFSR: " + str(len(gDFSR.nodes)))
            print("Cantidad de nodos DFSI: " + str(len(gDFSI.nodes)))

        print("")
        print("Do you want the random Dijkstra tree?")
        print("Enter y or n")
        a = str(input())
        if a == "y":
            print("")
            print("Wich is your root node:")
            s = str(input())
            g.addRandomWeights(1,100)
            g.toGVWeights()
            gDij = g.Dijkstra(str(s))
            gDij.printEdges()


    else:
        print("Pick a valid option please")
    

if __name__ == '__main__':
    run()