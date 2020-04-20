from operator import methodcaller

humpty_dumpty = [
	"  Humpty Dumpty sat on a wall,  ",
	"Humpty Dumpty had a great fall;     ",
	"  All the king's horses and all the king's men ",  
	"    Couldn't put Humpty together again."
]

# clean  =  map(lambda line:line.strip(), humpty_dumpty)
clean  =  map(methodcaller('strip'), humpty_dumpty)


print(*clean,sep=' ')