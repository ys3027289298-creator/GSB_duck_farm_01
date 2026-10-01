import json


def new_game():
    return {'next_id': 1, 'audit': [('a', 1), ('b', 2)], 'used': 1, 'cap': 2, 'count': 0, 'accounts': {}, 'queue': [], 'src': 5, 'dst': 0, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_9(state):
    current_id = state["next_id"]
    state["next_id"] += 1
    return current_id

def bug_16(state):
    return [row for row in state["audit"] if row[0] == "a"]

def bug_23(state):
    return state["cap"] - state["used"]

def bug_0(state):
    if state.get("processed"):
        return False
    state["processed"] = True
    return True

def bug_7(state):
    state["count"] += 1
    return state["count"]

def bug_14(state):
    return state["accounts"].get("missing", 0)

def bug_21(state):
    return False

def bug_28(state):
    return False

def bug_5(state):
    return state["queue"][0]

def bug_12(state):
    amount = 10
    if state["src"] < amount:
        return False
    state["src"] -= amount
    state["dst"] += amount
    return True

def bug_30(state):
    if any(status == "failed" for _, status in state["log"]):
        state["value"] = state["snapshot"]
        return False
    return True

def bug_31(state):
    return not state["settled"]

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
