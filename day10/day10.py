
## read file
with open('input') as f:
    lines = f.readlines()

## For each line, take a character at a time.
## If it's an "open" character add it to a list or double ended queue (deque)
## If it's a "close" character, check that the last one added to the deque
## is its partner.

opening_chars = {"(","[","{","<"}
closing_chars = {")","]","}",">"}
partner_char = {")" : "(", "]" : "[", "}" : "{", ">" : "<", "(" : ")", "[" : "]", "{" : "}", "<" : ">"}
completion_scores = {")" : 1, "]" : 2, "}" : 3, ">" : 4}
score_list = []

def process_line(this_line):
    openings = []
    for char in this_line:
        if char in opening_chars:
            #print("char",char,"is in opening_chars")
            openings.append(char)
            #print("appending to openings")
            #print("openings:",openings)
            #x = input()
        if char in closing_chars:
            lastopening = openings.pop(-1)
            expectedopening = partner_char[char]
            expectedclosing = partner_char[lastopening]
            if expectedopening != lastopening:
                outcome = ["error", expectedclosing, char]
                return outcome
    if len(openings) > 0: ## incomplete
        print("--- incomplete --- ")
        print("remaining openings: ", openings)
        score_count = 0
        total_score = 0
        while len(openings) > 0:
            total_score = (5 * total_score) + completion_scores[partner_char[openings.pop(-1)]]
        score_list.append(total_score)
        return ["incomplete",0,0]
    if len(openings) == 0: return ["success",0,0]


def process_file():
    points = {")" : 3, "]" : 57, "}" : 1197, ">" : 25137}
    total_score = 0
    for l in lines:
        result = process_line(l)
        if result[0] == "error":
            #print("illegal char:", result[2], "points for that:",points[result[2]])
            total_score += points[result[2]]
    return total_score
        #x = input()



total_score = process_file()
print(f"------------\nTotal score is: {total_score}")
print(f"------------\nScore list is: {score_list}")
score_list.sort()
print("Middle score is:",score_list[int((len(score_list)-1)/2)])
######################## ## Part 2 ## ########################
