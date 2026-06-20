import re
import readline

try:
	with open("dict.csv", 'r') as f:
		cur_set = [x.strip().lower() for x in f.readlines()]
except Exception:
	cur_set = []
cur_prompt = "(%d)>" % len(cur_set)
cur_char_class = '\\w'
stack = []

while True:
	line = input(cur_prompt)

	try:
		cmd, arg = line.split(' ', maxsplit=1)
	except ValueError:
		cmd = line
		arg = ""

	# The following group of commands pre-process the arg and pass it to "r"
	if cmd == "rs": # Arg is intended to start the word with _* trailing
		arg = "^%s_*$" % arg
		cmd = "r"
	if cmd == "re":
		arg = "^_*%s$" % arg
		cmd = "r"
	if cmd == "rw": # Wrap re with _* on both ends
		arg = "^_*%s_*$" % arg
		cmd = "r"
	if cmd == "rx": # x for exact. Puts ^ an $ around the re
		arg = "^%s$" % arg
		cmd = "r"
	# The "r" command filters the current set by the regular expression provided in arg
	# It saves the current state on the stack so you can build complicated searches one part at a time
	if cmd == "r": # Filter the cur_set according to the regular expression in arg
		stack.append((cur_set, cur_prompt)) # Save the state on the stack
		arg = arg.replace('_', "[%s]" % cur_char_class) # Pre process the arg
		exp = re.compile(arg)
		cur_set = sorted(list(filter(exp.match, cur_set)), key=len)
		cur_prompt = cur_prompt + "%s(%d)>" % (arg, len(cur_set))

	if cmd == "b": # Go back to the most recent state
		if len(stack) > 0:
			cur_set, cur_prompt = stack.pop()

	if cmd == "p": # Print set
		for i in cur_set:
			print(i)

	if cmd == "l": # Reset state and load arg as cur_set, one item per line.
		if not arg:
			print("Usage: l <filename>")
			continue
		with open(arg, 'r') as f:
			cur_set = [x.strip().lower() for x in f.readlines()]
		cur_prompt = "(%d)>" % len(cur_set)
		stack = []

	# Anytime the character "_" appears in a re, it is replaced with a canned string
	# Helpful for saving a character class like [aeiou] or one representing your available
	# letters. Which is a common wildcard used in this tool.
	if cmd == "_": # Set char class
		if arg:
			cur_char_class = arg
		else:
			print(cur_char_class)

	if cmd == "?":
		print("Commands:")
		print("  r <regex> - Raw regex. '_' is replaced with the tile set.")
		print("    rs <regex> - \"Starts with\" -> ^regex_*$")
		print("    re <regex> - \"Ends with\" -> ^_*regex$")
		print("    rw <regex> - \"Wrap\" -> ^_*regex_*$")
		print("    rx <regex> - \"Exact\" -> ^regex$")
		print("  b - Go back to the most recent state")
		print("  p - Print set")
		print("  l <filename> - Load a dictionary file.")
		print("  _ [chars] - Print / reset tile set")
		print("  ? - Print this help message")
		print("  q - Quit")

	if cmd == "q":
		break
