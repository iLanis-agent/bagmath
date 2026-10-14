import json, math

def num(x): return isinstance(x,(int,float)) and math.isfinite(x)
def pos(x): return num(x) and x>0
def jround(x): return math.floor(x+0.5)
def jsnum(x):
    if isinstance(x,float) and x==int(x): return str(int(x))
    return str(x)
def r1(x): return jround(x*10)/10

def comfort_plan(rating):
    if not num(rating): return {"error":"the rating must be a number"}
    return {"warm":r1(rating+15),"cold":r1(rating+25)}

def render_comfort(r,rating):
    return ("Your "+jsnum(rating)+" F sticker plans comfort at "+jsnum(r["warm"])+" F for a warm sleeper and "
            +jsnum(r["cold"])+" F for a cold one - the sticker is a lower-limit number, not a promise.")

def pad_plan(low):
    if not num(low): return {"error":"the low must be a number"}
    if low>40: r=2
    elif low>25: r=3
    elif low>10: r=4.5
    else: r=5.5
    return {"r":r}

def render_pad(r,low):
    return ("Your "+jsnum(low)+" F night wants a pad at R "+jsnum(r["r"])
            +" or better - the bag is only half the insulation; the ground takes its share through the pad.")

def carry_plan(fill):
    if not pos(fill): return {"error":"the fill weight must be above zero"}
    oz=fill*1.9
    return {"oz":r1(oz),"lb":r1(oz/16)}

def render_carry(r,fill):
    return ("Your "+jsnum(fill)+" oz of down wraps up to about "+jsnum(r["lb"])+" lb of bag ("+jsnum(r["oz"])
            +" oz) - the fill weight on the product page is not the carry weight.")

cases=[]
def add(tool,args):
    if tool=="comfort": r=comfort_plan(*args); fn=render_comfort
    elif tool=="pad": r=pad_plan(*args); fn=render_pad
    else: r=carry_plan(*args); fn=render_carry
    case={"tool":tool,"args":args,"result":r}
    if "error" not in r: case["render"]=fn(r,*args)
    cases.append(case)

for a in [(20,),(30,),(15,),(40,),(0,),(10,),(-10,),(25,)]:
    add("comfort",a)
for a in [(15,),(45,),(32,),(8,),(25.5,),(40,),(10,),(60,)]:
    add("pad",a)
for a in [(20,),(12,),(16,),(24,),(8.5,),(30,)]:
    add("carry",a)
add("pad",["warm"]); add("comfort",["freezing"]); add("carry",[0])

json.dump(cases,open("expected.json","w"),separators=(",",":"))
print(len(cases),"cases")
