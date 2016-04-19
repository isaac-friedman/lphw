formatter = "%r %r %r %r"

#using the formatter for digits
print formatter %(1, 2, 3, 4)
#and now strings
print formatter %("one", "two", "three", "four")
#bools
print formatter %(True, False, True, False)
#And you can even put a formatter in a formatter!!
print formatter %(formatter, formatter, formatter, formatter)
#And song references
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
