chess =[
    [0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],
    [0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],
    [0,2],[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],
    [0,3],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],
    [0,4],[1,4],[2,4],[3,4],[4,4],[5,4],[6,4],[7,4],
    [0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],
    [0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6],[7,6],
    [0,7],[1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7]
]


first = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0]]
second = [[0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1]]
third = [[0,2],[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2]]
fourth = [[0,3],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3]]
fifth = [[0,4],[1,4],[2,4],[3,4],[4,4],[5,4],[6,4],[7,4]]
sixth = [[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5]]
seventh = [[0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6],[7,6]]
eigth = [[0,7],[1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7]]


print("\n\nThis is how a chess looks like:-\n")
print(eigth)
print(seventh)
print(sixth)
print(fifth)
print(fourth)
print(third)
print(second)
print(first)
print("\n\n")

start = chess.index([0,0]) 
destination = chess.index([7,7])

print("Let us suppose our pawn is at [0,0] then the shortest\npath to reach [7,7] will be jumping form\n[0,0] to [1,1] to \n[2,2] to [3,3] to \n[4,4] to [5,5] to \n[6,6] to finally [7,7]")
    

#1 Case: If the starting location is [0,0] then the shortest path will be jumping from [0,0] to [7,7] diagonally
start_location = [0,0]
print("\n")
print(start_location)
print("Jumping:")
for i in range(8):
    for j in range(8):
        jump = [0 + i, 0 + j] 
print(jump)
print("\n\n")
#2 case: If it finds a pawn on the way it will shift to the closest diagonal adjacent to then pawn and then follow it's predefined path of moving diagonally.
print("Let's suppose that the pawn encounters any\nother pawn at [4,4] on the way to [7,7] it will shift to\n[4,3] then diagonally to [5,4] then going up to [5,5]\nand then following the diagonal path to reach [7,7]. ")
