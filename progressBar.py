# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    pass
else:
    pass

# =============================================================================


# data una percentuale restituisce una stringa corrispondente alla barra di caricamento
def progressBar(percentage: int, size=1):
	progressCharacter = "#"

	progress = int((percentage/10))

	bar = "["
	for i in range(0,10):
		if(i <= (progress - 1)):
			bar += (progressCharacter * (size))
		else:			
			bar += (" " * (size))

	bar += "]"
	return bar

# converte una frazione in una percentuale
def ratioToPercentage(a: int, b: int):
	return int((a/b) * 100)

# converte una frazione in una progressBar
def ratioToProgressBar(a: int, b: int,size=1):
	perc = ratioToPercentage(a,b)
	return progressBar(perc,size)

# mostra in una stringa la progressBar e la percentuale
def percentageAndProgressBar(a: int, b: int, size=1):
	return str(ratioToProgressBar(a,b,size) + " " + str(ratioToPercentage(a,b)) + "%")