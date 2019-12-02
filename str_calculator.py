import re
def add(args) :
    args = ("")
    num = []
    if len(args)== 0 :
        return 0

    try:
        int(args[-1])
    except :
        return "Not ok"

 for alpha in re.findall(r"-?\d+",args):
     try:
        if int(alpha) > 1000 :
                alpha = 0
            if int(alpha) < 0 :
                num.append(alpha)
                list_num.append(int(alpha))
        except:
            continue
            
    if len(num) > 0:
        raise Exception('negatives not allowed: {}'.format(num))

    return sum(args)
