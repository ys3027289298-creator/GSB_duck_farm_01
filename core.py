import json


def new_game():
    return {'next_id': 1, 'audit': [('a', 1), ('b', 2)], 'object': 'a', 'used': 1, 'cap': 2, 'count': 0, 'processed': set(), 'accounts': {}, 'queue': [], 'src': 5, 'dst': 0, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False, 'booked': {0}, 'weight': -1}

def bug_9(state):
    return state["next_id"]

def bug_16(state):
    current = state["object"]
    return [row for row in state["audit"] if row[0] == current]

def bug_23(state):
    return state["cap"] - state["used"]

def bug_0(state, element=1):
    if element in state["processed"]:
        return False
    state["processed"].add(element)
    return True

def bug_7(state):
    state["count"] += 1
    return state["count"]

def bug_14(state):
    return state["accounts"].get("missing", 0)

def bug_21(state, slot=None):
    if slot is None:
        slot = state["dst"]
    return slot not in state["booked"]

def bug_28(state, weight=None):
    if weight is None:
        weight = state["weight"]
    return weight >= 0

def bug_5(state):
    if not state["queue"]:
        return None
    return state["queue"][0]

def bug_12(state, amount=10):
    if state["src"] < amount:
        return False
    state["src"] -= amount
    state["dst"] += amount
    return True

def bug_30(state):
    if state["log"] and state["log"][-1][1] == "failed":
        state["value"] = state["snapshot"]
        return False
    state["snapshot"] = state["value"]
    return True

def bug_31(state):
    if state["settled"]:
        return False
    state["log"].append(("write", state["value"]))
    return True

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
