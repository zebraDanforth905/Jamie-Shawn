x=99
for i in range(x,0,-1):
    if i == 0:
        print(f"Take one down and pass it around, no more bottles of milk on the wall.")
        print(f"Go to the store and buy some more, 99 bottles of milk on the wall.")
        print(f"No more bottles of milk on the wall, no more bottles of milk.\nGo to the store and buy some more, 99 bottles of milk on the wall.")
    else:
        print(f"{i} bottles of milk on the wall, {i} bottles of milk.")
        print(f"Take one down and pass it along, {i-1} bottles of milk on the wall.")